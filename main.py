"""BGE-M3 本地向量服务（OpenAI 兼容接口）

启动: ./start.sh
或:   MODEL_PATH=/path/to/bge-m3 python main.py
"""
import json
import logging
import time
from typing import Optional

from fastapi import FastAPI
from FlagEmbedding import BGEM3FlagModel
from pydantic import BaseModel, Field
from config.logger import setup_logging

from config.model_config import get_model_path

# 初始化log 配置
setup_logging()

# GPT-5 修改：模型路径改由启动脚本注入，避免本地与线上路径硬编码冲突。
MODEL_PATH = get_model_path()
DEFAULT_DIM = 1024
MAX_INPUT_LENGTH = 8192

logger = logging.getLogger(__name__)
logger.info('正在从路径 %s 加载 BGE-M3 模型', MODEL_PATH)

app = FastAPI(title='BGE-M3 Embedding Service', version='1.0.0')

model = BGEM3FlagModel(
    MODEL_PATH,
    use_fp16=True,
    return_sparse=False,
    return_colbert_vecs=False,
)
logger.info('BGE-M3 模型加载完成，默认向量维度为 %s', DEFAULT_DIM)


class EmbedRequest(BaseModel):
    dim:int = Field(default=DEFAULT_DIM, max_length=MAX_INPUT_LENGTH, description="向量化维度")
    input: str | list[str]
    model: Optional[str] = 'bge-m3'
    encoding_format: Optional[str] = 'float'


class EmbeddingData(BaseModel):
    object: str = 'embedding'
    embedding: list[float]
    index: int


class EmbedResponse(BaseModel):
    object: str = 'list'
    model: str
    d:int
    data: list[EmbeddingData]
    usage: dict
    message: str = 'success'


@app.get('/health')
def health():
    return {'status': 'ok', 'model': 'bge-m3', 'dim': DEFAULT_DIM, 'device': str(next(model.model.parameters()).device)}


@app.post('/v1/embeddings', response_model=EmbedResponse)
def embeddings(req: EmbedRequest):
    """OpenAI 兼容接口，可直接对接 langchain / openai SDK 等"""
    logger.info("/v1/embeddings req: %s",req.model_dump_json())
    d=req.dim
    texts = [req.input] if isinstance(req.input, str) else req.input
    t0 = time.time()
    dense = model.encode(texts, batch_size=16, max_length=MAX_INPUT_LENGTH)['dense_vecs']
    cost = round(time.time() - t0, 4)
    return EmbedResponse(
        model='bge-m3',
        d=d,
        data=[EmbeddingData(embedding=[float(x) for x in vec], index=i) for i, vec in enumerate(dense)],
        usage={'prompt_tokens': sum(len(t) for t in texts), 'total_tokens': sum(len(t) for t in texts), 'time_cost_s': cost},
    )


class EmbedBatchRequest(BaseModel):
    texts: list[str]
    max_length: int = Field(default=512, ge=10, le=MAX_INPUT_LENGTH)


@app.post('/v1/embed/batch')
def embed_batch(req: EmbedBatchRequest):
    """简化接口：输入文本列表，返回稠密向量 """
    result = model.encode(req.texts, batch_size=10, max_length=req.max_length)
    return {
        'dense_vecs': [v.tolist() for v in result['dense_vecs']]
    }




if __name__ == '__main__':
    import uvicorn
    # 本地启动。 生产环境通过 start.sh 脚本启动
    uvicorn.run(app, host='127.0.0.1', port=8080)

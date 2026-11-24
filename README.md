# 向量模型 BGE-M3

## 参考文档
modelscope: https://www.modelscope.cn/models/BAAI/bge-m3
huggingface: https://huggingface.co/BAAI/bge-m3

## modelscope 示例

### 下载模型-SDK方式
> 看一下 download_bge_m3.py

### 使用案例
1, 安装以来 `uv pip install -U FlagEmbedding`
2, python 脚本示例
```python
from FlagEmbedding import BGEM3FlagModel

model = BGEM3FlagModel('BAAI/bge-m3',
                       use_fp16=True) # Setting use_fp16 to True speeds up computation with a slight performance degradation

sentences_1 = ["What is BGE M3?", "Defination of BM25"]
sentences_2 = ["BGE M3 is an embedding model supporting dense retrieval, lexical matching and multi-vector interaction.",
               "BM25 is a bag-of-words retrieval function that ranks a set of documents based on the query terms appearing in each document"]

embeddings_1 = model.encode(sentences_1,
                            batch_size=12,
                            max_length=8192, # If you don't need such a long length, you can set a smaller value to speed up the encoding process.
                            )['dense_vecs']
embeddings_2 = model.encode(sentences_2)['dense_vecs']
similarity = embeddings_1 @ embeddings_2.T
print(similarity)
# [[0.6265, 0.3477], [0.3499, 0.678 ]]

```

### 对外提供服务（HTTP API）
> 服务端见 main.py，基于 FastAPI，提供 OpenAI 兼容接口，可直接对接 langchain 等框架

1, 启动服务（首次加载模型约 1-2 分钟）
```bash
# 线上启动，默认使用 /opt/embedding/master
./start.sh

# 本地启动，通过环境变量覆盖模型路径
MODEL_PATH='/Users/wanglang/.cache/modelscope/models/BAAI--bge-m3/snapshots/master' ./start.sh

# 后台启动（端口 8080）
nohup ./start.sh > /tmp/bge_m3_server.log 2>&1 &
```

应用启动时必须存在 `MODEL_PATH` 环境变量。`start.sh` 会设置线上默认路径；外部传入的同名环境变量优先，可用于本地或其他部署环境。

2, 接口说明

| 接口 | 说明 |
| ---- | ---- |
| `GET /health` | 健康检查 |
| `POST /v1/embeddings` | OpenAI 兼容接口（返回 dense 向量，维度 1024） |
| `POST /embed` | 简化接口（返回 dense + 词法权重 + colbert 向量） |

3, 调用示例
```bash
# OpenAI 兼容
curl http://127.0.0.1:8080/v1/embeddings -H 'Content-Type: application/json' \
  -d '{"input": ["你好，世界"]}'

# 简化接口
curl http://127.0.0.1:8080/embed -H 'Content-Type: application/json' \
  -d '{"texts": ["文本1", "文本2"], "max_length": 1024}'
```

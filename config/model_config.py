"""BGE-M3 模型配置。"""

import logging
import os

logger = logging.getLogger(__name__)


def get_model_path() -> str:
    """读取模型路径。

    本方法由 GPT-5 生成。

    入参：无，通过 ``MODEL_PATH`` 环境变量读取配置。
    出参：去除首尾空白后的模型目录路径。
    异常：环境变量缺失或内容为空时抛出 ``RuntimeError``。
    """
    model_path = os.getenv('MODEL_PATH', '').strip()
    if not model_path:
        logger.error('MODEL_PATH 环境变量未配置，无法加载 BGE-M3 模型')
        raise RuntimeError('MODEL_PATH 环境变量未配置，请通过 start.sh 设置模型路径')

    logger.info('已读取 MODEL_PATH 环境变量：%s', model_path)
    return model_path

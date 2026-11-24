"""日志配置：统一控制台格式。

被 config 包及 problema 启动时调用一次即可。
"""

from __future__ import annotations

import logging
import os
import sys
from logging import Formatter
from pathlib import Path

_DEFAULT_FORMAT = "%(asctime)s-%(levelname)s-%(thread)s-%(filename)s:%(lineno)d--%(message)s"
_DEFAULT_DATEFMT = "%Y-%m-%d %H:%M:%S"

_LOG_FILE = os.getenv("LOG_FILE", "/opt/logs/detail.log")

_configured = False


def setup_logging(level: int | str = logging.INFO) -> None:
    """初始化文件和控制台日志，不可写时安全回退控制台。（GPT-5 修改）

    :param level: 根日志级别。
    :return: 无返回值。
    """
    global _configured
    if _configured:
        return

    root = logging.getLogger()
    root.setLevel(level)

    if not root.handlers:
        formatter = Formatter(_DEFAULT_FORMAT, _DEFAULT_DATEFMT)
        try:
            Path(_LOG_FILE).parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(_LOG_FILE)
            file_handler.setFormatter(formatter)
            root.addHandler(file_handler)
        except OSError as exc:
            # GPT-5 修改：本地无 /opt 写权限时不阻断应用启动，告警中保留目标路径与原因。
            fallback = logging.StreamHandler(stream=sys.stderr)
            fallback.setFormatter(formatter)
            root.addHandler(fallback)
            root.warning("日志文件不可写，已回退控制台: path=%s error=%s", _LOG_FILE, exc)

        console_handler = logging.StreamHandler(stream=sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        root.addHandler(console_handler)

    _configured = True


def get_logger(name: str) -> logging.Logger:
    setup_logging()
    return logging.getLogger(name)

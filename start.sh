#!/usr/bin/env bash
set -Eeuo pipefail

# 线上默认路径；本地启动时可在命令前传入 MODEL_PATH 覆盖。
readonly DEFAULT_MODEL_PATH='/opt/embedding/master'
readonly LOG_PATH='/opt/logs/embedding_model_bge_m3'
export MODEL_PATH="${MODEL_PATH:-${DEFAULT_MODEL_PATH}}"

# GPT-5 修改：启动前确保日志目录存在，创建失败时由 set -e 直接终止启动。
if [[ ! -d "${LOG_PATH}" ]]; then
  echo "Log directory ${LOG_PATH} does not exist, creating it..."
  mkdir -p "${LOG_PATH}"
  echo "Log directory ${LOG_PATH} created successfully."
fi

export LOG_FILE="${LOG_FILE:-${LOG_PATH}/detail.log}"

echo "Starting embedding server with MODEL_PATH=${MODEL_PATH}, LOG_FILE=${LOG_FILE}..."

exec uvicorn main:app --host 0.0.0.0 --port 8080

echo "Starting embedding server with MODEL_PATH=${MODEL_PATH} succeed"

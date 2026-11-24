from modelscope import snapshot_download
# 默认下载到这里了 ~/.cache/modelscope/models/BAAI--bge-m3/snapshots
#  local_dir 指定下载路径
model_dir = snapshot_download('BAAI/bge-m3')
print(model_dir)
from FlagEmbedding import BGEM3FlagModel
'''

'''
model = BGEM3FlagModel(
    '~/.cache/modelscope/models/BAAI--bge-m3/snapshots/master',
    use_fp16=True,  # Setting use_fp16 to True speeds up computation with a slight performance degradation
    return_sparse=True,
    return_colbert_vecs=True
)

sentences_1 = ["What is BGE M3?", "Defination of BM25"]
sentences_2 = [
    "BGE M3 is an embedding model supporting dense retrieval, lexical matching and multi-vector interaction.",
    "BM25 is a bag-of-words retrieval function that ranks a set of documents based on the query terms appearing in each document",
    '{"request":{"batch":false,"busLine":"PROPERTY","companyUuid":"qingdaohehezhiyuanfa_4d3_saas2_da2f6","estateInfo":{"buildingName":"2","buildingRockId":733055,"buildingUuid":"274CC608-8969-40DA-B766-8F0D140C2429","completeYear":"2017","elevatorFlag":1,"estateName":"海信悦华里(一期)","estateRockId":100444489,"estateUuid":"D0564A8A-1F4A-47F9-AD31-6510CD335575","ownYear":"50","propertyOwnType":{"name":"商品房","uuid":"propertyOwnType-commodityHouse-000"},"roomNo":"1801","roomRockId":50604992,"roomUuid":"48ce0831fcaf4c3ea383269fcd7cd55c","standardLockFlag":true,"structureMode":"buildingUnitRoom","unitName":"1","unitRockId":2097223,"unitUuid":"C56A7C9D-DE14-40E3-89D4-421A9D16CC1F"},"property":{"buildingUuid":"274CC608-8969-40DA-B766-8F0D140C2429","buyPaymentType":"按揭付款","buyTimeType":{"name":"满五","uuid":"purchaseTime-equalFive-0000000000000"},"buyTimeTypeCfgUuid":"purchaseTime-equalFive-0000000000000","companyUuid":"qingdaohehezhiyuanfa_4d3_saas2_da2f6","countBathroom":0,"countHall":1,"countRoom":2,"decoration":{"name":"精装","uuid":"proDecoration-hardCover-000000000000"},"decorationCfgUuid":"proDecoration-hardCover-000000000000","deleted":false,"direction":{"name":"南","uuid":"proDirection-south-00000000000000000"},"directionCfgUuid":"proDirection-south-00000000000000000","externalUpdatedTime":"1786700104233","floorNum":18,"invalidProperty":false,"occupancy":{"name":"空置","uuid":"housingStatus-vacancy-00000000000000"},"occupancyCfgUuid":"housingStatus-vacancy-00000000000000","onlyHouse":0,"ownerMentality":"海信品质 边户二居室 一号线地铁口 精装修 采光好","propertyDesc":"海信品质 边户二居室 一号线地铁口 精装修 采光好","propertyNo":"80814B8F049H0","propertyOwnType":{"name":"商品房","uuid":"propertyOwnType-commodityHouse-000"},"propertyUuid":"accdb1816d034a64be0f27a4604e929d","protectedFlag":false,"rentTag":0,"roomUuid":"48ce0831fcaf4c3ea383269fcd7cd55c","sellPrice":930000.00,"sellTag":1,"square":88.82,"title":"海信品质 边户二居室 一号线地铁口 精装修 采光好","totalFloor":30,"tradeStatus":{"name":"出售","uuid":"propertyStatus-toSell-00000000000000"},"unitUuid":"C56A7C9D-DE14-40E3-89D4-421A9D16CC1F","usageType":{"name":"住宅","uuid":"systemPrimayUsage-houseUsage-0000000"},"usageTypeCfgUuid":"systemPrimayUsage-houseUsage-0000000"},"propertyPhotoList":[{"coverFlag":false,"hashCode":"FsaRxZJpyOR9Frxikr89rQBqAAoj","height":1440,"imageSize":801515,"imageSizeStr":"782.7KB","meta":"image/JPEG","ordered":10004,"photoCategoryCfgUuid":"photoCategory-woshi-0000000000000000","photoURL":"//image.qfstatic.com/qingdaohehezhiyuanfa_4d3_saas2_da2f6/image/2026/08/14/1786700036000/42DA192E-E8D1-4BFC-A7E8-5EA85A7F4D3C.JPEG","propertyUuid":"accdb1816d034a64be0f27a4604e929d","width":1900},{"coverFlag":false,"hashCode":"Fn4_t-rp0zr4we5L2fvJ0RVKmcoH","height":1440,"imageSize":1013576,"imageSizeStr":"989.8KB","meta":"image/JPEG","ordered":10005,"photoCategoryCfgUuid":"photoCategory-woshi-0000000000000000","photoURL":"//image.qfstatic.com/qingdaohehezhiyuanfa_4d3_saas2_da2f6/image/2026/08/14/1786700037000/5736361C-4F29-4F03-9D3F-8EAE912C4255.JPEG","propertyUuid":"accdb1816d034a64be0f27a4604e929d","width":1900},{"coverFlag":false,"hashCode":"Fh_JvlEQ4YRYtdTElyNgjsyOKWpg","height":1280,"imageSize":206731,"imageSizeStr":"201.9KB","meta":"image/JPEG","ordered":10001,"photoCategoryCfgUuid":"photoCategory-huxing-000000000000000","photoURL":"//image.qfstatic.com/qingdaohehezhiyuanfa_4d3_saas2_da2f6/image/2026/08/14/1786700040000/6C9FDCBE-BA39-45E4-9E2D-C31B50839ACD.JPEG","propertyUuid":"accdb1816d034a64be0f27a4604e929d","width":1691},{"coverFlag":true,"hashCode":"FoLucIvK8Ed1stH3fHDMFrvjIUV7","height":1440,"imageSize":667459,"imageSizeStr":"651.8KB","meta":"image/JPEG","ordered":10002,"photoCategoryCfgUuid":"photoCategory-keting-000000000000000","photoURL":"//image.qfstatic.com/qingdaohehezhiyuanfa_4d3_saas2_da2f6/image/2026/08/14/1786700045000/3F173E03-5F04-4EBB-97EE-F5CF9F96CE6F.JPEG","propertyUuid":"accdb1816d034a64be0f27a4604e929d","width":1440},{"coverFlag":false,"hashCode":"FtO0P2JQU7P8GMQJLSLlx70n7YUu","height":1440,"imageSize":694845,"imageSizeStr":"678.6KB","meta":"image/JPEG","ordered":10003,"photoCategoryCfgUuid":"photoCategory-keting-000000000000000","photoURL":"//image.qfstatic.com/qingdaohehezhiyuanfa_4d3_saas2_da2f6/image/2026/08/14/1786700046000/E24B3180-DDDF-4C3F-8447-26D374B5A54A.JPEG","propertyUuid":"accdb1816d034a64be0f27a4604e929d","width":1900},{"coverFlag":false,"hashCode":"Fsty0QJD088B_uyNx3Q7Kx_K7c6S","height":1440,"imageSize":828106,"imageSizeStr":"808.7KB","meta":"image/JPEG","ordered":10006,"photoCategoryCfgUuid":"photoCategory-chufang-00000000000000","photoURL":"//image.qfstatic.com/qingdaohehezhiyuanfa_4d3_saas2_da2f6/image/2026/08/14/1786700050000/2CE14E28-6A4B-4DFA-AB73-94D23ACA1BB3.JPEG","propertyUuid":"accdb1816d034a64be0f27a4604e929d","width":1900}],"traceId":"2088198657986924544@e1e5f8fe79dfa91f"},"dockingList":["SELL","RENT"]}'
    ]
'''
  model.encode() 会返回一个字典，BGE-M3 可以包含多种表示：
  - dense_vecs：稠密语义向量，适合 Milvus、Qdrant、FAISS 等向量检索。默认 True
  - lexical_weights：词法权重，适合稀疏检索。默认 False
  - colbert_vecs：多向量表示，适合更精细的 token 级匹配。默认 False
  
  入参说明：
  sentences_1: 向量化的文本集合
  batch_size：一次批量 12 个文本
  max_length：每条文本分词后的最大 token 个数。一个汉字 ≈ 1个token
'''
embeddings_1 = model.encode(sentences_1,
                            batch_size=12,
                            max_length=1024,
                            # If you don't need such a long length, you can set a smaller value to speed up the encoding process.
                            )
embeddings_2 = model.encode(sentences_2,
                            batch_size=12,
                            max_length=1024,
                            )['dense_vecs']
# 向量 embeddings_1 与 embeddings_2 进行矩阵相乘
similarity = embeddings_1['dense_vecs'] @ embeddings_2.T
'''
输出结果：
[[0.626  0.3477]
 [0.3496 0.678 ]]
 
 输出结果详细解释：
    sentences_1         sentences_2 BGE-M3 文档      sentences_2 BM25 文档
  ━━━━━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━━━━━━━      ━━━━━━━━━━━━━━━━━━━━━━━━━
   What is BGE M3?            0.6265                0.3477
  ────────────────────  ━━━━━━━━━━━━━━━━━━━━━━      ━━━━━━━━━━━━━━━━━━━━━━━━━
   Definition of BM25         0.3499                0.6780
'''
print(similarity)

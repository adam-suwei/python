#pip install elasticsearch5 # 安装对应版本的模块

from elasticsearch6 import Elasticsearch

class esdata(object):

    #ES = ['127.0.0.1:9200']
    # 查找具体数据
    query = {
        "query":{
            "bool":{
            "must":[
                { "match": {"name":'a' } }              
            ]
            }
        },
        "size":100
    }
    
    def __init__(self,ES):
        self._add = ES
         #创建es客户端
        self.es = Elasticsearch(
            self._add,
            # 启动前嗅探es集群服务器
            sniff_on_start=True,
            # es集群服务器结点连接异常时是否刷新es节点信息
            sniff_on_connection_fail=True,
            # 每60秒刷新节点信息
            sniffer_timeout=60  
        )   

    def saveData(self,list):
        doc = self.createdoc(list)
        t = self.es.bulk(index="index1",doc_type='type1',body=doc) 
     
        
        print('insert es successfull ?',t)  

        # r=self.es.search(index="index1",doc_type='type1',body=self.query) 
        # print('es result is:',r)

# 转变数据模型
    def createdoc (self,list):
        doc=[]
        for dup in list:
            doc.append(dict(index={}))
            doc.append(dict(zip(['id','name','age'],dup)))

        print('doc is:',doc)
        return doc


        

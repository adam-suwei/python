from python2es  import esdata
from from_sqlite import  sqlite3data


SQLITE_ADD = 'd:/sqlite/test1.sqlite3'
ES = ['127.0.0.1:9200']

sd = sqlite3data(SQLITE_ADD)
rs = sd.getData()

es = esdata(ES)
es.saveData(rs)


## '.'表示当前执行命令时的路径，不管文件在哪， c:\a>python c:/b/c.py文件，c文件在b目录下。'.'是列出a目录下的文件目录
# '..' 当前执行命令路径的父目录。
# 方法列出路径下所有目录和文件
import os

print('hahaha==',[d for d in os.listdir('.')])  

#----------------------------------------------------
# 在Python中，安装第三方模块，是通过包管理工具pip完成的。
# 在命令提示符窗口下尝试运行pip，如果Windows提示未找到命令，可以重新运行安装程序添加pip。

# pip install Pillow 处理图像的工具库
# 直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库
# 上面提到的Pillow，以及MySQL驱动程序，Web框架Flask，科学计算Numpy等
# 推荐直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库

# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：

# >>> import sys
# >>> sys.path
# ['', 'D:\\Programs\\python382\\python38.zip', 'D:\\Programs\\python382\\DLLs', 'D:\\Programs\\python382\\lib', 'D:\\Programs\\python382', 'C:\\Users\\adam\\AppData\\Roaming\\Python\\Python38\\site-packages', 'D:\\Programs\\python382\\lib\\site-packages

# >>> import sys
# >>> sys.path.append('/Users/michael/my_py_scripts')
# 这种方法是在运行时修改，运行结束后失效。
# 

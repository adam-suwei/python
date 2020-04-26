#-----------------------------------------------------
#class的定义是运行时动态创建的，创建class的方法就是使用type()函数。
# 用class Xxx...来[定义]类，但是，type()函数也允许我们动态[创建]出类来
class Hello(object):
    def hello(self,name ='world'):
        print('Hello--,--%s' % name)


h = Hello()
h.hello()

type(Hello)  
type(h)
# <class 'type'>  类是一个type
# <class '__main__.Hello'>   实例

def fn(self,name='Adam'):
    print('Hello,%s' % name)

Hello = type('Hello',(object,),dict(hello=fn))
H = Hello()
H.hello()
# Hello,Adam

# lass的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
#--------------------------------------------------
# 继承：
# 此为为基类、父类或超类
class Animal(object): #-----此处注入父类
    def run(self):
        print('Animal can runable...')

# 此为子类 继承有什么好处？最大的好处是子类获得了父类的全部功能
class Dog(Animal):  #-----此处注入父类
    def run(self):
        print('Dog can runable...')   #此为多态
    def eat(self):
        print('Dog eat meat...')

class Cat(Animal):
    def run(self):
        print('Cat can run....') #此为多态

#--------------------------------------------------
# 多态：覆盖，重写 就是多态
# 不同子类覆盖父类同名方法，具备不同的功能，称之为多态
dog =Dog()
dog.run()
# Dog can runable...

cat = Cat()
cat.run()
# Cat can run....

a = list()
b = Animal()
c = Dog() 

isinstance(a,list)
isinstance(b,Animal)
isinstance(c,Dog)
# True
# True
# True
isinstance(c,Animal)
isinstance(c,object)
# True
# True

type(a)
type(b)
type(c)
# <class 'list'>
# <class '__main__.Animal'>
# <class '__main__.Dog'>

#----------------------------------------------------
#多态的好处,只要多层父类中有animal，dog cat等子类都可以作为合法参数

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
# Animal can runable...
# Animal can runable....
run_twice(Dog())
# Dog can runable...
# Dog can runable...
run_twice(Cat())
# Cat can run....
# Cat can run....

#动态开发语言---------------------------------------
#证明 run_twice 方法只认类中是否有run方法。不认Animal
class Tortoice(object):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoice())
# Tortoise is running slowly...
# Tortoise is running slowly...



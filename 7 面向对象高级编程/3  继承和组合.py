#---------------------------------------------------
#  多重继承

class Animal(object):
    def ami(self):
        print(' i am a amimal ')


class Mammal(Animal):
    def mam(self):
        print(' I am a Mammal ... ')
class Bird(Animal):
    pass


class Parrot(Bird): #鹦鹉
    pass

class Ostrich(Bird): # 鸵鸟
    pass

class Runnable():
    def run(self):
        print('Running  ...  ')

class Flyable(object):
    def fly(self):
        print(' Flying ... ')

#-----------------------------------------------------------
# Mixin
# 这即可继承，可以实现组合，比如西红柿炒蛋，继承西红柿和炒蛋的味道
class Dog(Mammal,Runnable):
    pass

class Bat(Mammal,Flyable): #蝙蝠
    pass

d = Dog()
d.ami()
d.mam()
d.run()

#  i am a amimal
#  I am a Mammal ...
#  Running  ...

#----------------------------------------------------------
# 面向过程编程

std1 = {'name':'Micheal','score':98}
std2 = {'name':'Bob','score':81}

def print_score(std):
    print('%s,%s' % (std['name'],std['score']))

print(print_score(std1))
print(print_score(std2))

# Micheal,98
# Bob,81

#----------------------------------------------------------
#面向对象编程

class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s,%s' % (self.name,self.score))

bart = Student('adam',88)
lisa = Student('Lisa',89)
bart.print_score()
lisa.print_score()

# adam,88
# Lisa,89
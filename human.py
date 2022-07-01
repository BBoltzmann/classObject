class Human():
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        print("name: ",name,)
        print("age: ",age)
    def speak(self,speak):
        self.speak = input("What do you want me to say? :\n")
        print(self.speak)
    def grow(self):
        print("If you are reading then I am still alive then i'm  older",self.age)
    def eat(self,food,liquid):
        self.food  = food
        self.liquid = liquid
        print("I am  eating", food, "and drinking",liquid)
class Male(Human):
    def __init__(self, name, personality):
        self.name = name
        name = input("New object,  whats your name?: ")
        print("name: ",name,)
        self.personality = personality
        personality = input("Enter any of these personality: extraversion,  agreeableness, openness,  conscientiousness,  neuroticism ")
        if personality=='extraversion':
            print("I am extroverted")
        elif personality=='agreeableness':
            print("I am agreeable")
        elif personality=='openness':
            print("I am open")
        elif personality=='conscientiousness':
            print("I am conscientious")
        elif personality=='neuroticism':
            print("I am neurotic")
        else:
            print("seclect correct personality");
    def speak(self):
        self.speak = input("type  something? :\n")
        print(self.speak) 
# timothy  = Human('Timothy',20)
# timothy.speak("speak")
# timothy.grow()
# timothy.eat("rice","water")

moses = Male(Human("moses","four"),"string")
# moses.eat("rice","water")
moses.speak()



# moses.speak("")
# henry = Dog('Henry',30)







# def add():
#     print ('hello')
# add()

# def new(a,b):
#     return a+b 
# print(new(2,3))

# def get(a):
#     a=  input("what is your name \n")
#     print(a)
# get('string')

# def get():
#     a=  input("what is your name \n")
#     print(a)

# for i in range(3):
#     get()

# def userInfo(name, age, address):
#     name = input("what is your name \n")
#     age = input("How old  are you \n")
#     address = input('country \n')
# userInfo(int,int,int)

# def isGreater(a,b):
#     a = input('Enter a number: ')
#     b = input('Enter a number: ')
#     if a == b:
#         return True
#     else:
#         return False
    
# print(isGreater(2,3))

# def userData(*args):
#     name = input('Enter name: ')
#     age = input('Enter age: ')
#     print(name,age)
# print (userData('strings'))
# def userData():
#     name = input('Enter name: ')
#     age = input('Enter age: ')
#     print(name,age)
# print (userData())
    










#Class
class Person():
    #Property (Yazmana gerek yok ) 
     name = " "
     age = 0
     gender = " "
     job = "developer " #Default Deger
     #method,init
     def __init__(self,name,age,gender):
         self.name=name
         self.age=age
         self.gender= gender
         
Person1 = Person("Onder", 22, "Male")
Person1.age
Person1.name 
Person1.job="Siber Güvenlik Uzmanı"
Person1.job

class Dog():
    year= 7
    def __init__(self,age):
        self.age=age
        
        print("Dog İnstance")
    def HumanAge(self):
        return self.age * self.year # Dog.year -> Self.year
        
myDog=Dog(3)
myDog.age


barley = Dog(2)
barley.HumanAge()


#Inheritance (Kalıtım)  Oop

class Musician():
    def __init__(self,name):
        self.name=name
        print("Musician class")
        
    def test1(self):
        print("Test1")
        
    def test2(self):
        print("Test2")
        
onder= Musician("Onder")
onder.name  
onder.test1()
        
class MusicianPlus(Musician):
    def __init__(self,name):
        Musician.__init__(self,name)
        print("musicianPlus")
        
    def test3(self):
        print("Test3")
        
    def test1(self):
        print("Test1-Test1")  #Overrating

atlas= MusicianPlus("Atlas")
atlas.test2()
atlas.test3()
onder.test2()
atlas.test1()


#Polymorphism

class Banana():
    def __init__(self,name):
        self.name= name 
        
    def info(self):
        return f"100 calories {self.name}"
    
class Apple():
    def __init__(self,name):
        self.name= name 
        
    def info(self):
        return f"150 calories {self.name}"
    
apple= Apple("Apple")
banana= Banana("Banana")

apple.info()
banana.info()
 #2 info var ikiside aynı işlevi yapıyor.
 
fruitList=[apple,banana]
for fruit in fruitList:
    print(fruit.info())  #Farklı işlevlerde olsa aynı ismi kullanarak yapılabilir.
    
#Encapsulation

class Phone():
    
    def __init__(self, name, price):
        self.name = name
        self.__price = price
        
    def info(self):
        print(f"{self.name} fiyatı: {self.__price}")
        
    def changePrice(self, price):
        self.__price = price
        
iphone = Phone("İphone 14", 9000)
iphone.info() # Bu şekilde fiyatı yazdırılacaktır
iphone.changePrice(300)
iphone.info() # Fiyat 300 olarak güncellendi

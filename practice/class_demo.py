
from practice.first import INDENT_IN_OUTPUT
from builtins import int


print (INDENT_IN_OUTPUT, 'class demo')  

def main():
#     static_method()
#     inheritance_demo()
#     singleton()
#     factory_demo()
#     slots()
#     decorator()
#     descriptor()
    type_checked()
    pass

def type_checked():
    
    class Contract():
        
        @classmethod
        def check (cls, value):
            pass
            
    class Type:
        type = None
        
        @classmethod
        def check (cls, value):
            assert isinstance(value, cls.type),"Expected type is {}".format(cls.type)
            
    class Integer(Type):
        type = int
        
    class Positive(Contract):
        
        @classmethod
        def check(cls, value):
            assert value >0, "value shuld be greater than 0"
        
    class PositiveInteger (Positive, Integer):
        pass
    
    a = Integer.check(1)
    b = PositiveInteger.check(-1)
    
    print(a)
    print(b)

def descriptor():
    
    class Alphabet:  
        def __init__(self, value):  
            self._value = value  
                
        # getting the values      
        @property
        def value_1(self):  
            print('Getting value_1')  
            return self._value  
                
        # setting the values      
        @value_1.setter # descriptor
        def value_1(self, value):  
            print('Setting value_1 to ' + value)  
            self._value = value  
                
        # deleting the values  
        @value_1.deleter   #descriptor
        def value_1(self):  
            print('Deleting value_1')  
            del self._value  
    
    
    # passing the value_1  
    x = Alphabet('Peter')  
    print(x.value_1)  
        
    x.value_1 = 'Diesel'
        
    del x.value_1  

def decorator():
    # class decorator 
      
    class ErrorCheck: 
      
        def __init__(self, function): 
            self.function = function 
      
        def __call__(self, *params): 
            if any([isinstance(i, str) for i in params]): 
                raise TypeError("parameter cannot be a string !!") 
            else: 
                return self.function(*params) 
      
      
    @ErrorCheck
    def add_numbers(*numbers): 
        return sum(numbers) 
      
    #  returns 6 
    print(add_numbers(1, 2, 3))  
      
    # raises Error.   
    print(add_numbers(1, '2', 3))   

def slots():
    class A():
        __slots__ = ["val"]
        def __init__(self, val):
            self.val = val
    
    a = A(2)
    a.val_1 = 3 # will give the error because of slots defined
            
def factory_demo():
    
    class A():
        def print_obj(self):
            return "A"

    class B():
        def print_obj(self):
            return "B"
        
    def fun(obj ):
        objs = dict(a=A(), b=B())
        return objs[obj]

    print(fun('a').print_obj())

def singleton():
    
    class Metaclass(type):
        __instance = {}
        
        def __call__(cls, *args, **kwargs):
            if cls not in cls.__instance:
                cls.__instance[cls] = super(Metaclass, cls).__call__(*args, **kwargs)
                return cls.__instance
    
    class A(metaclass= Metaclass):
        def __init__(self):
            pass
    
    obj = A()
    print(obj) # print address
    obj1 = A()
    print (obj1) # NONE
    print(A.__mro__)

def static_method():
    class Calculator:
        
        var_initial = 0 
        _private_var = 1  # private var
        __protected_var = 2 # protected var
        
        @property
        def get_scientific(self):
            """ @property decorator """
            print("I am scientific calc")
            
        @staticmethod
        def addNumbers( a, b):
            return a + b;
        
        def class_var_access(cls):
            print("class variable access :", cls.var_initial)
        
        def __str__(self):
            return "print class :-" + "private var :" + str(self._private_var)
            
    a = Calculator.addNumbers( 5, 6)
    print(a)
    Calculator.sum = staticmethod(Calculator.addNumbers)
    print(Calculator.sum(5,7))
    
    obj = Calculator()
    print(obj.get_scientific)
    obj.class_var_access()
    obj._private_var = 1 
    obj.__protected_var = 2
    print(obj)
    
        
def inheritance_demo():
    # Inheritance -> multiple, multilevel
    
    class Phone_base:
        def __init__(self, color):
            self.color  = color
    
    class Phone(Phone_base):
        def __init__(self,color, brand):
            super().__init__(color)
            self.brand = brand
            
        def set_color(self, color):
            self.color = color
            
        def get_color (self):
            return self.color
    
    phone_moto = Phone("Red", "mi");
    phone_moto.set_color("blue")
    print(phone_moto.get_color())
       
if __name__ == "__main__":
    main()
    
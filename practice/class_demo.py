
from practice.first import INDENT_IN_OUTPUT


print (INDENT_IN_OUTPUT, 'class demo')  

def main():
    static_method()
#     inheritance_demo()

def static_method():
    class Calculator:
        
        var_initial = 0 
        _private_var = 1  # private var
        __protected_var = 2 # protected var
        
        @property
        def get_scientific(self):
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
    
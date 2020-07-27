
from practice.first import INDENT_IN_OUTPUT


print (INDENT_IN_OUTPUT, 'class demo')  

def main():
#     static_method()
    inheritance_demo()

def static_method():
    class Calculator:
        @staticmethod
        def addNumbers( a, b):
            return a + b;
        
    a = Calculator.addNumbers( 5, 6)
    print(a)
    Calculator.sum = staticmethod(Calculator.addNumbers)
    print(Calculator.sum(5,7))
        
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
    
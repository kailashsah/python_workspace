
from test import INDENT_IN_OUTPUT 



# lambda

print(INDENT_IN_OUTPUT, "using lambdas")

def main():
#     get_cube(10)
#     reduce_demo()
#     test()
#     get_odd_numbers()
    global_demo()
     
def get_cube(x):
   
    lam = lambda x: x*x*x
    print (lam(10))

list1 = [1,3,4,8,9]
print("source list is", list1)

def get_odd_numbers():
   
    list_odd = list(filter(lambda x: (x%2!=0), list1)) # list odd numbers
    print("odd numbers are :", list_odd)

def reduce_demo():
    from functools import reduce # reduced to consolidated value
    sum_list = reduce(lambda x,y: x+y, list1)
    print("reduce result is :", sum_list)
    
def test():    
    list_task_mul_2 = list(map(lambda x : x*2,list1))  # map all no multiply by 2 and list it
    print("multiply by 2 result in :", list_task_mul_2)
    
g_a = 10
def global_demo():
    global g_a
    g_a = 5
    print(g_a)
    globals()['g_a']= 10
    print(g_a)

if (__name__ == '__main__'):
    main()
    
    
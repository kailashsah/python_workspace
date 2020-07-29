
INDENT_IN_OUTPUT  = "---------"

def main():
 
#     args_demo()
#     kwargs_demo()
#     pandas_demo()
#     numpy_demo()
    test()
    
    
def test():
    a1 = 10
    print(type(a1))
    print("divison is",  a1/1.2)
    
    # strings
    
    b = "My name is Python"
    print(len(b)) 
    c = b.replace('name', 'a', 1) # My a is Python
    print(c)
    c = b.split(' ')  # ['My', 'name', 'is', 'Python']
    print (c) 
    
    
def numpy_demo():
        # numpy -> shape, random.randint, vstack, hstack, column_stack(), 
    #        intersect1d, setdiff1d (difference), 
    #        sum([n1,n2]), sum([n1,n2], axis = 0) for columns sum 
    #        n1 = n1+1, n1=n1-1, n1=n1*2, n1=n1/2,
    #        mean, median, std (standard deviation), save(), load()
    import numpy as np
    
    print(INDENT_IN_OUTPUT, 'using numpy')
    np_z = np.zeros((10,10))
    np_z = np.full((10,10), 10) # set all elements to 10
    np_z = np.arange(10,20, 5) #  output is [10,15]
    print(np_z)
    
    
def pandas_demo():
    # pandas -> panel data, data manipulation
    #        s[1] (element at index), s[:4] (first four elements) , s[-3:] (last 3 elements)
    #        s+ 5, s1+ s2
    import pandas as pd
    
    print(INDENT_IN_OUTPUT, 'using pandas')
    pd1 = pd.Series([0,19,27,'a'])
    print(pd1)
    pd1 = pd.DataFrame({'keys':["a", "a", "a"] ,'values':["100", "100", "100"]} )
    print(pd1)
    
    # iris = pd.read_csv('iris.csv')
    # print(iris.describe())  # head(), tail(), shape(), iloc[0:3, 0:2] (extract first 3 rows and 2 columns)
    #      drop('column_name', axis=1) drop column, drop ([1,2,3], axis =0) drop rows
    #     min(), max(), mean(), median()
    #     def half(x): return x*0.5   iris['[column1', 'column2']].apply(half)
    #    iris.['column'].value_counts(), iris.sort_values(by= 'column')
    #    
        

def args_demo():
    print(INDENT_IN_OUTPUT, "args demo")
    
    def fun_sum(*args):
        sum = 0
        for i in args:
            sum += i
        return sum
    
    print("args fun print :", fun_sum(10,20)) # print 30
    print("args fun print :", fun_sum(10,20, 30)) # print 60
    
    
def kwargs_demo():
    print(INDENT_IN_OUTPUT, "**kwargs demo")   
    def fun_print (**kwarg):
        print(kwarg)
        
    print(fun_print(kawarg1 = "one", kawarg2 = 2)) # {'kawarg1': 'one', 'kawarg2': 2}

if ( __name__ == '__main__'):
     print("main")
     main()
    

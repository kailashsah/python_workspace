

from matplotlib.lines import lineStyles

INDENT_IN_OUTPUT  = "---------"
a1 = 10
def main():

    print(type(a1))
    print("divison is",  a1/1.2)
    
    # strings
    
    b = "My name is Python"
    print(len(b)) 
    c = b.replace('name', 'a', 1)
    c = b.split(' ')
    print (c)
    
   
    
    
    
   
    
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
    
    
    # matplotlib ->
    
    from matplotlib import pyplot as plt, pyplot
    
    TIME_TO_PAUSE = 1
    print(INDENT_IN_OUTPUT, "using matplotlib")
    


if ( __name__ == '__main__'):
     print("main")
     main()
    

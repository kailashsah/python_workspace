

from matplotlib import pyplot as plt
import numpy as np
# from asyncio import __main__

INDENT_IN_OUTPUT  = "---------"
TIME_TO_PAUSE = 1
print(INDENT_IN_OUTPUT, "using matplotlib")

def pie_plot():
    fruit = ['apple', 'orange', 'grapes']
    quantity = [10,30,50]
    plt.pie(quantity, labels=fruit)
    plt.pause(1)
    plt.close()
    
def plot_demo():
    x= np.arange(1,11)
    y= x*2
    
    # plt.subplot(1,2,1)
    plt.plot(x,y, color='g', linestyle= ":", linewidth=5)  # title(), xlabel(), ylabel()
    plt.grid(True)
    #plt.show()
    plt.pause(TIME_TO_PAUSE)
    plt.close()

def bar_demo():
    student = {'a': 100, 'b': 200,'c': 400,}
    x = list(student.keys())
    y = list(student.values())
    plt.bar(x, y) # bar graph -> barh() horizontal graph
    # plt.show()
    plt.pause(TIME_TO_PAUSE)
    plt.close()
    
def scatter_plot():
    x = [10,20,30,60,100]
    a = [1,2,3,4,10]
    
    plt.scatter(x, a)  # scatter graph, two scatter in one graph also possible, change market and color    
    plt.pause(TIME_TO_PAUSE)
    plt.close()
    
def histogram_demo():
    # histogram
    x = [1,3,5,6,7,7]
    plt.hist(x, color ='g', bins= 5)
    plt.pause(2)
    plt.close()
    # hist(iris['column'], color, bins) # load the csv befor you go

def box_plot():
    # box plot

    x = np.arange(1,10)
    y = np.arange(20,0)
    z = np.arange (1,10)
    data = list ([x,y,z])
    plt.boxplot(data)
    plt.pause(TIME_TO_PAUSE)
    plt.close()

def violin_plot():
    
    xx = np.arange(1,10)
    plt.violinplot(xx, showmedians=True)
    plt.pause(TIME_TO_PAUSE)
    plt.close()

if (__name__ == "__main__"):
#     bar_demo()
#     plot_demo()
#     scatter_plot()
#     histogram_demo()
#     box_plot()
#     violin_plot()
    pie_plot()
    
    
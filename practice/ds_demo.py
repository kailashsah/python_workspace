
from practice.first import INDENT_IN_OUTPUT
from _collections import defaultdict

print(INDENT_IN_OUTPUT, "using tuple")

def main():
#     tuple_demo()
    dict_demo()

def tuple_demo():
    # Tuple -> immutable
    tup = (1, 'sss', 3.14)
    tup_int = (1,2,3)
    print("max element in the tuple : ", max(tup_int)) 
    print("second element tup[1] in the tuple ", tup[1])

    if 3 in tup_int:
        print('3 is present in tuple')

def dict_demo():
    d = defaultdict(list)
    for i in range(5):
        d[i] = i+1
    print(d)
    d.clear()
    
    d = defaultdict(lambda: "not present")
    d[1] = 'a'
    print(d)
    print("d['c'] : ", d['c'])  # not present
    print("d.__missing__(1) :" , d.__missing__(1))
    
    
    
# list -> mutable, reverse, insert, sort, l1 + l2, L1*3 + l2
# dictionary -> mutable, unordered collection, d1.keys(), d1.values(), d1.pop("key")
# Set ->    unordered, unindexed collection, unique elements, add(), update([1,2,3]), 
#           remove("1"), union(), intersection

if __name__ == '__main__':
    main()
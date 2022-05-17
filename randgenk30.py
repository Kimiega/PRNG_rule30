import numpy
from random import randint as std_randint

def resetTree():
    global rand_generator_tree_ka30
    global tree_ka30_iter
    
    rule30 = {
    '111':0,
    '110':0,
    '101':0,
    '100':1,
    '011':1,
    '010':1,
    '001':1,
    '000':0
    }
    
    rand_generator_tree_ka30 = numpy.zeros((200,300),dtype=numpy.int8)

    tree_ka30_iter = len(rand_generator_tree_ka30)//2
    
    while True:
        start_num = bin(std_randint(0,int("1"*len(rand_generator_tree_ka30[0]),2)))[2:]

        if ("1"*25  or "0"*25) in start_num:
            continue
        else: 
            break
        
    start_num = "0"*(len(rand_generator_tree_ka30[0])-len(start_num)) + start_num
    
    for iterx in range(len(rand_generator_tree_ka30[0])):
        rand_generator_tree_ka30[0][iterx] = start_num[iterx]

    for i in range(1,len(rand_generator_tree_ka30)):
        for j in range(len(rand_generator_tree_ka30[0])):
            xt = [0,0,0]
            if j!=0:
                xt[0]=rand_generator_tree_ka30[i-1][j-1]
            if j!=len(rand_generator_tree_ka30[0])-1:
                xt[2]=rand_generator_tree_ka30[i-1][j+1]
            xt[1] = rand_generator_tree_ka30[i-1][j]
            xstr = str(int(xt[0]))+str(int(xt[1]))+str(int(xt[2]))
            rand_generator_tree_ka30[i][j]=rule30[xstr]


def nextRandom(a=None,b=None):
    global tree_ka30_iter
    if a == None and b == None:
        a = 0
        b = 4294967295
    elif b == None:
        b = a
        a = 0
    if a>b:
        a,b = b,a
    if tree_ka30_iter>=len(rand_generator_tree_ka30[0]):
        resetTree()
    
    rand_num_list = rand_generator_tree_ka30[:,tree_ka30_iter]
    rand_num_str = ''.join(str(e) for e in rand_num_list)
    rand_num = int(rand_num_str,2)
    tree_ka30_iter+=1
    return rand_num % (b-a+1) + a
    
rand_generator_tree_ka30 = 0
tree_ka30_iter = 0
resetTree()

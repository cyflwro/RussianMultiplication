import random
def diva(a):
    """
    sub function to divide a by 2, discarding remainder if exist.
    continue for result
    calculation stops at 1
    returns all calculation as list
    """
    if a==1:
        return a 
    else:
        list_a=[a]
        brk=False
        while brk!=True:
            list_a.append(list_a[-1]//2)
            if list_a[-1]==1:
                brk=True
        return list_a
def multib(len_a,b):
    """
    multiply b by 2
    continue for result
    operation stops at len_a
    """
    if len_a==1:
        return b
    else:
        list_b=[b]
        for i in range(1,len_a,1):
            list_b.append(list_b[-1]*2)
        return list_b
def even(i):
    """
    checks if i is even or odd, return a boolean answer
    """
    return True if i%2==0 else False
def rusmul_working(a,b):
    """
    this is the same as rusmul function but shows the workings
    
    multiplication using the Russian method as described in numberphile
    refer to link (youtube) below
        https://www.youtube.com/watch?v=HJ_PP5rqLg0
        guest in video is Johnny Ball
        
    also refer to Wolfram Alpha explanation:
        http://mathworld.wolfram.com/RussianMultiplication.html
    """
    list_a=diva(a)
    print(a,'x',b,'using the Russian Multiplication')
    print('Dividing',a,'-> ')
    print(list_a)
    if type(list_a)==int:
        print('multiplying by 1, so:')
        print('Answer is =',b)
        return b
    else:
        list_b=multib(len(list_a),b)
        for i,a_v in enumerate(list_a):
            if even(a_v) is True:
                list_b[i]=0
        print('Multiplying',b,'-> ')
        print(list_b)
        answer=0
        for b_v in list_b:
            answer+=b_v
        print('Discarding multiplications at "evens" positions')
        print(list_b)
        print('Summing them gives',answer)
        return answer        
def rusmul(a,b):
    """
    multiplication using the Russian method as described in numberphile
    refer to link (youtube) below
        https://www.youtube.com/watch?v=HJ_PP5rqLg0
        guest in video is Johnny Ball
        
    also refer to Wolfram Alpha explanation:
        http://mathworld.wolfram.com/RussianMultiplication.html
    """
    list_a=diva(a)
    if type(list_a)==int:
        return b
    else:
        list_b=multib(len(list_a),b)
        for i,a_v in enumerate(list_a):
            if even(a_v) is True:
                list_b[i]=0
        answer=0
        for b_v in list_b:
            answer+=b_v
        return answer   
def test_list_inputs(sample_size=100,min_num=1,max_num=999999):
    """
    test_list_inputs(sample_size,min_num=1,max_num=999999)
    
    generates 2 lists for test use
    must be integers
    results in integers
    """
    
    test_list_a=[]
    test_list_b=[]
    for i in range(1,sample_size,1):
        test_list_a.append(random.randint(min_num,max_num))
        test_list_b.append(random.randint(min_num,max_num))
   
    return test_list_a, test_list_b
def normal_multiplication(a,b):
    answer=a*b
    return answer
def check_accuracy(size=100,intent_error=0):
    """
    checking if rusmul function is accurate vs normal multiplication
    change error to 1 to introduce error (use this to validate this function)
    """
   
    listas,listbs=test_list_inputs(size)
    
    answer_rusmul=[]
    answer_normal_multi=[]
    
    for i,j in enumerate(listas):
        answer_rusmul.append(rusmul(j,listbs[i]))
        answer_normal_multi.append(normal_multiplication(j,listbs[i]))
    
    if intent_error!=0:
        answer_rusmul[random.randint(1,size)]+=1
                             
    bad_answer=False
    for ii,jj in enumerate(listas):
        if answer_rusmul[ii]!=answer_normal_multi[ii]:
            bad_answer=True
            return bad_answer
    return bad_answer
def rus_mul_v_normal_mult_time(size,min_num=1,max_num=99):
    """
    checking if rusmul function is faster vs normal multiplication
    """
    import time
        
    listas,listbs=test_list_inputs(size,min_num,max_num)
    
    answer_rusmul=[]
    answer_normal_multi=[]
    
    print('begin Normal Multiplication')
    start = time.process_time()
    for ii in range(0,size-1,1):
        answer_normal_multi.append(normal_multiplication(listas[ii],listbs[ii]))
        normal_time=time.process_time()-start
    print('Completed normal multiplication in',normal_time)
    
    print('begin Russian Multiplication')
    start = time.process_time()
    for i in range(0,size-1,1):
        answer_rusmul.append(rusmul(listas[i],listbs[i]))
        rusmul_time=time.process_time() - start
    print('Completed Rusmul in',rusmul_time)
    


    return listas,listbs,answer_rusmul
    
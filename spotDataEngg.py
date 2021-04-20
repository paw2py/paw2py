# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

.pydef listsong(lst):
    tmpdist = {}
    
    for i in lst:
        if i[0] in tmpdist:
            tmpdist [i[0]].append(i[1])
        else:
            tmpdist[i[0]] = [i[1]]
    print('paw',tmpdist)
    
    cntdist = {}
    for i in tmpdist:
        tmparr = tmpdist[i]
        for j in range(len(tmparr)-2):
            s = ''.join(tmparr[j:j+3])
            if s in cntdist:
                cntdist[s]+=1
            else:
                cntdist[s] = 1
    print('finalcnt', cntdist)        
    return 0
            

def doTestsPass():
    """ Returns true if the tests pass. Otherwise, returns false """

    # TOD = O: implement more test cases
    tc1 = [ [ "D", "s" ],
            [ "D", "p" ],
            [ "M", "s" ],
            [ "M", "s" ],
            [ "D", "t" ],
            [ "D", "q" ],
            [ "M", "t" ],
            [ "M", "s" ],
            [ "M", "p" ],
            [ "M", "t" ]
             ];
    return listsong(tc1) == 87


if __name__ == "__main__":
    result = doTestsPass()

    if result:
        print("All tests pass\n");
    else:
        print("Tests fail\n") ;           

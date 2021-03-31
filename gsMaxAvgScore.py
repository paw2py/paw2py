import operator
def bestAverageGrade(scores):
    # TODO: implement this function
    tmpdist = {}
    cnt = 1
    avg= 0
    for i in scores:
        
        if i[0] in tmpdist:
            tmpdist[i[0]] = [(tmpdist[i[0]][0]+int(i[1]))//2]
        else:
            tmpdist[i[0]] = [int(i[1])]
    
    #avglist = list(tmpdist.values())     
    avglist = max(tmpdist,key=tmpdist.get)
    print(tmpdist)
    print(avglist)
    
    return tmpdist[avglist][0]

def doTestsPass():
    """ Returns true if the tests pass. Otherwise, returns false """

    # TODO: implement more test cases
    tc1 = [ [ "Bobby", "87" ],
            [ "Charles", "100" ],
            [ "Eric", "64" ],
            [ "Charles", "22" ] ];
    return bestAverageGrade(tc1) == 87


if __name__ == "__main__":
    result = doTestsPass()

    if result:
        print("All tests pass\n");
    else:
        print("Tests fail\n");

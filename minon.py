#hakerrank minion problem
def minion_game(string):
    # your code goes here
    strv = 'AEIOU'
    kevin = 0
    stuart = 0
    strlen =  len(string)   
    
    
    for idx in range(strlen):
        if string[idx] in strv:
            kevin += strlen-idx
        else:
            stuart += strlen-idx    
                 
    if kevin == stuart:
        print('Draw')
    elif stuart > kevin:
        print('Stuart ' + str(stuart))
    else:
        print('Kevin ' + str(kevin))


if __name__ == '__main__':
    s = input()
    minion_game(s)
#https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

def tokenize(s):
    return s.split(' ')

if __name__=='__main__':
    l1 = input()
    l2 = input()
    l3 = input()
    l4 = input()

    happiness = 0
    l1s = tokenize(l1)
    n = l1s[0]
    m = l1s[0]
    arr = tokenize(l2)
    A = tokenize(l3)
    B = tokenize(l4)
    
    happyints = {k: 1 for k in A}
    sadints = {k: -1 for k in B}
    
    allints = {**happyints, **sadints}

    for i in arr:
        try:
            happiness += allints[i]
        except KeyError:
            continue

    print(happiness)
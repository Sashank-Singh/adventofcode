import sys

def firstdigit(a):
    n = len(a)
    for i in range(n):
        if a[i].isdigit():
            return a[i]

def lastdigit(a):
    n = len(a)
    for i in range(n-1, -1, -1):
        #print('>>>', i, repr(a[i]))
        if a[i].isdigit():
            return a[i]
result = 0 
for line in sys.stdin:
    line = line.strip()
    #print('DEBUG:', repr(line))

    twoofem = str(firstdigit(line)) + str(lastdigit(line))
    result += int(twoofem)

    #result = result + twoofem
    print(result)
    
    







    



    
    

    

    



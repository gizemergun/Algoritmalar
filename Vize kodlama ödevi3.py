import random
def median(myList,a):
    pivot=random.choice(myList)
    right_myList=[]
    left_myList=[]
    if a == len(myList):
       return max(myList)
    for i in myList:
        if pivot < i:
            right_myList.append(i)
        elif pivot >= i:
            left_myList.append(i)
    if len(left_myList) >= a:
        return (median(left_myList,a))
    elif len(left_myList) < a:
        return (median(right_myList,(a - len(left_myList))))
    if len(left_myList)+1==a:
        return pivot
myList = [1,2,3,4,5,6,7,8]
x = int(len(myList)/2)
if len(myList)%2 == 0:
    a = median(myList, x)
    b = median(myList, x+1)
    print (float((a+b)/2))
else:
    ortanca = median(myList,x+1)
    print (ortanca)

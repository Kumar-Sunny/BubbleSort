import time
import random
def BubSort(ar):
    for i in range(len(ar)):
        flg=False
        for j in range(len(ar)-1-i):
            if ar[j]>ar[j+1]:
                ar[j],ar[j+1]=ar[j+1],ar[j]
                flg=True
        if flg==False:
            break



n=int(input("Enter the number of Test Cases: "))
bCase=[]
wCase=[]
avgCase=[]
for i in range(n):
    s=int(input())
    arr=[]
    for j in range(s):
        arr.append(random.randrange(100))
        #AverageCase
    st=time.time()
    BubSort(arr)
    ed=time.time()
    avgCase.append(ed-st)
    #BestCase
    st=time.time()
    BubSort(arr)
    ed=time.time()
    bCase.append(ed-st)
    #WorstCase
    arr.reverse() 
    st=time.time()
    BubSort(arr)
    ed=time.time()
    wCase.append(ed-st) 
print("\n\nBest Case: ",bCase)
print("\n\nAverage Case: ",avgCase)
print("\n\nWorst Case: ",wCase)


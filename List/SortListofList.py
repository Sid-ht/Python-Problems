def sortList(myList):
    for i in range(0,len(myList)):
        if isinstance(myList[i][1],list):
            myList[i][1].sort()
    return myList

myList = [('business',['sales','infra','hr']),('region',['ind','amer','jap'])]

print(sortList(myList))

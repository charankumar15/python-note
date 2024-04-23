arr = [2,3,4,8,9]
for i in range(len(arr)):
    if (arr[i]%2) ==0:
        arr[i] +=2
    elif (arr[i]%3) ==0:
        arr[i] *= 3

print(arr)


arr = [2,3,6,12,4,8,9] #if 6,12 val was same use 
for i in range(len(arr)):
    if (arr[i]%6) ==0:
         arr[i] = 0
        
   
    
    
    elif (arr[i]%2) ==0:
        arr[i] +=2
    elif (arr[i]%3) ==0:
        arr[i] *= 3

print(arr)


arr = [[1,2],[3,4],[5,6]]
print(arr[0][0])

arr = [[1,2],[3,4],[5,6]]
print(arr[1][0])

arr = [[1,2],[3,4],[5,6]]
print(arr[2][0])

arr = [[1,2],[3,4],[5,6]]
print(arr[0][1])

#arr = [[1,2],[3,4],[5,6]]
#print(arr[][])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] +=1
print(arr)        
        
        




















    

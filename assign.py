arr= ['2' , '3', '4' ]
arr[0] = ['3']
arr[1] = ['4']
arr[2] = ['6']
for i in str(arr):
     print(i, end = "")


arr = ['1', '2', '3']
arr[0] = ['2']
arr[1] = ['3']
arr[2] = ['4']
for i in str(arr):
    print(i, end = "")

arr = ['2', '3', '5']     # for i in range(1,10):
                           # print(i)

#for i in range(2):
   # arr[i] +=1
   # print(arr)


for i in range(len(arr)):

  arr[i] = str(int(arr[i]) +1)
      print(arr)


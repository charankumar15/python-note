with open("file-handling.txt") as file:
    data = file.read()
print(data)    

with open("file-handling.txt") as file:
    data = file.read(11)  #total char
print(data) 

with open("file-handling.txt") as file:
    file.seek(5)  #remove the first value
    data = file.read(10)
print(data)

with open("file-handling.txt") as file:
    #file.seek()
    data = file.readlines()
print(data)


with open("file-handling.txt" , "r") as file:
    data = file.read()
with open("file-handling-copy.txt" , "w") as file:
    file.write(data)    


 #"avb12bgtyuikm"

with open ("file-handling.copy.txt" , "a") as f:
    f.write("\n new comee")
     
with open ("file-handling.txt", "r") as f:
    print(f.readline())
    print(f.tell())
    print(f.readline())
    print(f.tell())

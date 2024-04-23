
#prattern


print("""

    *
   * * 
  * * *
 * * * * 
* * * * *
""")
space_count =4
star_count =1
no_of_iters =5

for i in range(no_of_iters):
    print(" " *space_count + "* "*star_count)
    space_count = space_count -1
    star_count = star_count +1

   #function call

def pyramid_pattern(space_count ,star_count ,no_of_iters):
    for i in range(no_of_iters):
        print(" " *space_count + "* "*star_count)
        space_count = space_count -1
        star_count = star_count +1


    
pyramid_pattern(2,1,3)

#while loop

count = 0

while count < 10:
    print(count)
    count = count + 1


    #extention



   
    

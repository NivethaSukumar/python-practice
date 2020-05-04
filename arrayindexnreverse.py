import array
arr=array.array('i',[1,2,3,4,2,1,7])
print("The newly created array is:", end="")
for i in range(7):
    print(arr[i], end="")
print("\r")
print("The index of first occurence of 2 is: ", end="")
print(arr.index(2))
print("\r")
arr.reverse()
print("The reversed array is : ", end ="")
for i in range(7):
    print(arr[i], end="")



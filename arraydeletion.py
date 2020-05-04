import array
arr=array.array('i',[1,2,3,4,1,5])
print("The newly created array is :", end="")
for i in range(6):
    print(arr[i], end ="")
print("\r")
print("The popped element is:",end="")
print(arr.pop(3))
print("\r")
print("After popping, the array is :", end="")
for i in range(5):
    print(arr[i], end ="")
print("\r")
arr.remove(1)
print("The array after removing is : ", end="")
for i in range(4):
    print(arr[i], end ="")
print("\r")

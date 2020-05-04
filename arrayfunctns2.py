import  array
arr1=array.array('i',[1,2,4,5,7,2,7,3])
arr2=array.array('i',[1,2,4,8,3])
li=[1,2,3]
print("The datatype of the array is :", end="")
print(arr1.typecode)
print("The itemsize of the array is :", end="")
print(arr1.itemsize)
print("The buffer info of array is :", end="")
print(arr1.buffer_info())
print("The occurences of 7 in array 1 is:", end="")
print(arr1.count(7))
arr1.extend(arr2)
print("The modified array is:", end="")
for i in range(13):
    print(arr1[i], end="")
print("\r")
arr2.fromlist(li)
print("The modified array is:", end="")
for i in range(8):
    print(arr2[i], end="")
print("\r")
li2=arr2.tolist()
print("The new list created is:", end="")
for i in range(5):
    print(li2[i], end="")

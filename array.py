import array
arr = array.array('i',[1,2,3])
print("The newly created array is: ", end="")
for i in range(0,3):
    print(arr[i],end="")

print("\r") 




arr.append(5);
print("The appended array is : ", end="")
for i in range(0,4):
      print(arr[i],end="")
arr.insert(3,4)

print("\r") 



print("After insertion:")
print("The array is : ",end="")
for i in range(0,5):
      print(arr[i],end="")
      

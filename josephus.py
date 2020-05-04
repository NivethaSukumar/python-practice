def josephus(n, k): 
  
      if (n == 1): 
          return 1
      else: 
          return (josephus(n - 1, k) + k-1) % n + 1 
  
n = input("Enter the number of players:");
k = input("Enter the value of k");
  
print("The chosen place is ", josephus(n, k)) 
  
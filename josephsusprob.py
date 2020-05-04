def josephus(n,k):
    if (n==1):
        return 1
    return ((josephus(n - 1, k) + k) % n)
n=int(input("Enter n:"))
k=int(input("Enter k:"))
print("The winner is ", josephus(n,k))
def left(arr,d):
     d = d % len(arr)
     return arr[-d:]+arr[:-d]
arr=input()
arr=list(map(int,arr.split()))
d=int(input("Enter the position "))
result = left(arr,d)
print(result)
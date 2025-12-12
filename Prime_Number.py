n=int(input("Enter any number: "))
if n <=1:
  print("It is not prime ")
else:
  count=0
  for i in range (1,n+1):
    if n % i ==0:
      count=count+1
  if count ==2:
      print("It is  prime Number")
  else:
      print("It is Not Prime Number")
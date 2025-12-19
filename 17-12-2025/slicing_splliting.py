#slicing-substring
myString="abcdef ghijkl"
sub1=myString[0:6] #slice the first 7 elements
sub1=myString[7:]  #from the 7th element till end
sub3=myString[:5]  #first 6 element
sub3=myString[10]  #the 10th element - index from 0
sub3=myString[-5]  # last 5 elements

if "a" in myString:
  print("a is there")

word=myString.split('#')
print((word))
myString.upper()
myString.lower()
# append is used in collection and avoided in string 
print(myString+"m")
#the above string  is not same and a new string created
#String is immutable in python

#
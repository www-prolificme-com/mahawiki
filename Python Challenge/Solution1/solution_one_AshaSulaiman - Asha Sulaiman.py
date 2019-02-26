input=input("Enter a list of numbers separated by comma : ")
numbers=input.split(",")

count=0

for num in numbers:
     count= numbers.count(num)
     if count == 1 :
         print (num)

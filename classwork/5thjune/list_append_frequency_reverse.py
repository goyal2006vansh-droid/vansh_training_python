number = []
print("enter any 20 number : ")
for x in range(20):
  num = int(input())
  #append into list
  numbers.append(num)
print("----------------------------------------------------------------")
element = int(input("enter any number to remove its duplicate : "))
#----------------------------------------------------------------------
#finding the frequency of given number
frequency = numbers.count(element)
if frequency == 0:
  print("element not found")
elif frequency == 1:
  print("no duplicates found")
else:
  numbers.reverse()
  for i in range (1,frequency):
    numbers.remove(element)
  numbers.reverse()
  print("after removing duplicates")
  print(numbers)
  

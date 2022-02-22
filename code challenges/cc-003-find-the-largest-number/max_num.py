list1 = []
  
num = int(input("Enter how many numbers do you want to calculate3: "))
  
for i in range(1, num + 1):
    numbers = int(input("Enter numbers: "))
    list1.append(numbers)

def myMax(list1):
  
    max = list1[0]
   
    for x in list1:
        if x > max :
             max = x
    return max
   
print("Largest number is:", myMax(list1))
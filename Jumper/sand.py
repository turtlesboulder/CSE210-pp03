numbers = [2, 1]
target = int(input("Enter the target\n>> "))-1
for i in range(1,target):
    numbers.append(numbers[i]+numbers[i-1])
print(numbers[target])
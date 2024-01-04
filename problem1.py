#print sum of multiples of 3 and 5 below 1 to 1000
sum = 0

for i in range(1, 1000): #iterate trough numbers 1,...,1000
    if(i%3==0 or i%5==0):
        sum += i
    else:
        continue

print(sum)
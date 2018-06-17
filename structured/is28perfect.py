# Check that 28 is a perfect number by finding all the positive
#  integers smaller than 28 that divide 28 and adding them up
total = 0
for n in range(1, 28):
    if ((28 % n) == 0):
        total += n

if (total == 28):
    print("28 is perfect!")
else:
    print("Hmm either 28 isn't perfect or your program isn't")

# for loop
for number in range(1, 11):     # it will print numbers from 1 to 10
    print(number)

for number in range(1, 11, 2):  # it will print odd numbers from 1 to 10
    print(number)

for number in range(5):         # it will print numbers from 0 to 4
    print(number)


# while loop
count = 1
while count <= 10:
    print(count)
    count += 1  # increment the count by 1

# loop control statements

# break statement
for number in range(1, 11):
    if number == 5:
        break   # it will exit the loop when number is 5
    print(number)

# continue statement
for number in range(1, 11):
    if number == 5:
        continue    # it will skip the number 5 and continue the loop
    print(number)

# multiplication table generator exercise
num = int(input("Enter a number to generate its multiplication table: "))
print(f"Multiplication table for {num}:")

for i in range(1, 13):                      # it will print multiplication table from 1 to 12
    print(f"{num} x {i} = {num * i}")

# finding all prime numbers (nombor perdana) up to a given number exercise (limit = 20)
limit = int(input("Find all prime numbers up to: "))
print(f"Prime numbers up to {limit} are:")
for num in range(2, limit + 1):
    is_prime = True                                 # assume the number is prime
    for i in range(2, num):                         # check divisibility from 2 to num-1
        if num % i == 0:                            # if num is divisible by i, then it's not prime
            is_prime = False                        # set is_prime to False
            break                                   # exit the inner loop if not prime
    if is_prime:                                    # if is_prime is still True, then it's prime   
        print(num)                                  # print each prime number from user input

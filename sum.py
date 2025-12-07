while True:
    try:
        n = int(input("Enter a number:"))
        if n <=0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input.")


total = 0

for i in range(1,n+1):
    total += i

print("The sum is:", total)


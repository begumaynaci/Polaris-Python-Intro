import time

while True:

    try :
        count = int(input ("Enter a positive integer to start countdown: "))

        if(count <= 0):
            print("Please enter a positive integer.")
            
        else :
            break

    except ValueError:
        print("Invalid input.")


while count > 0:

    print(count)
    count -= 1
    time.sleep(.5)
    
print("Boom!")

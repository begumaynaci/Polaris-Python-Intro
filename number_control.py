while True:
    try:
        num =int(input("Enter a integer:"))
        break
    except ValueError:
        print("Please enter a valid integer.")
    

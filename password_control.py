import re 

def control_pass(password):

    if re.search(r"[0-9]", password) is None:
        return False
    if re.search(r"[A-Z]", password) is None:
        return False
    if re.search(r"[a-z]", password) is None:
        return False
    if re.search(r"[^A-Za-z0-9]", password) is None:
        return False
    
    return True

if __name__ == "__main__":

    entered_pass = input("Enter a password:")

    if control_pass(entered_pass):
            print("Strong password!")
    else:
            print("Weak password!")
class Assistant:
    def __init__(self, name):
        self.name = name 
        self.action_count = 0

    def greet(self, user_name):

        print(f"Hello {user_name}, I am {self.name}. How can I help you?")
        self.action_count += 1

    def math_operation(self, operation, num1, num2):

        match operation:
            case "+": 
                print(f"The result is: {num1 + num2}") 
            case "-": 
                print(f"The result is: {num1 - num2}") 
            case "*": 
                print(f"The result is: {num1 * num2}") 
            case "/": 
                print(f"The result is: {num1 / num2}")
            case _:  
                print("Error! Invalid operation.")
                return
        self.action_count += 1

    def status_report(self):
        print(f"I performed a total of {self.action_count} operations so far.")


my_ai = Assistant("Bego")
my_ai.greet("Begüm")
my_ai.math_operation("/", 40, 6)
my_ai.greet("Begüm")
my_ai.math_operation("-", -5, 6)
my_ai.math_operation("&", -5, 6)

my_ai.status_report()
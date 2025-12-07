import datetime

while True:
    try:
        exam_time_string = input("Enter the exam time (DD-MM-YYYY HH:MM): ")
        exam_time = datetime.datetime.strptime(exam_time_string, "%d-%m-%Y %H:%M")
        break
    except ValueError:
        print("Invalid format. Please enter the date and time in 'DD-MM-YYYY HH:MM' format.")

current_time = datetime.datetime.now()

if exam_time < current_time:
    print("The exam time has already passed.")

else:
    time_dif = exam_time - current_time
    
    hours = time_dif.seconds // 3600
    minutes = (time_dif.seconds % 3600) // 60
    
    print(f"Time remaining until the exam: {time_dif.days} days, {hours} hours, {minutes} minutes.")


import re 


with open("lvl1_bozuk_veri.txt", "r") as file:
    text = file.read()



email = re.findall(r"[a-zA-Z0-9._\+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" , text)
phone_number = re.findall(r"(?<!\d)[\d\+]{1,4}[\s-]*\(?[\d]{3}\)?[\s-]*[\d]{3}[\s-]*[\d]{2}[\s-]*[\d]{2}(?!\d)", text)



with open("lvl1_temiz_rehber.txt" , "w") as file:

    file.write("Found mails:\n")

    for mail in email:
        file.write(f"{mail}\n")

    file.write("\nFound phone numbers:\n")

    for number in phone_number:
        file.write(f"{number}\n")


with open("lvl2_bozuk_veri.txt", "r") as file:
    text = file.read()



email = re.findall(r"[a-zA-Z0-9._\+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" , text)
phone_number = re.findall(r"(?<!\d)[\d\+]{1,4}[\s-]*\(?[\d]{3}\)?[\s-]*[\d]{3}[\s-]*[\d]{2}[\s-]*[\d]{2}(?!\d)", text)

with open("lvl2_temiz_rehber.txt" , "w") as file:

    file.write("Found mails:\n")

    for mail in email:
        file.write(f"{mail}\n")

    file.write("\nFound phone numbers:\n")

    for number in phone_number:
        file.write(f"{number}\n")
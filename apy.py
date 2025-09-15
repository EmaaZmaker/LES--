import random
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
all_characters = lowercase + uppercase + numbers
password = ""
for i in range(8):
    password += random.choice(all_characters)
print("Your password is:", password)

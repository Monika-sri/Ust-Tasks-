email = "ilearniexcel@gmail.com"

# Find the position of "@"
print("the position of @ is :",email.find("@"))

# Extract only '.com' from the email string
print("printing the last four characters of email :",email[-4:])

# Extract only 'gmail' from the email
print("Extarct only gmail from the mail :",email[13:18])

# Split the string based on the separator "@" and "."
split_email = email.replace("@", ".").split(".")
print("Split the string based on '@' and '.':", split_email)



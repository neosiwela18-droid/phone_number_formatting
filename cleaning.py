# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."



#Input your phone number ensure its 10 digits long
phone = str(input("Enter a phone number: ")).strip()

# Cleaning process of the input value
for char in [",", ".", "-", "(", ")"]:

    replace = phone.replace(char, " ")
    joint = (("".join(replace.split())))
    lenght = (len(joint))

#If phon is less than 10 digits is invalid else it will format it like this: (123) 456-7890
if lenght != 10:
        print("Please enter exactly 10 digits.")
        phone = str(input("Enter a phone number: ")).strip()
elif lenght == 10:
     print(f"({joint[0:3]}) {joint[3:6]}-{joint[6:10]}")

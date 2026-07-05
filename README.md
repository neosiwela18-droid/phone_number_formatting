# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."
#task by scrimba

phone = input("Enter a phone number: ")
cleaned = phone.strip()

for char in [",", ".", "-", "(", ")"]:
    cleaned = cleaned.replace(char, " ")
    
    joint = (cleaned.split())
    value = "".join(joint)

if len(value) == 10:
      print(f"({value[0:3]}) {value[3:6]}-{value[6:10]}")
elif len(value) != 10:
      print("Please enter exactly 10 digits.")

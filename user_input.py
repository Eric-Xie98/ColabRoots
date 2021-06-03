## https://gitlab.oit.duke.edu/colab/colab_summer_software_2021/-/blob/master/practice/USER_INPUT.md

nums = []

while True:

    user_num = input("Please enter a number: ")
    if(user_num == ""):
        break

    try:
        val = float(user_num)
    except ValueError:
        print("That's not a number!")
        continue

    nums.append(user_num)

total = 0
count = len(nums)

for num in nums:
    total += float(num)

try:
    average = total / count
except ZeroDivisionError:
    print("You can't divide a number by zero!")

print(f"The total amount inputted by the user is {total}" )
print(f"The average number is {average}")



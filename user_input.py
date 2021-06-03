## https://gitlab.oit.duke.edu/colab/colab_summer_software_2021/-/blob/master/practice/USER_INPUT.md

nums = []

isString = False
isError = False

first = 0

while True:

    user_num = input("Please enter a number or a string: ")
    if(user_num == ""):
        break

    if(isString):
        try:
            val = float(user_num)
            print("You tried to input a number into a string list")
            isError = True
            break
        except ValueError:
            nums.append(user_num)
    else:
        try:
            val = float(user_num)
            nums.append(val)
        except ValueError:
            if(first == 0):
                isString = True
                nums.append(user_num)
            else:
                print("You tried to enter a string into a number list")
                isError = True
                break
    
    first += 1



total = 0
count = len(nums)

if isError:
    pass

elif not isString:
    for num in nums:
        total += float(num)

    try:
        average = total / count
    except ZeroDivisionError:
        print("You can't divide a number by zero!")

    print(f"The total amount inputted by the user is {total}" )
    print(f"The average number is {average}")

else:
    concat = ""
    for word in nums:
        concat += word

    print(concat)


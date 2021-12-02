i = 0
while i < 1001:
    if i < 1000:
        action = str(input()).capitalize()  # Enter Tour action here Y or R.
        if action == 'Y':
            print(i + 1)
            i += 1
        elif action == 'R':
            i = 0
            print(i)
        else:
            # if your choise not Y or R. there is somthing wrong here.
            print("Wrong Action. ")
            break
    elif i >= 1000:
        i = 0
        print(i)

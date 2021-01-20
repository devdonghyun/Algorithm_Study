def changeOrder(str1, str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    str1 = "".join(sorted_str1)
    str2 = "".join(sorted_str2)

    if str1 == str2:
        print("Yes")
    else:
        print("No")


str1 = input()
str2 = input()
changeOrder(str1, str2)

def minCalc():
    accPlus, numbers = [], []
    str = ""
    for c in data:
        if c == "+":
            num = int(str)
            accPlus.append(num)
            str = ""

        elif c == "-":
            num = int(str)
            accPlus.append(num)
            numbers.append(sum(accPlus))
            str = ""
            accPlus = []

        else:
            str += c
    num = int(str)
    if len(accPlus) != 0:
        accPlus.append(num)
        numbers.append(sum(accPlus))
    else:
        numbers.append(num)

    result = numbers[0]
    for num in numbers[1:]:
        result -= num

    return result


data = input()
print(minCalc())

def runLength(s):
    result = ""
    i = 0
    while i <= len(s)-1:
        count = 1
        j = i
        while j < len(s)-1:
            if s[j] == s[j+1]:
                count += 1
                j += 1
            else:
                break
        result += (s[j] + str(count))
        i = j+1

    print(len(result))
    print(result)


s = input()
runLength(s)

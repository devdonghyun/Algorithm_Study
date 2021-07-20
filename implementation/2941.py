word = input()
alpha_list = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
i, count = 0, 0
while True:
    if i >= len(word):
        break

    count += 1

    if i == len(word)-1:
        break

    if word[i:i+2] in alpha_list:
        i += 2

    elif word[i:i+3] == 'dz=':
        i += 3

    else:
        i += 1

print(count)

# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem


n = int(input().strip())

dict_name = {}
for i in range(n):
    strs = str(input()).split(" ")
    name = strs[0]
    number = int(strs[1])
    dict_name[name] = number

for i in range(n):
    name = str(input())

    if name in dict_name:
        print(name + "=" + str(dict_name[name]))
    else:
        print('Not found')
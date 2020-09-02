word = "banana"
obj = {}
discard = {}
count = 0


# for i in range(len(word)):
#     print(i)
#     # print(word[i])
#     # if word[i] not in obj:
#     #     obj[i] = word[i]
#     # else:
#     #     discard[i] = word[i]
#     #     # print("not true")
#     # print('its already in there')

# print(obj)


for i in word:
    count += 1

    if i in obj:
        print("first repeating char is", i)
        break
    obj[i] = count

print(obj)


countme = dict()
for i in word:
    print("count", i)
    countme[i] = countme.get(i, 0)+1

print(countme)

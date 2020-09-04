array = [9, 7, 13, 22, 9, 8, 22]

cont = []
repeat = []
pos = 0
for i in range(len(array)):
    if array[i] in cont:
        repeat.append(array[i])
        pos = i
    cont.append(array[i])

    print(cont[i])

print("cont", cont)
print(f"this is repeated {repeat}")
print(f"the first repeating element is {repeat[0]} at {pos} ")


pair = {}
containing = {}


for i in range(len(array)):
    if array[i] in pair.values():
        containing[i] = array[i]
    pair[i] = array[i]


print("pair->", pair)
print("containing", containing)
for i in containing:
    print(f"repeating numbers are {containing[i]} in position {i}")

#!/usr/bin/python3

bobo = ['donna douglas', 'patty duke', 'mary tyler moore', 'jennifer o\'neill', 'evelyn arden', 'frances bavier', 'doris day']
lengths = []
for i in bobo:
    lengths.append(len(i))
width = max(lengths) + 4

for i in bobo:
    print((width * "-") + "\n| " + i + ((width-len(i)-4) * " ") + " |")

print(width * "-")

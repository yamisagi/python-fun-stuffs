import random as rd
loop_time = 0
tru = True
while tru:

    love = []
    for i in range(1000):
        shuffle_love = ['e', 'n', 'e', 'v', 'r', 'o', 'l']
        rd.shuffle(shuffle_love)
        love.append(shuffle_love)

    tru_love = ["l", "o", "v", "e", "r", "e", "n"]

    for eren in love:
        if eren == tru_love:
            tru = False
            print(eren)
            break
    loop_time += 1

print(f"List has {love.count(tru_love)} True love in.")
print(f"Aaaand looped {loop_time} times *so in {loop_time*len(love)}")

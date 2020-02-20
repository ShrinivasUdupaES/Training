import random

w = ['EAGLESTONE', 'ADDICTION', 'SUBTRACTION']
ch = random.choice(w)
wd = []
pos = []
c = 0

while c < 6:
    a = random.randrange(len(ch))

    if ch[a] not in wd:
        c = c + 1
        pos.append(a)
        wd.append(ch[a])

d = dict(zip(wd, pos))
nwd = []
nwd2 = ''

for j in ch:
    nwd.append(j)

for k in pos:
    nwd.pop(k)
    nwd.insert(k, '_')

nwd2 = nwd2.join(nwd)
print(nwd2)

flag = 0

for h in range(6):
    nwd1 = ''
    n = str(input('Enter your guess: '))

    if n == ch:
        flag = 1
        print('Congrats!!!')
        break

    elif n in wd:
        nwd.pop(d[n])
        nwd.insert(d[n], n)
        nwd1 = nwd1.join(nwd)
        print(nwd1)

        if nwd1 == ch:
            flag = 1
            print('Congrats!!!')

if flag == 0:
    print('Sorry you have run out of chances :( :( :(')
print('Your points:', (6 - h) * 5)



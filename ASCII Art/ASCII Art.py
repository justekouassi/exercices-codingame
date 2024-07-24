art = open("art1.txt", "r")

l = int(input())
h = int(input())
t = input().upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
T = ""
for i in range(h):
    # row = input()
    row = art.readline()
    for j in t:
        if j not in alphabet:
            tmp = row[104:107]
            T += tmp+" "
        else:
            tmp = row[(ord(j)-65)*l:(ord(j)-65)*l+l]
            T += tmp
    T += "\n"

print(T)

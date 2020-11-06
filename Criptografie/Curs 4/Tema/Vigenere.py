# s = "zpgdlrjlajkpylxzpyyglrjgdlrzhzqyjzqrepvmswrzyrigzhzvregkwivssaoltnliuwoldieaqewfiiykhbjowrhdogcqhkwajyaggemisrzqoqhoavlkbjofrylvpsrtgiuavmswlzgmsevwpcdmjsvjqbrnklpcfiowhvkxjbjpmfkrqthtkozrgqihbmqsbivdardymqmpbunivxmtzwqvgefjhucborvwpcdxuwftqmoowjipdsuqmoeavljgqealrktiwvextvkrrgxanidlr"

s = "togmggbymkkcqivdmlxkkbyifvcuekcuuisvvxqspwwejkoqggphumtwhlsfyovwwknhhmrcqfqvvhkwpsuedugrsfctwijkhvfathkeffwptjggvivcgdrapgwvmosqxghkdvtwhuevkcwyjpsgsngfwsljsfseooqhwtofshaciingfbifgabgjadwsytopmlecqzwasgvsfwrqsfsfvqrhdrsnmvmkcbhrvkblxkgzi"
print(len(s))
counter = 0
salvate = []
cheie = 5
for i in range(0, (len(s) - cheie - 1)):
    curent = s[i: i + cheie]
    if (curent not in salvate):
        counter += 1
        gasit = False
        counterInterior = counter + cheie - 1
        memoCounter = []
        for j in range(i+cheie, len(s) - cheie):
            curentInterior = s[j: j + cheie]
            counterInterior += 1
            if (curent == curentInterior):
                gasit = True
                memoCounter.append(counterInterior)
        if gasit:
            salvate.append(curent)
            poz = counter
            for i in range(len(memoCounter)):
                #print (curent + " " + str(memoCounter[i]))
                print(curent + ": " + str(poz) + ", " + str(memoCounter[i])  + " distanta = " + str(memoCounter[i] - poz))
                poz = memoCounter[i]

            #print(curent + ": " + str(counter) + ", " + str(memoCounter)  + " distanta = " + str(memoCounter - counter))



# splited = []
# for i in range (0, len(s) - 2):
#     #curent = s[i: i + 3]
#     splited.append(s[i: i + 3])
#     #print(curent)
# print (splited)

# for str1 in splited:
#     counter = 0
#     memo = 0
#     for str2 in splited:
#         if str1 == str2:
#             memo = counter
#         counter += 1
#     print(str1 + ": " + str(memo))

    







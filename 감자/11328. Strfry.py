number = int(input())

tc = []
# dict -> count 
for i in range(number):
   tc.append(input().split()) 

for row in range(number):
    alpha = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,
            'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'w':0,'x':0,'y':0,'z':0}
    beta = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,
            'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'w':0,'x':0,'y':0,'z':0}
    first = tc[row][0]
    second = tc[row][1]
    for i in range(len(first)):
        if first[i] in alpha:
            alpha[str(first[i])] +=1
    for i in range(len(second)):
        if second[i] in beta:
            beta[str(second[i])]+=1
    if alpha == beta:
        print("Possible")
    else:
        print("Impossible")

print(''' The Grid is: 
      11 12 13
      21 22 23
      31 32 33
Only give input from this!!
      ''')
a,b =[],[]
ap,bp = 0, 0
i=0
while i<6:
    if i%2==0:
        x=input("Enter the position of player A: ")
        a.append(x)
    else:
        x=input("Enter the position of player B: ")
        b.append(x)
    if x[0] in ['1','2','3'] and x[1] in ['1','2','3']:
        if i>1:
            if i == 3:
                k = [b[0][0],b[1][0]]
                ks =  [b[0][1],b[1][1]]
                if len(k) == 2*k[0]:
                    if (ks[0] == '1') and (ks[1] == '3') or (ks[0] == '3') and (ks[1] == '1'):
                        print("Incorrect move")
                        pass
                    else:
                        if ks == sorted(ks):
                            i+=1
                elif k == sorted(k):
                    if (k[0] == '1') and (k[1] == '3') or (k[0] == '3') and (k[1] == '1'):
                        print("Incorrect move")
                        pass
                    else:
                        i += 1
            elif i == 2:
                l = [a[0][0],a[1][0]]
                ls = [a[0][1],a[1][1]]
                if len(l) == 2*l[0]:
                    if (ls[0] == '1') and (ls[1] == '3') or (ls[0] == '3') and (ls[1] == '1'):
                        print("Incorrect move")
                        pass
                    else:
                        if ls == sorted(ls):
                            i+=1
                elif l == sorted(l):
                    if (l[0] == '1') and (l[1] == '3') or (l[0] == '3') and (l[1] == '1'):
                        print("Incorrect move")
                        pass
                    else:
                        i += 1
            elif i == 5:
                k = [b[0][0],b[1][0],b[2][0]]
                ks =  [b[0][1],b[1][1],b[2][0]]
                if len(k) == 2*k[0]:
                    if ks == sorted(ks):
                        i+=1
                elif k == sorted(k):
                    i += 1
            elif i == 4:
                l = [a[0][0],a[1][0],a[2][0]]
                ls = [a[0][1],a[1][1],a[2][0]]
                if len(l) == 2*l[0]: 
                    if ls == sorted(ls):
                        i+=1
                elif l == sorted(l):
                    i += 1
        else:
            i+=1
    else:
        print('incorrect')
print('\n\n\n')
for i in range(3):
    if a[i] == b[i-1]:
        ap += 1
    elif b[i] == a[i-1]:
        bp += 1

if ap > bp:
    print(f"A wins with {ap} points!")
elif ap < bp:
    print(f"B wins with {bp} points!")
else:
    print(f"A and B draw themselves with {ap} points!")

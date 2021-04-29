tab1 =[]
tab2 =[]

for i in range(0,101):
    tab1.append(i)

for k in range(0,101):
    tab2.append(k)

for c in range(0,101):
    tab2[c]= tab2[c]+tab1[c]

print(tab2)

def moyenne(l):
    for i in range (0,x):
        y=int(input(f'Donner element n° {i} :'))
        l.append(y)
    print(l)
    moy= sum(l[:])/x
    print('La moyenne de ces valeurs est egales a :',moy)
while True:
        x=int(input('Donner la taille de la liste'))
        if(x>0):
            break;
l=[]

print(moyenne(l))



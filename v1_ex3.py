while True:
    taille_tuple=int(input('Donner la taille de tuple'))
    if(taille_tuple>0):
        break;

Tupl1 = ()
l= list(Tupl1)

for i in range (0,taille_tuple):
    x = int(input(f'Donner element {i}:'))
    l.append(x)

mon_tuple=tuple(l)
print("Tuple 1 =",mon_tuple)
n =int(input('Donner un entier n :'))

tupl2=()
l2 =list(tupl2 )
for i in range(0,taille_tuple):
    x=l[i]*n
    l2.append(x)
mon_tuple2 = tuple(l2)
print("Tuple 2 ",mon_tuple2)
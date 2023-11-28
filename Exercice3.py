while True:
    taille_tuple=int(input('Donner la taille de tuple'))
    if(taille_tuple>0):
        break;

nombre = ()
l= list(nombre)

for i in range (0,taille_tuple):
    x = int(input(f'Donner element {i}:'))
    l.append(x)
nombre = tuple(l)
print("Tuple 1 :",nombre)

n=int(input('Donner un entier naturel'))

nouveau_nombre = tuple(x*n for x in nombre)
print("Tuple 2 :",nouveau_nombre)
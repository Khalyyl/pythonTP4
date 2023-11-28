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
print("Tuple saisi est",nombre)
nombre_pairs = tuple( x for x in nombre if x%2== 0)
nombre_impairs = tuple( x for x in nombre if x%2 != 0)
print("Tuple des nombres pairs",nombre_pairs)
print("Tuple des nombres impaires",nombre_impairs)




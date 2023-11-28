tuple1= (1,2,3,4,5,8)
element = int(input('Donner element :'))

if element in tuple1:
    pos = tuple1.index(element)
    print(f"La position de {element} dans {tuple1} est {pos}")
else:
    print(f'{element} nest pas dans {tuple1}')


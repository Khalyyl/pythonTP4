d = {'prenom': 'khalil', 'Nom': 'Askri', 'Age': 22}
d1 = {v: k for k, v in d.items()}
print("Dictionnaire initial :", d)
print("Dictionnaire échangé :", d1)
for k,v in d.items():
    print ("Dans la clé",k," il y a la valeur ",v)



def compare(x,y):
    if(x < y):
        print("Primul numar este mai mare decat al doilea")
    else:
        print("Al doilea numar este mai mare")

compare(5,2)
compare(10,1)
compare(1,9)

clr = ""

def list_items(x):
    for i in x:
        print(i)

print(clr)
orase1 = ("Bucuresti", "Brasov", "Piteste")
list_items(orase1)
print(clr)

orase2 = ("Iasi", "Craiova", "Oradea", "Ploiesti")
list_items(orase2)
print(clr)

orase3 = ("Constanta", "Botosani", "Cluj", "Timisoara", "Sibiu", "Galat")
list_items(orase3)


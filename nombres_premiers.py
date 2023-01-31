# Ce programme trouvera les nombres premiers dans une fourchette donnée

nombre_premier = int(input("Écrit un nombre premier: "))

def ep(n):
    count=0
    if n <= 1:
      print(f"{n} n'est pas un nombre premier")
    for k in range(2, n):
      if n%k == 0:
        count+=1
        break
    if count==0:
      print(f"{n} est un nombre premier")

      
ep(nombre_premier)

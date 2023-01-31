# SNT-ALGO

Exercices des Cours d'ALGO

Verification de nombres premiers:

...
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
...

Chercheur de nombre palindrome à partir d'un nombre de votre choix: 

...
# Ce programme nous montrera un nombre palindrome
n = int(input("Donne moi un nombre: "))

def change(n):
  nb = str(n)
  ch = nb[::-1]
  return int(ch)

def palind(n):
  if change(n)==n:
    return 1
  else:
    return 0

def nbetape(n):
  compt=0
  while palind(n) == 0:
    n = n+change(n)
    compt+=1
  print(f"La recherche d'un nombre palindrome à partir de {n} à pris {compt} étapes")
  return n
  

nbetape(n)
...

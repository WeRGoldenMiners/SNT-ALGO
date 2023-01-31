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

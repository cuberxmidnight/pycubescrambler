import random

def get3():
  def scramble3():
    moves = ["F","B","R","L","U","D"]
    turns = [" ","2 ","' ","2 "]
    scramble = []
    usedmoves=[]
    usedmoves1=[]
    for i in range(20):

      if i % 2 ==0:
        randmoves=random.choice(moves)
        if i>1:                      
          while randmoves=="F" and scramble[-4]=="F" and scramble[-2]=="B":
            randmoves=random.choice(moves)
          while randmoves=="B" and scramble[-4]=="B" and scramble[-2]=="F":
            randmoves=random.choice(moves)
          while randmoves=="R" and scramble[-4]=="R" and scramble[-2]=="L":
            randmoves=random.choice(moves)
          while randmoves=="L" and scramble[-4]=="L" and scramble[-2]=="R":
            randmoves=random.choice(moves)
          while randmoves=="U" and scramble[-4]=="U" and scramble[-2]=="D":
            randmoves=random.choice(moves)
          while randmoves=="D" and scramble[-4]=="D" and scramble[-2]=="U":
            randmoves=random.choice(moves)     
        usedmoves.append(randmoves)
        scramble.append(randmoves)
        if i<=4:
          ok=random.randint(1,3)
          if ok!=1:
            scramble.append("2 ")
          else:
            scramble.append(random.choice(turns))

        else:
          scramble.append(random.choice(turns))
        moves.remove(randmoves)
        if i != 0:
          moves.append(usedmoves1[-1])

      else:

        randmoves1=random.choice(moves)
        if i>1:
          while randmoves1=="F" and scramble[-4]=="F" and scramble[-2]=="B":
            randmoves1=random.choice(moves)
          while randmoves=="B" and scramble[-4]=="B" and scramble[-2]=="F":
            randmoves1=random.choice(moves)
          while randmoves1=="R" and scramble[-4]=="R" and scramble[-2]=="L":
            randmoves1=random.choice(moves)
          while randmoves1=="L" and scramble[-4]=="L" and scramble[-2]=="R":
            randmoves1=random.choice(moves)
          while randmoves1=="U" and scramble[-4]=="U" and scramble[-2]=="D":
            randmoves1=random.choice(moves)
          while randmoves1=="D" and scramble[-4]=="D" and scramble[-2]=="U":
            randmoves1=random.choice(moves) 
        scramble.append(randmoves1)
        usedmoves1.append(randmoves1)
        scramble.append(random.choice(turns))
        moves.remove(randmoves1)
        moves.append(usedmoves[-1])
    return "".join(scramble)

  scramble=[]
  scramble3=scramble3()
  scramble.append(scramble3)
  possi=["","Rw ","Rw' ","Rw2 ","Fw ","Fw2 ","Fw' "]
  possi2=["Uw","Uw'","Uw2",""]
  scramble.append(random.choice(possi))
  scramble.append(random.choice(possi2))
  

  return "".join(scramble)



def get4():
  scramble=nxn.get4()
  return scramble



def get5():
  scramble=nxn.get5()
  return scramble

from getpass import getpass as input
print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()
player1 = input("Player 1 > ")
print()
player2 = input("Player 2 > ")
print()
if player1 == "R":
  if player2 == "R" :
    print("You both picked Rock, draw!")
  elif player2 == "S" :
    print("Player1 smashed Player2's Scissors into dust with their Rock!")
  elif player2 == "P" :
    print("Player1's Rock is smothered by Player2's Paper!")
  else:
    print("Invalid Move Player 2!")
  

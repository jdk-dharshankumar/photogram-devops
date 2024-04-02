import random
lst=['r','p','s']
chance=4
no_of_chance=0
computer_pnt=0
humn_pnt=0
tie=0
charater_error=0
name=input("enter your name : ")
print("\n\t\tWELCOME TO ROCK,PAPER,SECIOR GAME")
print("\nRules for this game\n")
print("r of stone \np for paper \ns for secior\n")
print("\t\t\t four round's Only\n")
while no_of_chance < chance:
	userinput=input("stone,paper,secior : ")
	computer=random.choice(lst)
	
	if userinput == computer:
		tie=tie+1
		print(f"\nபோச்சு 0 points match tie your choice {userinput} computer choice {computer}")
		
	elif userinput == 'r' and computer == 'p':
		computer_pnt=computer_pnt+1
		print(f"\nyour chose {userinput} computer chose {computer}")
		print("computer win 1 point")
		print(f"your point {humn_pnt} computer point {computer_pnt}")
		
	elif userinput == 'p' and computer == 'r':
		humn_pnt=humn_pnt+1
		print(f"\nyour chose {userinput} computer chose {computer}")
		print("you win 1 point")
		print(f"your point {humn_pnt} computer point {computer_pnt}")
		
	elif userinput == 'p' and computer == 's':
		computer_pnt=computer_pnt+1
		print(f"\nyour chose {userinput} computer chose {computer}")
		print("computer win 1 point")
		print(f"your point {humn_pnt} computer point {computer_pnt}")
		
	elif userinput == 's' and computer == 'p':
		humn_pnt=humn_pnt+1
		print(f"\nyour chose {userinput} computer chose {computer}")
		print("you win 1 point")
		print(f"your point {humn_pnt} computer point {computer_pnt}")
		
	elif userinput == 's' and computer == 'r':
		computer_pnt=computer_pnt+1
		print(f"\nyour chose {userinput} computer chose {computer}")
		print("computer win 1 point")
		print(f"your point {humn_pnt} computer point {computer_pnt}")
		
	elif userinput == 'r' and computer == 's':
		humn_pnt=humn_pnt+1
		print(f"\nyour chose {userinput} computer chose {computer}")
		print("you win 1 point")
		print(f"your point {humn_pnt} computer point {computer_pnt}")
		
	else:
		charater_error=charater_error+1
		print("your type is rong pls try r,p,s")
		
	no_of_chance=no_of_chance+1
	print(f"{chance - no_of_chance} left out of {chance}\n")
print("\t\t\tgame over\n")

if humn_pnt==computer_pnt:
	print("\t\t\tmatch draw\n")
elif computer_pnt>humn_pnt:
	print("\t\tcomputer win you losssss\n")
else:
	print(f"\t\t\t{name} you win\n")
	
print(f"tie match's {tie}\nCharater Error's {charater_error}\n{name} total point of you {humn_pnt}\ntotal computer point {computer_pnt}")

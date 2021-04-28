from os import system
import random
square=['0','1','2','3','4','5','6','7','8','9']

def board():
	system('cls')
	print("\n\t\t    TIC TAC TOE\n\n")
	print("\t\t      |     |     ")
	print("\t\t   "+square[1]+"  |  "+square[2]+"  |  "+square[3])
	print("\t\t _____|_____|_____")
	print("\t\t      |     |     ")
	print("\t\t   "+square[4]+"  |  "+square[5]+"  |  "+square[6])
	print("\t\t _____|_____|_____")
	print("\t\t      |     |     ")
	print("\t\t   "+square[7]+"  |  "+square[8]+"  |  "+square[9])
	print("\t\t      |     |     \n")

def checkwin():
	if(square[1] == square[2] and square[2] == square[3]):
		if(square[1] == 'X'):
			return 1
		else:
			return 0
	elif (square[4] == square[5] and square[5] == square[6]):
		if(square[4] == 'X'):
			return 1
		else:
			return 0
	elif (square[7] == square[8] and square[8] == square[9]):
		if(square[7] == 'X'):
			return 1
		else:
			return 0
	elif (square[1] == square[4] and square[4] == square[7]):
		if(square[1] == 'X'):
			return 1
		else:
			return 0
	elif (square[2] == square[5] and square[5] == square[8]):
		if(square[2] == 'X'):
			return 1
		else:
			return 0
	elif (square[3] == square[6] and square[6] == square[9]):
		if(square[3] == 'X'):
			return 1
		else:
			return 0
	elif (square[1] == square[5] and square[5] == square[9]):
		if(square[1] == 'X'):
			return 1
		else:
			return 0
	elif (square[3] == square[5] and square[5] == square[7]):
		if(square[7] == 'X'):
			return 1
		else:
			return 0
	elif (square[1] != '1' and square[2] != '2' and square[3] != '3' and square[4] != '4' and square[5] != '5' and square[6] != '6' and square[7]!= '7' and square[8] != '8' and square[9] != '9'):
		return 2
	else:
		return (-1)

def compmark():
	if (square[1] == '1' or square[2] == '2' or square[3] == '3' or square[4] == '4' or square[5] == '5' or square[6] == '6' or square[7]== '7' or square[8] == '8' or square[9] == '9'):
		if square[1]=='O' and square[2]=='O':
			if square[3]=='3':
				square[3] = 'O'
		elif square[4]=='O' and square[5]=='O':
			if square[6]=='6':
				square[6] = 'O'
		elif square[7]=='O' and square[8]=='O':
			if square[9]=='9':
				square[9] = 'O'
		elif square[1]=='O' and square[4]=='O':
			if square[7]=='7':
				square[7] = 'O'
		elif square[2]=='O' and square[5]=='O':
			if square[8]=='7':
				square[8] = 'O'
		elif square[3]=='O' and square[6]=='O':
			if square[9]=='9':
				square[9] = 'O'
		elif square[1]=='O' and square[5]=='O':
			if square[9]=='9':
				square[9] = 'O'
		elif square[3]=='O' and square[5]=='O':
			if square[7]=='7':
				square[7] = 'O'
		elif square[3]=='O' and square[2]=='O':
			if square[1]=='1':
				square[1] = 'O'
		elif square[6]=='O' and square[5]=='O':
			if square[4]=='4':
				square[4] = 'O'
		elif square[9]=='O' and square[8]=='O':
			if square[7]=='7':
				square[7] = 'O'
		elif square[7]=='O' and square[4]=='O':
			if square[1]=='1':
				square[1] = 'O'
		elif square[8]=='O' and square[5]=='O':
			if square[2]=='2':
				square[2] = 'O'
		elif square[9]=='O' and square[6]=='O':
			if square[3]=='3':
				square[3] = 'O'
		elif square[9]=='O' and square[5]=='O':
			if square[1]=='1':
				square[1] = 'O'
		elif square[7]=='O' and square[5]=='O':
			if square[3]=='3':
				square[3] = 'O'
		if square[1]=='O' and square[3]=='O':
			if square[2]=='2':
				square[2] = 'O'
		elif square[4]=='O' and square[6]=='O':
			if square[5]=='5':
				square[5] = 'O'
		elif square[7]=='O' and square[9]=='O':
			if square[8]=='8':
				square[8] = 'O'
		elif square[1]=='O' and square[7]=='O':
			if square[4]=='4':
				square[4] = 'O'
		elif square[2]=='O' and square[8]=='O':
			if square[5]=='5':
				square[5] = 'O'
		elif square[3]=='O' and square[9]=='O':
			if square[6]=='6':
				square[6] = 'O'
		elif square[1]=='O' and square[9]=='O':
			if square[5]=='5':
				square[5] = 'O'
		elif square[3]=='O' and square[7]=='O':
			if square[5]=='7':
				square[5] = 'O'
		else :
			choice=random.randint(1,9)
			if(choice == 1 and square[1] == '1'):
				square[1] = 'O'
			elif(choice == 2 and square[2] == '2'):
				square[2] = 'O'
			elif(choice == 3 and square[3] == '3'):
				square[3] = 'O'
			elif(choice == 4 and square[4] == '4'):
				square[4] = 'O'
			elif(choice == 5 and square[5] == '5'):
				square[5] = 'O'
			elif(choice == 6 and square[6] == '6'):
				square[6] = 'O'
			elif(choice == 7 and square[7] == '7'):
				square[7] = 'O'
			elif(choice == 8 and square[8] == '8'):
				square[8] = 'O'
			elif(choice == 9 and square[9] == '9'):
				square[9] = 'O'
			else :
				compmark()
  	
def game():
	counter=0
	j=1
	i=-1
	choice=0
	while(choice>=0 and choice<=9 and i==-1):
		counter=counter+1
		board()
		print("\nPlayer, Enter Your Number : ",end="")
		choice=int(input())
		if(choice == 1 and square[1] == '1'):
			square[1] = 'X'
		elif(choice == 2 and square[2] == '2'):
			square[2] = 'X'
		elif(choice == 3 and square[3] == '3'):
			square[3] = 'X'
		elif(choice == 4 and square[4] == '4'):
			square[4] = 'X'
		elif(choice == 5 and square[5] == '5'):
			square[5] = 'X'
		elif(choice == 6 and square[6] == '6'):
			square[6] = 'X'
		elif(choice == 7 and square[7] == '7'):
			square[7] = 'X'
		elif(choice == 8 and square[8] == '8'):
			square[8] = 'X'
		elif(choice == 9 and square[9] == '9'):
			square[9] = 'X'
		else :
			print("\n\n\t\tInvalid Move")
			input()
			j=0
		if j!=0:
			compmark()
		i=checkwin()
		if i==2:
			break
		j=j+1
	system('cls')
	board()
	if (i == 1):
		print(" ==> \aYou Win")
	elif (i==0):
		print(" ==> \aComputer Win")
	else:
		print(" ==> \aGame draw")
		
#----main()----			
game()


#------MADE BY : CODING PLEX(https://coding-plex.blogspot.com)

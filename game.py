import random
import time 

def gamesIntro():

    print('Welcome to the misty mountains')
    print('Before you lies unchartered territory!!')
    time.sleep(2)
    print('The path forks and two caves lie before you...')
    print('Choose your direction wisely...')
    time.sleep(3)

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print('Please choose which cave to enter.... 1 or 2')
		cave = input()

	return cave 

def checkcheck(cavechoice):
	print('You walk towards the eery entrance....')
	time.sleep(2)
	print('Upon entering the cave a huge hunk of bones rises from the ground')
	time.sleep(4)
	print('A large skeleton jumps at you and lifts its sword into the air...')
	time.sleep(4)

	friendlycave = random.randint(1, 2)

	if cavechoice == str(friendlycave):
		print('It reaches out with his other hand and gives you a tattered map and lets out a deafening shriek')
		time.sleep(2)
		print('The skeleton crumbles and shrinks to the floor')
		print()
		time.sleep(3)
	else:
		print('He swings his sword and kills you in one blow')
		print()
		time.sleep(2)
		print('YOU ARE DEAD')
		print()
		time.sleep(3)
		Again()

def destinationDungeon():
	print('After picking up the map, the torches strung to the walls all light up with a burst of flames!')
	time.sleep(4)
	print('You take a look at the map, its burnt and in terrible condition. You can only make out one section')
	time.sleep(5)
	print('THE DANK DUNGEONS....')
	time.sleep(4)
	print('You notice the sword on the floor, you pick it up and delve into the cave')
	print()
	print()
	time.sleep(5)
	print('After following the trail of torches for a couple of moments a shadowy figure approaches...')

def fightcheck():
	destination = ''
	while destination != 'attack' and destination != 'talk':
		print('Do you attack or attempt to talk to the figure?')
		destination = input()
		if destination == 'talk':
			print()
			print('You Talk however..... THIS IS A PLACEHOLDER!!!')
			print()
			time.sleep(5)
			print('The END')
			Again()
		else:
			print('The figure notices your act of aggression and takes hostile action')
			time.sleep(2)
			print('He charges his fireball!!')
			time.sleep(3)
			print('YOU HAVE DIED')
			time.sleep(3)
			Again()

	return destination

def Again():
	while True:
		print('Do you want to play again? (yes or no)')
		print('Please hit yes, come on you love this game!!')
		Again = input()
		if Again == 'yes':
			break

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

	gamesIntro() 

	caveNumber = chooseCave()

	checkcheck(caveNumber)

	destinationDungeon()

	attackchoice = fightcheck()

	print('Do you want to play again? (yes or no)')
	playAgain = input()
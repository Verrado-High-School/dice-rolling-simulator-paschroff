# Preston Schroff
# Period 1
# Dice Rolling Simulator

import random

rollNumber = 0
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
hundred = 100

print("Welcome to Dice Rolling Simulator")
print("")
pinput = int(input("How many times would you like to roll the dice?"))
print("")

while True:
	rollNumber = rollNumber + 1
	randomNum = random.randint(1,6)
	print ("Roll: " + str(rollNumber) + "  " + "What the dice landed on: " + str(randomNum))
	if rollNumber >= pinput:
		if randomNum == 1:
			break
		if randomNum == 2:
			break
		if randomNum == 3:
			break
		if randomNum == 4:
			break
		if randomNum == 5:
			break
		if randomNum == 6:
			break

	if randomNum == 1:
		ones = ones + 1
	if randomNum == 2:
		twos = twos + 1
	if randomNum == 3:
		threes = threes + 1
	if randomNum == 4:
		fours = fours + 1
	if randomNum == 5:
		fives = fives + 1
	if randomNum == 6:
		sixes = sixes + 1

print("")    
print("Results after rolling the dice " + str(pinput) + " times: ")
print("")
print("Number of times dice landed on one: " + str(ones))
print("Number of times dice landed on two: " + str(twos))
print("Number of times dice landed on three: " + str(threes))
print("Number of times dice landed on four: " + str(fours))
print("Number of times dice landed on five: " + str(fives))
print("Number of times dice landed on six: " + str(sixes))
print("")
print("Percentage of rolls that landed on one: " + str(ones/rollNumber*100) + "%")
print("Percentage of rolls that landed on two: " + str(((twos) / (rollNumber))*100) + "%")
print("Percentage of rolls that landed on three: " + str(((threes) / (rollNumber))*100)  + "%")
print("Percentage of rolls that landed on four: " + str(((fours) / (rollNumber))*100) + "%")
print("Percentage of rolls that landed on five: " + str(((fives) / (rollNumber))*100) + "%")
print("Percentage of rolls that landed on six: " + str(((sixes) / (rollNumber))*100) + "%")

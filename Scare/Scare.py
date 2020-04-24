import random
import time
import winsound
n1 = 0
n2 = 0 

print("Warning I don’t take responsibility for death because of a heart attack. Use at your own risk. By typing yes you're taking responsibility for certain consequences for using this script.")

def start():
	n1 = input("Max time for scare: ")
	print(n1)
	n1 = int(n1)
	n2 = input("least time for scare: ")
	print(n2)
	n2 = int(n2)
	print("Wach out")
	n = random.uniform(n1, n2)
	time.sleep(n)
	scare()

def scare():
	winsound.PlaySound("BLAAA", winsound.SND_FILENAME)
	print("haha got you")
	time.sleep(3)

if input("Type Yes to continue: ") == "Yes" or "yes":
	print("Good Luck")
	start()

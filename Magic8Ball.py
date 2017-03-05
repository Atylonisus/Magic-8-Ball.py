"""
Use raw_input() to get user to ask a question
Computer cycles through 20 responses randomly (import the random module), use a dictionary or list range(0,20) or (1,21)
No matter what they type, pick one of those 20 and display
Allow the user to do it all over again if they want
DISPLAY an in-progress message ("I am thinking...") --> Wait() function/sleep from time

MagicResponse = {}					# an empty dictionary, because a range
									# would not tie numbers to responses
#actually, fill that dictionary out with 20 responses

import random
response = random(MagicResponse from 0-19) 	#or something to this effect, choose any value out of the dict

But FIRST, you need to ask a question with
raw_input("Ask your most Burning Questions, and I will have a response...\n> ")

"""
import random
from time import sleep

MagicResponse = {
0:"I don't think so.",
1:"It is decidedly so.",
2:"Signs point to yes.",
3:"Anybody else would say you are crazy. But sure.",
4:"Life is meaningless but for our own intervention",
5:"Literally go do anything else but this.",
6:"Common sense says not.",
7:"That sounds lovely, I hope so.",
8:"Not in your wildest dreams.",
9:"The Truth is too terrible to speak.",
10:"Why ask when you already know what you're hoping for?",
11:"Come back later, the Powers which Move me made a coding error again.",
12:"Realistically how would a 20 response magic 8 ball be designed? Think how large the facets would have to be to legibly read the text.",
13:"If I give a different response to the same question asked multiple times, what does that mean?",
14:"Hard yes. Firm yes... It's gonna happen.\nProbably.\n\nEh.",
15:"Your concerns are inconsequential; focus instead on the imperative of interplanetary colonization.",
16:"Good Question. I might ask you the same thing. But I won't. I'll ask you this:",
17:"Nope.",
18:"Are you asking because you want to know, or are you asking because you are afraid to know?",
19:"The most insidious thing you can do is make excuses to not be your happiest self.",
20:"know yourself and the answer will come before the question... Is the punchline to this laffy taffy wrapper."
}

def EndPrompt():
	answer = raw_input("Do you wish to play again, y/n?\n> ")
	if answer == "y":
		sleep(1)
		StartGame()
	else:
		print "Game Over."

def AskMe():
	Question = raw_input("Ask your most Burning Questions, and I will have a response...\n> ")
	print "\nSo, you wish to know about %r..." % Question
	sleep(2)									#I hate waiting, when i have errors
	print random.choice(MagicResponse.values())
	sleep(1)
	EndPrompt()
		
def StartGame():
		print "~~~~~\nWelcome to the game!\n~~~~~"
		AskMe()
		
StartGame()

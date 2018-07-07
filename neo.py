import aiml 
import time
neo = aiml.Kernel()
neo.learn('intro.aiml')
# neo.respond("load aiml b")

while True:
	query = raw_input("YOU :> ")
	if query.lower() == "stop":
		time.sleep(0.5)
		print('Ok Bye')
		time.sleep(1)
		print('Nice to chat You :) ')
		break
	else:	
		time.sleep(0.5)
		responce = neo.respond(query)
		print("Neo:> {}".format(responce))		

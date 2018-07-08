import aiml 
import time
nemo = aiml.Kernel()
nemo.learn('intro.aiml')
nemo.learn('ai.aiml')
nemo.learn('Business.aiml')
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
		time.sleep(0.2)
		responce = nemo.respond(query)
		print("Neo:> {}".format(responce))		

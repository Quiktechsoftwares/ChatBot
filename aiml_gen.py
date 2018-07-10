print("""
|~|||\/||   |~_[~|\ ||~||~)|~|~|~/~\|~)
|~|||  ||_  |_|[_| \||~||~\|~| | \_/|~\
	""")
print("""
This Python file generates basic AIML file struture Only, 
                 ###### STILL UNDER CONSTRUCTION #########
                 Enter "stop" to quit
	""")

filename = raw_input("Enter The File Name: ")
myfile = open(filename+".aiml", 'a+')
myfile.write("""<?xml version="1.0" encoding="ISO-8859-1"?>""")
myfile.write("\n")
myfile.write('<aiml>')
myfile.write("\n")
while True:
	query = raw_input("Question: ")
	if query == "stop":
		myfile.write("\n")
		myfile.write("</aiml>")
		myfile.close()
		break
		
	responce = raw_input("responce: ")
	myfile.write('<category><pattern>{}</pattern>'.format(query.upper()))
	myfile.write('<template>{}</template></category>'.format(responce))
	myfile.write("\n")
	print("\n")
	
print("""
|~|||\/||   |~_[~|\ ||~||~)|~|~|~/~\|~)
|~|||  ||_  |_|[_| \||~||~\|~| | \_/|~\
	""")
print("""
This Python file generates basic AIML file struture between <catogory> tags only
 In Default it creates normal text, You need to put some extra stuff tags for a fully
functional
                 ###### STILL UNDER CONSTRUCTION #########
                 Enter "stop" to quit
	""")

filename = raw_input("Enter The File Name: ")
myfile = open(filename, 'a+')
while True:
	query = raw_input("Question: ")
	if query == "stop":
		break
		myfile.close()
	responce = raw_input("responce: ")
	myfile.write('<category><pattern>{}</pattern>'.format(query.upper()))
	myfile.write('<template>{}</template></category>'.format(responce))
	myfile.write("\n")
	print("\n")
	
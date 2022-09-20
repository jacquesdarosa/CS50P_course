'''name = input("What's your name? ")'''

'''if name == "Harry":
    print("Gryffindor")

elif name == "Hermione":
    print("Gryffindor")

elif name == "Ron":
    print("Gryffindor")

elif name == "Draco":
    print("Slythterin")

else:
    print("Who?")'''

# another way to write this

'''if name == "Harry" or name == "Hermione" or name == "Ron":
     print("Gryffindor")

elif name == "Draco":
    print("Slytherin")

else:
    print("Who?")'''

# using match will return an error since match is only available on Python ≥ 3.10


'''name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    
    case "Hermione":
        print("Gryffindor")
   
    case "Ron":
        print("Gryffindor")
    
    case "Draco":
        print("Slytherin")'''

import sys
 
 
print("User Current Version:-", sys.version)
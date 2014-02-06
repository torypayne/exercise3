import arithmetic

print "Calculator here, at your service! Give me numbers to math or q to get out of here"

while True:
    
    userinput = raw_input()
    
    tokens = userinput.split(" ")

    doubleoperators = ["+","-","*","/","mod","pow"]
    singleoperators = ["cube","square"]
    
    #Checking that the values are numbers in two value expresions
    if tokens[0] in doubleoperators:
        try:
            int(tokens[1])
            int(tokens[2])
        except ValueError: 
            print "use your numbers"
            continue

    #Checking that the value is a number in one value expressions
    elif tokens[0] in singleoperators:
        try:
            int(tokens[1])
        except ValueError:
            print "use your numbers"
            continue

    #Dealing with extra values for two value expressions
    if tokens[0] in doubleoperators:
        try:
           tokens[3] == True
        except IndexError: 
           print "I can only handle two values with that expression"
           continue

    #Dealing with extra values for one value expressions
    elif tokens[0] == singleoperators:
        try:
            tokens[2] == True
        except IndexError:
          print "I can only handle one value with this expression"
        

    if tokens[0] == "q":
        break
    
    elif tokens[0] == "+":
        print arithmetic.add(int(tokens[1]),int(tokens[2]))

    elif tokens[0] == "-":
        print arithmetic.subtract(int(tokens[1]),int(tokens[2]))
    
    elif tokens[0] == "*":
        print arithmetic.multiply(int(tokens[1]),int(tokens[2]))

    elif tokens[0] == "/":
        print arithmetic.divide(float(tokens[1]),float(tokens[2]))

    elif tokens[0] == "square":
        print arithmetic.square(int(tokens[1]))

    elif tokens[0] == "cube":
        print arithmetic.cube(int(tokens[1]))

    elif tokens[0] == "pow":
        print arithmetic.power(int(tokens[1]),int(tokens[2]))

    elif tokens[0] == "mod":
        print arithmetic.mod(int(tokens[1]),int(tokens[2]))

    else:
         print "Sorry, I can't process that"
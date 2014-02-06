import arithmetic

print "Calculator here, at your service! Give me numbers to math or q to get out of here"

while True:
    
    userinput = raw_input()
    
    tokens = userinput.split(" ")

    if tokens[0] == "q":
        break
    
    if tokens[0] == "+":
        print arithmetic.add(int(tokens[1]),int(tokens[2]))
        continue

    if tokens[0] == "-":
        print arithmetic.subtract(int(tokens[1]),int(tokens[2]))
        continue

    if tokens[0] == "*":
        print arithmetic.multiply(int(tokens[1]),int(tokens[2]))
        continue

    if tokens[0] == "/":
        print arithmetic.divide(float(tokens[1]),float(tokens[2]))
        continue

    if tokens[0] == "square":
        print arithmetic.square(int(tokens[1]))
        continue

    if tokens[0] == "cube":
        print arithmetic.cube(int(tokens[1]))
        continue

    if tokens[0] == "pow":
        print arithmetic.power(int(tokens[1]),int(tokens[2]))
        continue

    if tokens[0] == "mod":
        print arithmetic.mod(int(tokens[1]),int(tokens[2]))
        continue

    else:
         print "Sorry, I can't process that"
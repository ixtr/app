import random
in_file = open("input.txt", "r")
out_file = open("output.txt", "w")
#read each line of the input file
for line in in_file:
    #generate a random 5 digit number
    rand_a = random.randint(1000,9999)
    rand_b = random.randint(1,6)
    rand_c = random.randint(450,475)    
    #add the random number to the beginning of the line
    new_line = str(rand_a) + str(rand_b) + line + str(rand_c)
    #write the new line to the output file
    out_file.write(new_line)
in_file.close()
out_file.close()

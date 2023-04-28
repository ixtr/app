import random
in_file  = open("input.txt", "r")
out_file = open("output.txt", "w")
#read each line of the input file
for line in in_file:
    #generate a random 5 digit number
    rand_num = random.randint(10000,99999)
    #add the random number to the beginning of the line
    new_line = str(rand_num) + line
    #write the new line to the output file
    out_file.write(new_line)
in_file.close()
out_file.close()

import random

#open the output file
out_file = open("output.txt", "w")

#generate the first number in the list
rand_num = random.randint(1000000000000000,9999999999999999)
out_file.write(str(rand_num)+"\n")

#generate the rest of the numbers in the list
for i in range(1,50):
    #generate a random 16 digit number
    rand_num = random.randint(1000000000000000,9999999999999999)
    #change some of the digits in the number
    new_num = ""
    for c in str(rand_num):
        if random.randint(0,1) == 1:
            #change the digit to a random number
            new_num += str(random.randint(0,9))
        else:
            #keep the digit
            new_num += c
    #write the new number to the output file
    out_file.write(new_num+"\n")

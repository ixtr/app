# Open the file
file = open('workfile01.txt', 'r')

# Read the file contents
text = file.read()

# Close the file
file.close()

# Split the words into a list 
words = text.split() 

# Use a for loop to iterate through the list of words 
for i in range(len(words)): 
    if words[i] == 'vvv*1701k19*11*': 
        words[i] = '<a href="https://github.com/wattie/song' 
    elif words[i] == '*67AH17*ttt*719*': 
        words[i] = '">' 
    elif words[i] == '*200667*sss*235395*719*': 
        words[i] = '</a><br>' 

# Join the words back into a string
new_text = ' '.join(words) 

# Open the file in write mode
file = open('outworkfile02.txt', 'w')

# Write the new text to the file
file.write(new_text)

# Close the file
file.close()

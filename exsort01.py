with open("extendedwf02.txt", "r") as f:
    lines = f.readlines()
    with open("exchange.txt", "w") as new_f:
        for line in lines:
            line_new = "<a href=\"https://github.com/wallerellei4/?4=" + line[5:]
            line_new = line_new[:58] + "\"/><br>" + line_new[58:]
            new_f.write(line_new + "\n")

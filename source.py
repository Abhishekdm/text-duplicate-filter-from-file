def checkLine(rline):
    write_file = open('output.txt', 'r')
    for line in write_file:
        # elements passed as paramaters for lstrip will remove the matching elements from the leftside of the string
        wline = line.lstrip('0123456789.')
        if (wline == rline):
            return True


read_file = open('text.txt', 'r')
# creating output.txt file
create_file=open('output.txt','w')
create_file.close()

for line in read_file:
    if(checkLine(line.lstrip('0123456789.'))):
        print("line already exist")
    else:
        wrt_file = open('output.txt', 'a')
        wrt_file.write(line)
        wrt_file.close()
print("completed")

a = open("demofile.txt","a")        #open existing file and append text to it
a.write("newly added line")
a.close()

f = open("demofile.txt","r")        #print the file with appended text
print(f.read())
f.close()

f = open("tempfile.txt","x")        #create a new file and write text to file
f.write("newly created file")
f.close()
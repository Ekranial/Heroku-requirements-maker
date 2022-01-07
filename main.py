file = open("input.txt")
file2 = open("requirements.txt", "w")
text = file.readlines()
for i in range(len(text)):
    s = str(text[i]).replace("\n", "")
    first = s.find(" ")
    s = s.replace(" ", "")
    s = s[0:first] + "==" + s[first:len(s)]
    file2.write(f"{s}\n")
file.close()
file2.close()

text_file = open("word.txt", "r")
line = text_file.readlines()

check = line[0].split('\n')[0]

c = 0

if check == 'a':
	c += 20
print c

text_file.close()
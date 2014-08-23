text_file = open("word.txt", "r")
line = text_file.readlines()

#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's' , 't', 'u', 'v', 'w', 'x', 'y', 'z']

# check = line[0].split('\n')[0]
count = 0

alph = raw_input('alphabet: ')

for i in range(len(line)):
	word = line[i].split()
	check = line[i].split(alph)
	if len(word) != len(check):
		count += 1

prob = float(count)/len(line)
print 'prob:',prob

# prob = float(count/len(text))

# print prob

text_file.close()
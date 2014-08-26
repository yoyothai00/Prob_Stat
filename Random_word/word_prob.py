text_file = open("word.txt", "r")
line = text_file.readlines()

count = 0
# alph = raw_input('alphabet: ')
vowel = ['a', 'e', 'i', 'o', 'u']

for i in range(len(line)):
	word = list(line[i])
	check_vowel = False
	temp_count = 0
	for j in range(len(word)):
		for k in range(len(vowel)):
			if word[j] == vowel[k]:
				temp_count += 1
				break
	if temp_count > 3:
		count+=1

prob = float(count)/len(line)
print 'prob:',prob

text_file.close()
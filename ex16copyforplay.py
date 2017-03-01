from sys import argv

script, filename = argv

target = open(filename, 'w')

print "Now I'm going to ask you for three lines."

sentence = raw_input("Please write your sentence: ")

print "I'm going to write these to the file."

target.write(sentence)

print "And finally we close it."
target.close()

file = open('my_file.txt', 'w')
file.write('I have created one file!\n')
file.close()

file = open('my_file.txt', 'r+')
file.readline()
file.write('This is the second text in my file!\n')

file.seek(0)
print(file.read())
file.close()

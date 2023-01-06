#open file

file = open('data.txt','r')

#readlines
show = file.readlines()

#show all data in list
for x in show:
    print(x)

#close file
file.close()


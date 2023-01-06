name = input('enter your name: ')
kelas = input('enter your class: ')

teks = f'''
=======
BIODATA
=======

my name is {name}
and my class is {kelas}

'''
file = open ('biodata.txt','w')

file.write(teks)


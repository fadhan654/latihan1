#area of triangel
alas=int(input('input base: '))
tinggi=int(input('input high: '))
luas=0.5*alas*tinggi

teks=f'''
luas segitiga adalah {luas}
'''
file=open('area of triangel.txt','w')

readfile=file.read

file.write(teks)
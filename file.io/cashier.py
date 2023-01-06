menu=input('input menu: ')
price=int(input('input price of menu: '))
quantity=int(input('input your quantity: '))
quantity2=price * quantity
total_money=int(input('input your money: '))
return_money=total_money - quantity2

teks = f'''
menu: {menu}
price: {price}
quantity: {quantity}
total price: {quantity2}
total money: {total_money}
return: {return_money}

'''
file = open('nota.txt','w')

file.write(teks)
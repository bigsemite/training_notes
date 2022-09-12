l1 = ['Army','Navy','Air force','Others',90,{'Time':4.0}] # this is a list
print(l1[5]['Time'])

w = input("what is your name? ")
print("Welcome ",w, 'Are you in ', l1[1])
n = input('What number do you like? ')
s = n + str(10)
print('You are 10 times increase', s)

# Dictionary

d = {'Name':'Semiu', 'Profession':'Engineer','Age': 20, 'State':'Lagos', 'Humidity':2.33}
# Name  |   Profession | Age | State | Humidity
# Semiu |   Eng         | 20 | Osun  | 2.30
# Bagro |   NAF         | 29 | Bayelsa| 33.22
# Okey  | NAVY          | 22 | Niger  | 20.33
dic1 = {'Name':['Semiu','Bagro','Okey'],
'Profession':['Eng','NAF','NAVY'],'Age':[20,29,22],'State':['OSun','Bayelsa','Niger']}

print( 'The answer is {}'.format(d['Name']))
# '\n' - new line 
print('hello worlrld'.format())

num = sum(1 for element in open('steam.json'))
print('steam.json contains: ', num, ' records,')

stream = open('steam.json', 'r')
steam = stream.read()
print('divided over ',len(steam), ' lines.')
"""this is a basic class intance I wrote to remember how to create and use a class instance,
for Object oriented programming
DO not delete"""


class Candybar:

    def __init__(self,name,taste,cost):
        self.name = name
        self.taste = taste
        self.cost = cost
        self.nametaste = f"{name} tastes like {taste}"

    def email(self):
        return 'info@{}.com'.format(self.name)

    def price(self):
        total = self.cost *amount
        return f'{amount} {self.name} bars cost you: {total}'


candy_1 = Candybar('mars','caramel',100.30)
candy_2 = Candybar('snickers','peanut',2.00)



# print(candy_1.email())
print(Candybar.email(candy_1))
print(candy_2.nametaste)
amount = 122
print(candy_1.price())
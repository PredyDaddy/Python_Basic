# A simple 2 class implementation for an online shopping
# application

class Customer:
    """Represents a customer for an online shop"""

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.basket = []
        self.cost = 0.0

    def buyItem(self, item):
        self.basket.append(item)
        self.cost += item.price

    def removeItem(self, item):
        """Removes an item from the basket
           Returns True is removed, False if not present"""
        if item in self.basket:
            self.cost -= item.price
            self.basket.remove(item)
            return True
        else:
            print('Not in the basket')
            return False

    def removeItemByName(self, name):
        """Removes an item from the basket
           Returns True is removed, False if not present"""
        for i in self.basket:
            if i.name == name:
                self.cost -= i.price
                self.basket.remove(i)
                return True
        # If we get here, the named item was not in the basket
        return False

    def showCost(self):
        """Returns the total cost of the basket"""
        print(f'Total cost is £{self.cost:.2f}')
        return self.cost

    def discountBasket(self, rate):
        """Make a discount of rate %
           Returns True is rate is between 10 ro 50% inclusive, False otherwise"""
        if rate >= 10.0 and rate <= 50.0:
            for i in self.basket:
                disc = i.price*(rate/100)
                i.price = i.price - disc
                self.cost -= disc
            return True
        else:
            print('Invalid rate')
            return False

class Item:
    """Represents something we can buy in an online shop"""

    def __init__(self,name, price):
        self.name = name
        self.price = price

    def changeName(self, newName):
        self.name = newName
class TestShoppingApplication():
    def setUp(self):
        print('test start')
    def teardown(self):
        print('test end')
    def test_1(self):
        self.c1 = Customer()
        self.c2 = Customer()
        self.c3 = Customer()
        self.i1 = Item()
        self.i2 = Item()
        self.i3 = Item()
        self.c1.buyItem('i1')
        self.c1.buyItem('i2')
        self.c2.buyItem('i1')
        self.c2.buyItem('i3')
        self.assertEqual(self.c1.showCost(),80)
        self.assertEqual(self.c2.showCost(),150)
        self.assertEqual(self.c3.showCost(),0)
        self.c1.removeItem('i1')
        self.assertTrue(self.c1.removeItem('i1'))
        self.assertFalse(self.c1.removeItem('i3'))
        self.c1.removeItemByName('table lamp')
        self.c2.removeItemByName('small table')
        self.assertEqual(self.c1.showCost(),0)
        self.assertEqual(self.c2.showCost(),100)
    def test_2(self):
        self.c1 = Customer()
        self.c2 = Customer()
        self.c3 = Customer()
        self.i1 = Item()
        self.i2 = Item()
        self.i3 = Item()
        self.c1.buyItem('i1')
        self.c1.buyItem('i2')
        self.c2.buyItem('i1')
        self.c2.buyItem('i3')
        self.c3.buyItem('i3')
        self.i3.changeName('red rug')
        self.assertEqual(self.c1.showCost(),80)
        self.assertEqual(self.c2.showCost(),150)
        self.assertEqual(self.c3.showCost(),100)
        self.c1.discountBasket(10)
        self.assertTrue(self.c1.discountBasket(72))
        self.c2.discountBasket(60)
        self.assertEqual(self.c2.showCost(),150)

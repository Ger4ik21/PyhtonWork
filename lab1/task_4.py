class FruitGarden:
    def __init__(self, garden_square, trees_amount):
        self.garden_square = garden_square
        self.trees_amount = trees_amount
        self.fruite_type = "Fruit"

    def amount_inc(self):
        self.trees_amount += 1
        print("Tress amount increased!")

    def amount_decr(self):
        if self.trees_amount > 0:
            self.trees_amount -= 1
            print("Tress amount decreased!")
        else:
            print("The amount of trees is lower than 1! Cannot decrease!")

    def info(self):
        print("Garden square: ", self.garden_square, ". Amount of trees: ", self.trees_amount, ". Fruites type: ", self.fruite_type)

class AppleGarden(FruitGarden):
    def __init__(self, garden_square, trees_amount):
        super().__init__(garden_square, trees_amount)
        self.fruite_type = "Apple"

    def print_specific_info(self):
        print("This is a garden with apple trees.")

    def polym(self):
        print("Polymorphic method in Apple Garden")  


class PearGarden(FruitGarden):
    def __init__(self, garden_square, trees_amount):
        super().__init__(garden_square, trees_amount)
        self.fruite_type = "Pear"

    def print_specific_info(self):
        print("This is a garden with pear trees.")

    def polym(self):
        print("Polymorphic method in Pear Garden")   




g1 = FruitGarden(5000, 20)
g1.info()
g1.amount_inc()
g1.amount_decr()
g1.info()

apple = AppleGarden(1000, 20)
pear = PearGarden(500, 10)
apple.info()
apple.print_specific_info()
apple.amount_inc()
apple.amount_decr()
apple.info()
apple.polym()
pear.info()
pear.print_specific_info()
pear.amount_inc()
pear.amount_decr()
pear.info()
pear.polym()
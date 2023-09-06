class FruitGarden:
    def __init__(self, garden_square, trees_amount, fruite_type):
        self.__garden_square = garden_square
        self.__trees_amount = trees_amount
        self.__fruite_type = fruite_type

    def amount_inc(self):
        self.__trees_amount += 1
        print("Tress amount increased!")

    def amount_decr(self):
        if self.__trees_amount > 0:
            self.__trees_amount -= 1
            print("Tress amount decreased!")
        else:
            print("The amount of trees is lower than 1! Cannot decrease!")



    def info(self):
        print("Garden square: ", self.__garden_square, ". Amount of trees: ", self.__trees_amount, ". Fruites type: ", self.__fruite_type)

g1 = FruitGarden(5000, 20, "Apple")
g1.info()
g1.amount_inc()
g1.amount_decr()
g1.info()
g2 = FruitGarden(1000, 10, "Peach")
g2.info()
g2.amount_inc()
g2.amount_decr()
g2.info()
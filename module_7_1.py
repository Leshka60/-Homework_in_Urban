class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        self.file = open(self.__file_name, 'a')
        self.file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        goods = file.read()
        file.close()
        return goods

    def add(self, *products):
        for goods in products:
            if goods.name not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(goods.__str__() + '\n')

            else:
                print(f'Продукт {goods.name} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

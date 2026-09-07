# Create class Dish - instance attributes: dish_id (int), name (str),
# price (int)
# Create class Menu - instance attributes: dishes (list of Dish objects).
# Implement appropriate methods so that Menu objects support the following
# operations:
# d = Dish(0, 'Lasagna', 20)
# m = Menu()
# m.append(d) - dish appended to m.dishes
# m[0] - implement getitem on Menu
# d in m - implement membership test operators
# len(m) - return length of m.dishes
# Have 2 dishes created with same values for attributes (d1 and d2). Add d1 to
# the menu instance m. Test membership of d2 in m. Does it find d2 in menu? Why?
# Modify Dish to test for equality by looking at dish_id, name, price being the
# same, so that the dishes above would make this true d1 == d2. Test d2 in m
# again.
# Modify the getitem dunder to get the dish with the dish_id equal with the
# argument given. Raise KeyError if not found.

class Dish:
    def __init__(self, dish_id, name, price):
        self.id = dish_id
        self.name = name
        self.price = price

    def __eq__(self, other):
        return (self.id, self.name, self.price) == (
            other.id, other.name, other.price)


class Menu:
    def __init__(self, dishes=None):
        if not dishes:
            dishes = []
        self.dishes = dishes

    def append(self, item):
        self.dishes.append(item)

    def __getitem__(self, dish_id):
        for dish in self.dishes:
            if dish.id == dish_id:
                return dish
        raise KeyError(f"Dish with id={dish_id} not found.")

    def __contains__(self, item):
        return item in self.dishes

    def __len__(self):
        return len(self.dishes)


if __name__ == "__main__":
    d = Dish(123, 'Lasagna', 20)
    m = Menu()
    m.append(d)
    try:
        print(m[0])
    except KeyError as ex:
        print(ex)
    print(m[123])
    print(d in m)
    print(len(m))

    d1 = Dish(562, 'Pizza', 15)
    d2 = Dish(562, 'Pizza', 15)

    m.append(d1)
    print(d2 in m)

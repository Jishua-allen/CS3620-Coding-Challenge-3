def student_discount(price):
    return price * 0.90


def regular_buyer_discount(price):
    return student_discount(price) * 0.95


originalPrice = 100
print("Part 1: Discount functions")
print("Original price: " + str(originalPrice))
print("Student discounted price: {0}".format(student_discount(originalPrice)))
print("Regular Buyer discounted price: {0}\n\n".format(regular_buyer_discount(originalPrice)))


print("Part 2: Calculate x*(x+5)^2 where x= 5 using lambdas")
print("Answer: {0}\n\n".format((lambda x: x*(x+5)**2)(5)))


def markdown(price):
    return round(price * .90, 2)


print("Part 3: Editing a list with map")
prices = [12.99, 4.99, 3.75, 5.50, 25.00, 39.99, 499.95, 15.35]
print("Original list: {0}".format(prices))
print("List discounted by 10%: {0}\n\n".format(list(map(markdown, prices))))


class Computer:
    def __init__(self, ram, cpu, graphics_card):
        self.ram = ram
        self.cpu = cpu
        self.graphics_card = graphics_card

    def get_specs(self, ram, cpu, graphics_card):
        self.ram = ram
        self.cpu = cpu
        self.graphics_card = graphics_card

    def display_specs(self):
        print("CPU: {0}".format(self.cpu))
        print("ram: {0}gb".format(self.ram))
        print("graphics card: {0}".format(self.graphics_card))


class Desktop(Computer):
    monitor = ""

    def get_desktop_specs(self, monitor):
        self.monitor = monitor

    def display_specs(self):
        super().display_specs()
        print("monitor: {0}".format(self.monitor))


class Laptop(Computer):
    model = ""

    def get_laptop_specs(self, model):
        self.model = model

    def display_specs(self):
        super().display_specs()
        print("model: {0} lbs".format(self.model))


desktop = Desktop(32, "AMD ryzen 5 3600", "Geforce RTX 3060TI founders edition")
laptop = Laptop(16, "Intel Core I7", "AMD Radeon Pro 5300M")

print("Desktop specs:")
desktop.get_specs(16, "AMD ryzen 5 3600", "Geforce RTX 3060TI founders edition")
desktop.get_desktop_specs("HP X27q 165Hz 27\"")
desktop.display_specs()

print("\n\nLaptop Specs:")
laptop.get_laptop_specs("2019 Macbook pro 16\"")
laptop.display_specs()


class Integer:
    def __init__(self, integer):
        self.integer = integer

    def __mul__(self, other):
        return self.integer + other.integer


print("\n\nPart 5 overloading the multiplication operator to addition")
int1 = Integer(4)
int2 = Integer(5)

print("Overloading multiply so 5*4 = ... {0}".format(int1 * int2))


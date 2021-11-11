
class Juicer:
    ''' A simple juice making machine '''
    # Class properties
    power_status = "OFF"
    sugar = 0
    milk = 0
    hot_water = 0
    a_f1 = 0
    a_f2 = 0
    j_hotwater = 0
    j_sugar = 0
    j_fruit1 = 0
    j_fruit2 = 0
    name_fruit1 = ""
    name_fruit2 = ""
    j_milk = 0

    
    # Constructor
    def __init__(self, connection):
        self.power_status = connection

    # Class methords
    def switch_on(self):
        self.power_status = "ON"
    
    def mixed_juice(self):
        t_am = self.sugar + self.milk + self.hot_water + self.a_f1 + self.a_f2
        self.j_hotwater = (self.hot_water / t_am) * 100.0
        self.j_sugar = (self.sugar / t_am) * 100.0
        self.j_milk = (self.milk / t_am) * 100.0
        self.j_fruit1 = (self.a_f1 / t_am) * 100.0
        self.j_fruit2 = (self.a_f2 / t_am) * 100.0

    def get_juice(self):
        print("amount of hot water(%): ", self.j_hotwater)
        print("amount of sugar(%): ", self.j_sugar)
        print("amount of milk(%): ", self.j_milk)
        print("amount of ", self.name_fruit1, "(%): ", self.j_fruit1)
        print("amount of ", self.name_fruit2, "(%): ", self.j_fruit2)
        print("Bye from", self)

    def setup_machine(self, user_fruit1, u_af1, user_fruit2, u_af2):
        self.name_fruit1 = user_fruit1 
        self.name_fruit2 = user_fruit2 
        if (u_af1 + u_af2) < 100:
            self.a_f1 = u_af1
            self.a_f2 = u_af2
        else:
            print("Your amount is exceed the requirement") 
    
    def add_ingredients(self):
        self.a_f1 = self.a_f1 / 2
        self.a_f2 = self.a_f2 / 2
        if (self.a_f1 + self.a_f2)  < 40:
            self.sugar = 15
            self.milk = 25
        else:
            self.sugar =10
            self.milk = 20

        self.hot_water = 20

def customer_input():
    mes = "choice the fruits from this list:'mango','orange','banana' \
           give the amount in percentage"
    print(mes)

    n_fr1 = input("Give a Fruiet Name:")
    a_fr1 = int(input("Give the ammount:"))
    n_fr2 = input("Give second Fruiet Name:")
    a_fr2 = int(input("Give the ammount (2):"))

    return n_fr1, a_fr1, n_fr2, a_fr2

# Make an object
j   = Juicer(connection="ON")

# Get user input
(a, b, c, d) = customer_input()
print("After Customer Input:", a, b, c, d)

# Power On of the machine
print(j.power_status)

# Setting the mechaine with user options
j.setup_machine(a, b ,c ,d)

# Add all the ingredient
j.add_ingredients()

# Mixe all the ingredient
j.mixed_juice()

# Get the juice
j.get_juice()

n   = Juicer(connection="OFF")
print(n.power_status)
(a, b, c, d) = customer_input()
print("After Customer Input:", a, b, c, d)
n.setup_machine(a, b ,c ,d)
n.add_ingredients()
n.mixed_juice()
n.get_juice()



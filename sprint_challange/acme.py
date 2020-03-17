import random

class Product:
    """
    Class for product :  
    name  - string with no default
    price - integer with default of 10 
    weight - integer with default of 20
    flammability - integer with default of 0.5
    identifier - random number from 100000 to 9999999
    """
    def __init__(self,
                name,
                price = 10,
                weight = 20,
                flammability = 0.5,
                identifier = random.randint(1000000,9999999)):

        self.name = name
        self.price=price
        self.weight=weight
        self.flammability = flammability
        self.identifier= identifier
    
    def stealability(self):
        """
        calculates stealability using price and weight of the product
        """
        if self.price/self.weight< 0.5 :
            print ("Not so stealable...")
        elif 1 > self.price/self.weight >= 0.5 :
            print ("Kinda stealable")
        else : 
            print ("Very stealabe")
        
    def explode(self):
        """
        calculates explodibility using flammability and weight of the product
        """
        self.flammability * self.weight
        if self.flammability * self.weight < 10 :
            print ("...fizzle.")
        elif 50 > self.flammability * self.weight >= 10 :
            print ("...boom!")
        else : 
            print ("...BABOOM!!")

    def stealability_for_flammable(self):
        """
        sets highly prices and hihgly flammable items on higher stealibility risk
        """
        (self.price/self.weight)*self.flammability
        if (self.price/self.weight)*self.flammability > 1  :
            print ("High risk, put in the safe")
        else : 
            print ("Not too bad")


class BoxingGlove(Product):
    """
    Subclass of Product: 
    name  - string with no default
    price - integer with default of 10 
    weight - integer with default of 20
    flammability - integer with default of 0.5
    identifier - random number from 100000 to 9999999
    """
    def __init__(self,
            name,
            price = 10,
            weight = 10,
            flammability = 0.5,
            identifier = random.randint(1000000,9999999)):
            super().__init__(name, price, weight, flammability, identifier)

    def stealability(self):
        """
        Letting people know gloves dont worth stealing
        """
        print("...It's a glove.")

    def punch(self):
        """
        How hurtful a gove is based on its weight
        """
        if self.weight < 5 :
            print("That tickles")
        elif 15 > self.weight >= 5 :
            print("Hey that hurt")
        else : 
            print("Ouch")
    




        
    


        
import random
from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """
    Use this function to generate 30 products and put them in different lists based on catagory.
    names - names of products dragged from Addjetives and Nouns
    prices - price of products randomly generated from 5 to 100
    weights - weights of products randomly generated from 5 to 100
    flamms - flammability randomly generated from 0.5 to 2.5
    """
    names = []
    prices = []
    weights = []
    flamms = []

    for x in range(num_products):
        product = Product(
            name =  [random.choice(ADJECTIVES) + " " + random.choice(NOUNS)],
            price = [randint(5,100)],
            weight = [randint(5,100)],
            flammability = [uniform(0.5,2.5)])
        names.append(name)
        prices.append(price)
        weights.append(weight)
        flamms.append(flammability)
    return names, prices, weights, flamms


def inventory_report(names, prices, weights, flamms):
    """
    printing an inventory report with the following componenets:
    Unique product names : number of unique products in the inventory
    Average weight: weight average of all listed products 
    Average flammabilty : flammability average of all listed products
    Average price : price average of all lusted products
    """
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print("unique product name:",len(set(names))
    print("Average price:", sum(prices)/len(prices))
    print("Unique prices:", len((set(prices))
    print("Average weight:", sum(weights)/len(weights))
    print("Unique weights:", len((set(weights))
    print("Average flammability:", sum(flamms)/len(flamms))

    
if __name__ == '__main__':
    inventory_report(generate_products())


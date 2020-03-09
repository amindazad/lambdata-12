# lambdata_amindazad/my_mod.py

def enlarge(n):
    """
    param n is a number
    Function will enlarge the number
    """
    return n*100

def train_test_split(x) :
    from sklearn.model_selection import train_test_split
    train , test = train_test_split(x, train_size=.85, test_size = .15, random_state=42)    
    return  train , test
    
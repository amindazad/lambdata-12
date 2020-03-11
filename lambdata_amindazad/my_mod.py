# lambdata_amindazad/my_mod.py
import pandas

def split(x) :
    from sklearn.model_selection import train_test_split
    train , test = train_test_split(df, train_size=.85, test_size = .15, random_state=42)
    train , val = train_test_split(train, train_size=.85, test_size = .15, random_state=42)    
    return  train , test, val
def find_null(x) :
    return x.isnull().sum().sort_values()

class DataProcessor():
    def __init__(self, my_df):
        """
        Param my_df pandas.DataFrame should have a column of "abbrev"
        """
        self.df = my_df
    def add_state_names(self):
        """
        Add a column of state names to a dataframe that already has the abbrevs
        Return a copy of the DataFrame with a new column called "name"
        """
        #names_map = {"CT": "Conn", "CO": "Colorado", "CA": "Cali"}
        names_map = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
        } # http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/
        #breakpoint() # python 3.7 or later, otherwise use pdb module
        self.df["name"] = self.df["abbrev"].map(names_map) # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
df1 = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
df2 = pandas.DataFrame({"abbrev": ["AZ", "DC", "CO", "MI", "WI"]})
for df in [df1, df2]:
    print("-------")
    processor = DataProcessor(df)
    print(type(processor))
    processor.add_state_names()
    print(processor.df.head())
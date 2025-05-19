import pandas as pd  # Importing the Pandas library
import numpy as np   # Importing NumPy

# Creating an empty Series
ser = pd.Series()
print("Pandas Series: ", ser)

# Creating a Series from a NumPy array
data = np.array(['g', 'e', 'e', 'k', 's'])
ser = pd.Series(data)
print("Pandas Series:\n", ser)

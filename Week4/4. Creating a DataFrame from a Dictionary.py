import pandas as pd

# Dictionary of lists
dict_data = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
             'degree': ["MBA", "BCA", "M.Tech", "MBA"],
             'score': [90, 40, 80, 98]}

df = pd.DataFrame(dict_data)
print(df)

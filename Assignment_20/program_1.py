"""
Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.
"""

import pandas as pd

data = {'Name': ['Test'], 'Age': [20], 'Mail Id': ['testuser@email.com'], 'Phone No': ['9034xxxxxxx']}
df = pd.DataFrame(data)

df.loc[1] = ['User1', 21, 'user1@email.com', '942xxxxxx']
df.loc[2] = ['User2', 20, 'user2@email.com', '827xxxxxxx']
df.loc[3] = ['User3', 20, 'user3@email.com', '717xxxxxxx']
print("Dataframes defined are as follows: ", df)
print("\n")

import pandas as pd

#Pandas Series => 1D Labelled Data

scores = [800, 1200, 568, 654, 1000]
players = pd.Series(scores, index = ["Soyinka", "Martin", "Nifemi", "John", "Ben"])
print(players)


#Pandas DataFrame => 2D Data (Table) => Rows and Columns

data = {
    "Player": ["Soyinka", "Martin", "Nifemi", "John", "Ben"],
    "Level": [15, 13, 17, 16, 20],
    "Score": [800, 1200, 568, 654, 1000]
}

df = pd.DataFrame(data)
print(df)


#Accessing Rows

print("Row 0 (Top Player)")
print(df.loc[0])

print("Row 2 and 3")
print(df.loc[2:3])


#Reading a csv file

data2 = pd.read_csv("leaderboard.csv")
print(data2.head())
print(data2.tail())
print("Dataset Information")
print(data2.info())

print("Missing values")
print(data2.isnull().sum())
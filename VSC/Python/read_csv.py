print("start uitlezen CSV") #kijken of de file werkt

import pandas #library voor lezen

#pandas gebruiken om csv uit te lezen en in een dataframe te zetten
df = pandas.read_csv('/Users/werk/Desktop/CodeFounders/VSC/Python/pokemon.csv') #als deze file ergens anders staat volledig path invullen

print(df["Name"])

for r,rij in df.iterrows(): # for loop
    print(rij["Name"])
    #print(rij["Attack"])

    
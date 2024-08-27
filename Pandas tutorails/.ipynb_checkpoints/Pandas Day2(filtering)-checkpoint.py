#Filetering  Columns and Rows 

#operations performed on population.csv
##################

import pandas as pd



#df = pd.read_csv(r"C:\Users\Ganseh\Downloads\world_population.csv")
#print(df)




#To find the Rank & To filter the no of column

#df = df[df['Rank']<= 10] #it will print columns having the rank below or equal to 10.
#print(df) 

#print(df.columns)

#################
#Specific Values in the perticular column (ISIN Function)

specific_countries = ["India","Mexico"]

#df = df[df['Country'].isin(specific_countries)] #it will search 'counrty1' and 'country2' in 'country'

#print(df)


#####################################
#Contains () - To search for specific String/Number/Value 
#df = df[df['Country'].str.contains('United')]
#print(df)
#it will search strings with 'united' init.



#################
#set.index = to set a perticular column as an index.
#here we stored result in the another dataframe


pd.set_option('display.max_rows',None)
df2 = df.set_index('Country')   #it will take 'country' column as an 'index'

#print(df2)


####################
#fiter() - To filter out perticualr columns/rows with
# perticular items and for perticular axis 'x' and 'y'.

df2 = df2.filter(items = ['Continent','CCA3'], axis=1) 

print(df)


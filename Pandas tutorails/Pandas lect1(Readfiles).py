# To read any file and add Datafram in Pandas 

import pandas as pd #pandas package


#To read the csv file on path.

df = pd.read_csv(r"C:\Users\Ganseh\Desktop\Retail  Project\csv files\member_data.csv")
#print(df)     #to print the file 


#To remove the column names from the files. 
df = pd.read_csv(r"C:\Users\Ganseh\Desktop\Retail  Project\csv files\member_data.csv", header = None)
#print(df)


# to give the custom names to the columns. 

df = pd.read_csv(r"C:\Users\Ganseh\Desktop\Retail  Project\csv files\member_data.csv", names = ["emp_id", "firstname", "lastname", "storeid", "registration"] )
#print(df)


# to not consider the first row of the file as the column name or header it generate by itself
 
df = pd.read_csv(r"C:\Users\Ganseh\Desktop\Retail  Project\csv files\member_data.csv", header= None )
#print(df)


# header=<int>: Useful when the header is located in a row other than the first.

df = pd.read_csv(r"C:\Users\Ganseh\Desktop\Retail  Project\csv files\member_data.csv", header= 1 )
#print(df)


#header=True/False: When writing a DataFrame, it controls whether the header row is included in the output file.



#########################################

#to read the '.txt' files  and remove the '\' from them.

df = pd.read_csv(r"C:\Users\Ganseh\Downloads\countries of the world.txt ",sep='\t' )
#print(df)

#OR
#without using the 'sep'
df = pd.read_table(r"C:\Users\Ganseh\Downloads\countries of the world.txt " )
#print(df)


################################################################

#To Read the Json files (in key value pair format (dictionary ))

df = pd.read_json(r"C:\Users\Ganseh\Downloads\json_sample.json" )
#print(df)



###########################################################################

# To read the XLSX files 

df = pd.read_excel(r"C:\Users\Ganseh\Downloads\world_population_excel_workbook.Xlsx" )
#print(df)


#to print the results for the perticular file in xlsx format.

df = pd.read_excel(r"C:\Users\Ganseh\Downloads\world_population_excel_workbook.Xlsx",sheet_name= 'Sheet1' )
#print(df)


####################################################################################################

#other functions


#to print all the rows 
pd.set_option('display.max.rows',None)


#to print mentioned number of rows
pd.set_option('display.max.rows',101) #have to mention before reading the file.


#to print all the present column in the file.
pd.set_option('display.max.columns',None)


df = pd.read_csv(r"C:\Users\Ganseh\Desktop\Retail  Project\csv files\member_data.csv")

#print(df)



# to print information of any 'data frame' 

#df.info() #return all the column names and data types 


# to print all the count of columns and rows 

#print(df.shape) #rows , columns


# to print top rows according to need (head).

print(df.head()) #by default 5

print(df.head(10))


#to print last rows accroding to need
 
print(df.tail()) #last default 5

#print(df.tail(10)) 


# Print data for the row with index label 'David'
#This will return the row at the integer index position 2. 
# Note that indexing is zero-based, so this will be the third row of the DataFrame.

#print(df.loc['member_id'])
print(df.index) #return index


# Print data for the row at position 2
print(df.iloc[2])

###############

#To print size columns X rows

print(df.size)


#tp print datatypes in data frame

print(df.dtypes) #returns data type of the columns


#to print the values in data frame

print(df.values) #prints values one by one separated by ','

#shows as per mentioned position result

print(df.index[0:5:1]) #from:to:step





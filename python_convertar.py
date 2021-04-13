
# # importing pandas library
# import pandas as pd
  
# # reading given csv file 
# # and creating dataframe
# websites = pd.read_csv("/Users/bahaafathi/Desktop/GeeksforGeeks.txt"
#                        ,header = None)
  
# # adding column headings
# websites.columns = ['Name', 'Type', 'Website']
  
# # store dataframe into csv file
# websites.to_csv('GeeksforGeeks.csv', 
#                 index = None)



                # importing panda library
import pandas as pd
  
# readinag given csv file
# and creating dataframe
dataframe1 = pd.read_csv("/Users/bahaafathi/Desktop/2.csv")
  
# storing this dataframe in a csv file
# dataframe1.to_csv('newtest.csv', 
#                   index = None)
dataframe1.to_json('large.json',orient='records',force_ascii=False,indent=2) 

           
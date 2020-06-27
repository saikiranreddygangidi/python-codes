# Importing the fuzzy package
import fuzzy
# Exploring the output of fuzzy.nysiis
a=fuzzy.nysiis('color')
# Testing equivalence of similar sounding words
fuzzy.nysiis('color')==fuzzy.nysiis(a)
# Reading in datasets/nytkids_yearly.csv, which is semicolon delimited.
author_df=pd.read_csv('datasets/nytkids_yearly.csv',';')

# Looping through author_df['Author'] to extract the authors first names
first_name = []
for name in author_df['Author']:
 first_name.append(name.split()[0])


# Adding first_name as a column to author_df
author_df['first_name'] = first_name 



# Checking out the first few rows of author_df
author_df.head()
import numpy

# Looping through author's first names to create the nysiis (fuzzy) equivalent
nysiis_name = []
for name in author_df['first_name']:
  nysiis_name.append(fuzzy.nysiis(name))  

# Adding nysiis_name as a column to author_df
author_df['nysiis_name']=nysiis_name

# Printing out the difference between unique firstnames and unique nysiis_names:
print(len(np.unique(author_df['first_name']))-len(np.unique(author_df['nysiis_name'])))

# Reading in datasets/babynames_nysiis.csv, which is semicolon delimited.
babies_df = pd.read_csv('datasets/babynames_nysiis.csv',';')

# Looping through babies_df to and filling up gender
gender = []
for i in range(len(babies_df)):
  if babies_df.iloc[i,1]>babies_df.iloc[i,2]:
   gender.append('F')
  else:
   gender.append('M')
# Adding a gender column to babies_df
babies_df['gender']=gender
#babies_df.iloc[0]
# Printing out the first few rows of babies_df
babies_df.head()
# This function returns the location of an element in a_list.
# Where an item does not exist, it returns -1.
def l(a_list, element):
    loc_of_name = a_list.index(element) if element in a_list else -1
    return(loc_of_name)

# Looping through author_df['nysiis_name'] and appending the gender of each
# author to author_gender.
author_gender = []
for name in author_df['nysiis_name']:
    k=l(list(babies_df['babynysiis']),name)
    if(k!=-1):
        author_gender.append(babies_df.iloc[k,3])
    else:
        author_gender.append('Unknown') 

# Adding author_gender to the author_df
author_df['author_gender']=author_gender

# Counting the author's genders
author_df['author_gender'].value_counts()
author_df.head()
# Creating a list of unique years, sorted in ascending order.
years = [2008,2009,2010,2011]

# Initializing lists
males = []
females= []
unknown = []

# Looping through years to find the number of male, female and unknown authors per year
for y in years:
   females.append(len(author_df[(author_df["author_gender"] == 'F') &(author_df['Year']==y) ])) 
   males.append(len(author_df[(author_df["author_gender"] == 'M') &(author_df['Year']==y) ])) 
   unknown.append(len(author_df[(author_df["author_gender"] == 'Unknown') &(author_df['Year']==y) ])) 

# Printing out yearly values to examine changes over time
for i in range(len(years)):
    print(years[i],females[i],males[i],unknown[i])
# Importing matplotlib
import matplotlib.pyplot as plt

# This makes plots appear in the notebook
%matplotlib inline

# Plotting the bar chart
plt.bar(years,unknown)

# [OPTIONAL] - Setting a title, and axes labels
# ...YOUR CODE FOR TASK 7...

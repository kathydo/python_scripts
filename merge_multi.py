'''
Processes multiple csv files in directory and then writes into one excel files as different sheets
'''

import pandas as pd
import os
import csv
import glob 
import IPython

path = "[path to folder containing all the csv]"

os.chdir(path)

all_files = sorted(glob.glob("*.csv"))

print(os.path)
print(path)
print("Processing this many files: " + str(len(all_files)))

# Pull project group names into variable
groups_list = [os.path.splitext(item)[0] for item in all_files]

# Take the group names taken from the filenanes above and writes into a txt file
with open('groups_ordered_list.txt', 'w') as f:
    for item in groups_list:
        f.write("%s\n" % item)

# declare writer for a single excel file
writer = pd.ExcelWriter('group_back_up.xlsx', engine='xlsxwriter')

# convert csv to pandas dataframe
df_from_each_file = (pd.read_csv(f) for f in all_files)

# loop and write dataframe into file on different sheets
for idx, df in enumerate(df_from_each_file):
    df.to_excel(writer, sheet_name='groupid_{0}'.format(idx))

# Save excel
writer.save()
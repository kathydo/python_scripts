import pandas
import re
import glob
import IPython
import json

'''
This is a python script that will convert multiple CSV files of the same structure to JSON format
'''

# Scrub data so there is no white space before and after string, and only one space between words
def clean(x):
    x = " ".join(x.split())
    return x

if __name__ == "__main__":
    print("Processing Groups!")

    export_folder = "[insert path to folder containing csv files]"
    path = export_folder + '/*.csv'
    fileExports = glob.glob(path)

    # Uncomment for projectID dictionary
    projectID = {
        "project A" : "[unique objectID as String]",
        "project B" : "[unique objectID as String]",
    }

    li = []

    # go through each file in folder and add to list
    for fname in fileExports:
        # read in csv file and store in pandas data frame
        result = pandas.read_csv(fname)

        # extract name of project group from file name
        groupName = re.search(r'/Users/kdo/Documents/csv_exports/(.*?).csv',fname)
        groupName = groupName.group(1)

        # clean data
        cleaned = result['Name'].apply(clean)

        # Start JSON file and set fields
        data = {}
        data["_schemaName"] = "Group"
        data['name'] = groupName
        data['members'] = list(cleaned)

        # Look up projectID by name from dictionary
        for x in projectID:
            if( re.search( x , groupName )):
                 data["project"] = projectID[x]

        li.append(data)

    # after adding all elements to list, convert to JSON
    y = json.dumps(li, indent = 4)

    print(y)

    # write contents out to file
    with open('newGroups.json', 'w') as outfile:
        json.dump(li, outfile, indent = 4)

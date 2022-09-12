import pandas as pd

# given this type of data
mydata = {'person1':{'Name':'Guy1 Boy',
            'Sex':'Male',
            'Age':20,
            'Patners':1,
            'Children':2,
            'ChildName':['Buba','Dick']},
            'person2':{'Name':'Babe2 girl',
            'Sex':'Female',
            'Age':29,
            'Patners':2,
            'Children':4,
            'ChildName':['Joy','Jane','Joke','Jick']}
}
# convert the given data into pandas dataframe
mypd = pd.DataFrame(mydata)
print(mypd)
# refer to a specific field  in the data
df = mypd['person2']['Sex']     # this prints out the sex of person2
print(df)

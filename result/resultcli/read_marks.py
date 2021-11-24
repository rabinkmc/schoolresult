import sys
import os, csv

marksfolder = os.path.join(os.getcwd(),"resultcli/marks")
filepaths = [ os.path.join(marksfolder,file) for file in os.listdir(marksfolder)]
filepaths.sort()

files = []
readers = []
Records = {}
RecordList = []

for i,path in enumerate(filepaths):
    file = open(path,"r", newline='')
    reader = csv.DictReader(file, delimiter=',')
    readers.append(reader)
    files.append(file)

# first field is name, second is the
# marks we are interested in 

#english = readers[1].fieldnames[1] 
for f1,f2,f3,f4,f5,f6 in zip(*readers):
    # names and fields are hardcoded also the subject are not extensible
    english=float(f2['english'])
    maths  =float(f3['maths'])
    nepali =float(f4['nepali']) 
    science=float(f5['science'])
    social =float(f6['social'])

    info  = {'name': f1['name'],
            'rollno': f1['rollno'],
            'english':english, 
            'maths':maths,  
            'nepali':nepali, 
            'science':science,
            'social':social 
            }
    sub = [ english, maths, nepali, science, social ] 
    info['total']  = sum(sub)

    fail = any(marks < 32 for marks in sub)

    info['percentage'] = '*' if fail else sum(sub)/len(sub)

    Records[f1['name']] = info
    RecordList.append(info)


with open('output.csv', 'w', newline='') as  csvfile:
    fieldnames = ['name', 'rollno', 'english', 'maths', 'nepali', \
    'science', 'social', 'total', 'percentage']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(RecordList)
    
for file in files:
    file.close()



import csv

def read_csv(file):
    with open(file,"r",newline='') as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        filedict = {}
        key_column,value_column = fields[0],fields[1]

        for row in reader:
            key = row[key_column]
            value = round(float(row[value_column]), 2)
            filedict.update({key:value})

        return filedict
            



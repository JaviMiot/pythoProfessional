""" Una funcion que lea archivos csv y que te devuelva
en diccionario con el campo en mayusculas 
    """


import csv

def upper_by(option):
    def upper(func):
        def wrapper(*args, **kwargs):
            datas = func(*args, **kwargs)
            for  data in datas:
                data[option] = data[option].upper()
            return datas
        return wrapper
    return upper



@upper_by('firstName')
@upper_by('lastName')
def readCsv(filename, fields):
    with open(filename, newline='') as csvfile:
        read = csv.DictReader(
            csvfile,
            fieldnames=fields,
        )

        listData =  [data for data in read]
    return listData


data = readCsv('./data.csv',
        ('id', 'firstName',
         'lastName', 'email',
         'profession')
        )

print(data)
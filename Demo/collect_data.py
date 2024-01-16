import JSON_convertor as JDC

fin = open('Name_ID_gen.txt', 'r')
DATA = dict()
for line in fin.readlines():
    line = line.split()
    ID = line[0]
    Name = line[1] + ' ' + line[2]
    if ID not in DATA:
        DATA[ID] = dict()
    DATA[ID]['Name'] = Name.strip()
    DATA[ID]['score'] = 60.0
    DATA[ID]['ROOM'] = '301'
    DATA[ID]['Faculty'] = 'Chulalongkorn'
fin.close()
JDC.Dict2JSON(DATA, 'DATA.json')

DATA2 = JDC.JSON2Dict('DATA.json')
print(DATA2)

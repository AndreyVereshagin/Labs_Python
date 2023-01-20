import json
from Tableware import Tableware
from Fork import Fork
from Knife import Knife
from Pan import Pan
from Plate import Plate
from Pot import Pot
from Spoon import Spoon

def write(data):
    jsonstr = json.dumps(ensure_ascii=False, obj=data, indent=4)
    open('output.json', 'w').write(jsonstr)


def read_from_json():
    return json.load(open('output.json', 'r'))

if __name__ == '__main__':
    knife = Knife('Samura', True, 'big', 'silver')
    fork = Fork('Potrat', True, 'big', 'silver')
    spoon = Spoon('Lofolop', False, 'small', 'silver')
    plate = Plate(18, 2, 'MyHouse', False, 'big', 'ceramics')
    pot = Pot(25, 20, 'Exted', False, 'big', 'steel')
    pan = Pan(20, 4, 'OverCook', False, 'small', 'steel')
    Tablewares = [knife, fork, spoon, plate, pot, pan]
    data = {
        'amount': len(Tablewares),
        'obj': []
    }
    for elem in Tablewares:
        data['obj'].append(elem.__dict__)

    write(data)
    data.clear()
    Tablewares.clear()
    data = read_from_json()

    for elem in data['obj']:
        if elem['name'] == "Knife":
            obj = Knife(elem['brand'], elem['sharpness'], elem['size'], elem['material'])
        elif elem['name'] == "Fork":
            obj = Fork(elem['brand'], elem['sharpness'], elem['size'], elem['material'])
        elif elem['name'] == "Spoon":
            obj = Spoon(elem['brand'], elem['sharpness'], elem['size'], elem['material'])
        elif elem['name'] == "Plate":
            obj = Plate(elem['D'], elem['H'], elem['brand'], elem['sharpness'], elem['size'], elem['material'])
        elif elem['name'] == "Pot":
            obj = Pot(elem['D'], elem['H'], elem['brand'], elem['sharpness'], elem['size'], elem['material'])
        elif elem['name'] == "Pan":
            obj = Pan(elem['D'], elem['H'], elem['brand'], elem['sharpness'], elem['size'], elem['material'])
        Tablewares.append(obj)

    f = open("output.txt", 'w')
    try:
        for elem in Tablewares:
            f.write(elem.Volume()+'\n')
    finally:
        f.close()

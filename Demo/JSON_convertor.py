import json
# ------------------------------------------ #
def Dict2JSON(D, Filename):
    fout = open(Filename, "w")
    json.dump(D, fout, ensure_ascii = False, indent = 4)
    fout.close()
    return
# ------------------------------------------ #
def JSON2Dict(Filename):
    fin = open(Filename, "r")
    json_string = ''
    for d in fin.readlines():
        json_string += d.strip()
    D = json.loads(json_string)
    fin.close()
    return D
# ------------------------------------------ #
def class2json(C, filename):
    fout = open(filename, 'w'):
    fout.write(json.dump(C.__dict__, fout, ensure_ascii = False, indent = 4))
    fout.close()
    return
# ------------------------------------------ #

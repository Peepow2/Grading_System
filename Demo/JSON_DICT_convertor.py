import json
# ------------------------------------------ #
def Dict2JSON(D, Filename):
    fout = open(Filename, "w")
    json.dump(D, fout)
    fout.close()
    return
# ------------------------------------------ #
def JSON2Dict(Filename):
    fin = open(Filename, "r")
    D = json.loads(fin.readline())
    fin.close()
    return D
# ------------------------------------------ #

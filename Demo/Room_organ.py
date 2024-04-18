def Room_organization(Seq_Name): 
    Special_Room = 2
    NO_ROOM = 8
    Per_Room = (len(Seq_Name) // NO_ROOM) + int((len(Seq_Name) % NO_ROOM) != 0)
    ROOM = dict()
    NNR = "204 Priest,205 Bard,206 Archer,301 Scorcerer,304 Warlock,306 Rogue,404 Druid,409 Barbarian"
    Number_Name_Room = [tuple(e.strip().split()) for e in NNR.split(',')]
    
    for e in Number_Name_Room:
        ROOM[e[0]] = list()
    
    for i in range(len(Seq_Name)):
        if i < (Per_Room * Special_Room):
            ROOM[Number_Name_Room[i % Special_Room][0]].append(Seq_Name[i])
        else:
            ROOM[Number_Name_Room[(i % (8 - Special_Room)) + Special_Room][0]].append(Seq_Name[i])
            
    for line in ROOM:
        print(line)
        print(ROOM[line])
# ------------------------------------------------------------------------- #
Seq_Name = [('00' + str(e))[-3::] for e in range(1, 35)]
Room_organization(Seq_Name)

# ------------------------------------------------------------------------- #
Seq_Name = [('00' + str(e))[-3::] for e in range(1, 270)]
Room_organization(Seq_Name)

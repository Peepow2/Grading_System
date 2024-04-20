import random
def Room_organization(Seq_Name): 
    Special_Room = 2
    NO_ROOM = 8
    Per_Room = (len(Seq_Name) // NO_ROOM) + int((len(Seq_Name) % NO_ROOM) != 0)
    ROOM = dict()
    RN = "204,Priest,205,Bard,206,Archer,301,Scorcerer,304,Warlock,306,Rogue,404,Druid,409,Barbarian".split(',')
    seq = [int(i) for i in range(8)]
    random.shuffle(seq)

    for i in range(1, len(RN), 2):
        ROOM[RN[i]] = list()        # RN[i] = room_namee
    
    for i in range(len(Seq_Name)):
        if i < (Per_Room * Special_Room):
            idx = seq[i % Special_Room]
        else:
            idx = seq[(i % (8 - Special_Room)) + Special_Room]
        r = RN[2*idx + 1]
        ROOM[r].append(Seq_Name[i])
    
    fout = open("List_ROOM.txt", 'w')
    for room_name in ROOM:
        room_num = RN[RN.index(room_name) - 1]
        print(room_name, (9 - len(room_name)) * ' ' , \
             '(' + room_num + ')', '-->', ROOM[room_name])
        
        fout.write(room_name + (9 - len(room_name)) * ' ' + \
             ' (' + room_num + ')' + ' --> ' + str(ROOM[room_name]) + '\n')
    fout.close()
    return
# ------------------------------------------------------------------------- #
Seq_Name = [('00' + str(e+1))[-3::] for e in range(264)]
Room_organization(Seq_Name)

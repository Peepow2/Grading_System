import random
def Room_organization(Seq_Name): 
    Special_Room = 2
    NO_ROOM = 8
    Per_Room = (len(Seq_Name) // NO_ROOM) + int((len(Seq_Name) % NO_ROOM) != 0)
    ROOM = dict()
    NR = "204,Priest,205,Bard,206,Archer,301,Scorcerer,304,Warlock,306,Rogue,404,Druid,409,Barbarian".split(',')
    List_NR = [tuple([NR[i], NR[i+1]]) for i in range(0,len(NR),2)]
    seq = [int(i) for i in range(8)]
    random.shuffle(seq)

    for e in List_NR:
        ROOM[e[1]] = list()
    
    for i in range(len(Seq_Name)):
        if i < (Per_Room * Special_Room):
            idx = seq[i % Special_Room]
        else:
            idx = seq[(i % (8 - Special_Room)) + Special_Room]
        e = List_NR[idx][1]
        ROOM[e].append(Seq_Name[i])
    
    fin = open("List_ROOM.txt", 'w')
    for room_nam in ROOM:
        room_num = NR[NR.index(room_nam) - 1]
        print(room_nam, (9 - len(room_nam)) * ' ' , \
             '(' + room_num + ')', '-->', ROOM[room_nam])
    fin.close()
    return
# ------------------------------------------------------------------------- #
Seq_Name = [('00' + str(e+1))[-3::] for e in range(8*15)]
Room_organization(Seq_Name)

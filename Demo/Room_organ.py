def Room_organization(Seq_Name): 
    Special_Room = 2
    NO_ROOM = 8
    Per_Room = (len(Seq_Name) // NO_ROOM) + int((len(Seq_Name) % NO_ROOM) != 0)
    ROOM = [list() for i in range(NO_ROOM)]

    Room_Name = ['King', 'Queen', 'J', 'A', '10', '9', '8', '7']
    Number_Room = '205 206 207 208 201 202 203 204'.split()
    Seq_Room = [int(e) for e in range(Special_Room + 1, 9)]

    for i in range(len(Seq_Name)):
        if i < (Per_Room * Special_Room):
            ROOM[i % Special_Room].append(Seq_Name[i])
        else:
            ROOM[Seq_Room[i % (8 - Special_Room)] - 1].append(Seq_Name[i])

    fout = open('List_ROOM.txt', 'w')
    for i in range(len(ROOM)):
        #print(Number_Room[i], '-->' ,ROOM[i])
        fout.write(str(Number_Room[i]) + ' --> ' + str(ROOM[i]) + '\n')
    fout.close()
    return
# ------------------------------------------------------------------------- #
Seq_Name = [('00' + str(e))[-3::] for e in range(1, 270)]
Room_organization(Seq_Name)
"""Generates data comparable to real data."""
import random

date1 = 'Mon May 18 2020'
date2 = 'Tue May 19 2020'
date3 = 'Wed May 20 2020'
date4 = 'Thr May 21 2020'
date5 = 'Fri May 22 2020'
date6 = 'Sat May 23 2020'
date7 = 'Sun May 24 2020'

#num of tweets per day between 0 - 200
#COVIDnum = 150
#CORONAVIRUSnum = 150
#PANDEMICnum = 150
#num of duplicate IDS



def gen_info(date, COVnum, RONnum, PNDnum, dups):
    """Creates a weeks worth of fake data to test on.
    Args:
        date: the date
        COVnum: how many times covid was tweeted
        RONnum: how many times coronavirus was tweeted
        PNDnum: how many times pandemic was tweetet
        dups:  how many duplicate tweet IDs for that day
    Returns:
        COVID.csv : csv w covid info
        CORONA.csv: csv w coronavirus info
        PANDEMIC.csv: csv with pandemic info
    """
    #111 for Covid, 112 for coronavirus, 113 for pandemic
    #12 for day of the week
    COVtweetID = 1710000000000000000
    RONtweetID = 1720000000000000000
    PNDtweetID = 1730000000000000000

    DUPID = 9999999999999999000
#dup data
    for i in range(dups):
        num = random.randint(1,99)
        ID = DUPID + num
        info = date + ',' + str(ID)
        saveData = open('COVID.csv', 'a')
        saveData.write(info)
        saveData.write('\n')
        saveData.close()

        saveData = open('CORONA.csv', 'a')
        saveData.write(info)
        saveData.write('\n')
        saveData.close()

        saveData = open('PANDEMIC.csv', 'a')
        saveData.write(info)
        saveData.write('\n')
        saveData.close()

#maindata
    for info in range(COVnum):
        info = date + ',' + str(COVtweetID)
        #print(info)
        saveData = open('COVID.csv', 'a')
        saveData.write(info)
        saveData.write('\n')
        COVtweetID += 1
        saveData.close()

    for info in range(RONnum):
        info = date + ',' + str(RONtweetID)
        #print(info)
        saveData = open('CORONA.csv', 'a')
        saveData.write(info)
        saveData.write('\n')
        RONtweetID += 1
        saveData.close()

    for info in range(PNDnum):
        info = date + ',' + str(PNDtweetID)
        #print(info)
        saveData = open('PANDEMIC.csv', 'a')
        saveData.write(info)
        saveData.write('\n')
        PNDtweetID += 1
        saveData.close()

#gen_info(date1, 173, 159, 147, 2)
#gen_info(date2, 161, 168, 162, 4)
#gen_info(date3, 167, 175, 179, 12)
#gen_info(date4, 154, 161, 183, 8)
#gen_info(date5, 171, 155, 152, 6)
#gen_info(date6, 183, 173, 185, 12)
#gen_info(date7, 159, 177, 163, 8)

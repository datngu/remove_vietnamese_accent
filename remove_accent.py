#!/usr/bin/python
import sys
import re
import os
from unidecode import unidecode

#os.chdir("/Users/datn/GDrive/Data/DiaB/Data")
#os.getcwd()

def remove_accent_csv(in_fn):
    base_dir = os.path.dirname(in_fn)
    base_in_fn = os.path.basename(in_fn)
    in_file = open(in_fn, 'r')
    out_fn = base_dir + "/removed_accent_" + base_in_fn
    out_file = open(out_fn, 'w')
    count = 0
    while True:
        count += 1
        # Get next line from file
        line = in_file.readline() 
        # if line is empty
        # end of file is reached
        if not line:
            break
        #tem = no_accent_vietnamese(line)
        tem = unidecode(line)
        out_file.writelines((tem))
    in_file.close()
    out_file.close()

# run function
#remove_accent_csv(sys.argv[1])
remove_accent_csv("/Users/datn/GDrive/Data/DiaB/Data/Coaching_pilot/Pilot_Coaching_RawData_1.Glucose.csv")
remove_accent_csv("/Users/datn/GDrive/Data/DiaB/Data/Coaching_pilot/Pilot_Coaching_RawData_2.HuyetAP.csv")
remove_accent_csv("/Users/datn/GDrive/Data/DiaB/Data/Coaching_pilot/Pilot_Coaching_RawData_5.CanNang.csv")
remove_accent_csv("/Users/datn/GDrive/Data/DiaB/Data/Coaching_pilot/Pilot_Coaching_RawData_7.HbA1C.csv")
remove_accent_csv("/Users/datn/GDrive/Data/DiaB/Data/Coaching_pilot/Pilot_Coaching Data_KQKS.csv")
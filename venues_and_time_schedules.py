#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 12:21:04 2024

@author: NRonoh
"""
import pandas as pd
import random
import numpy as np


ROOMS =['AH1', 'LR3', 'DC', 'SL1', 'SR3', 'SR18', 'SR22', 'CR-SC','PG-ROOM', 'LH2', 'DO','FL','FL1']
WEEK_DAYS = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday']
LABS = ['BOT-LAB', 'COM-LAB', 'CHE-LAB', 'PHY-LAB (SL2)','ZOO-LAB', 'NEM-LAB (SR2)']
TIMES = ['7.00AM-8.00AM','8.00AM-9.00AM', '9.00AM-10.00AM', '10.00AM-11.00AM', '11.00AM-12.00PM','12.00PM-1.00PM',
               '1.00PM-2.00PM', '2.00PM-3.00PM', '3.00PM-4.00PM', '4.00PM-5.00PM', '5.00PM-6.00PM','6.00PM-7.00PM']

# create dictionaries
room_data = [{room:['']+['-' for time in TIMES]} for room in ROOMS]
lab_data = [{lab:['']+['-' for time in TIMES]} for lab in LABS]


#merge dictionaries
merged_room_dict = room_data[0].copy()
for dict_ in room_data[0:]:
    for key, value in dict_.items():
        merged_room_dict[key] = value    
        
def merge_listed_dicts(dict_list):
    merged_dict = dict_list[0].copy()
    for dict_ in dict_list[0:]:
        for key, value in dict_.items():
            merged_dict[key] = value
    return merged_dict  
        
# merged_room_dict        
merged_room_dict = merge_listed_dicts(room_data+lab_data)

[mon_dict, tue_dict, wed_dict, thu_dict, fri_dict] = [merged_room_dict for i in range(5)]

mon_room_df = pd.DataFrame(mon_dict,index=['MONDAY']+TIMES)
tue_room_df = pd.DataFrame(tue_dict,index=['TUESDAY']+TIMES)
wed_room_df = pd.DataFrame(wed_dict,index=['WEDNESDAY']+TIMES)
thu_room_df = pd.DataFrame(thu_dict,index=['THURSDAY']+TIMES)
fri_room_df = pd.DataFrame(fri_dict,index=['FRIDAY']+TIMES)

room_dfs = [mon_room_df, tue_room_df, wed_room_df, thu_room_df,fri_room_df]

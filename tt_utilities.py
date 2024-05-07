#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 12:21:04 2024

@author: NRonoh
"""
import pandas as pd
import random
import numpy as np

from venues_and_time_schedules import (ROOMS, 
                                       LABS, 
                                       TIMES, 
                                       merged_room_dict, 
                                       mon_room_df,
                                       tue_room_df, 
                                       wed_room_df,
                                       thu_room_df,
                                       fri_room_df
                                      )

# Insert column
def insert_room(df_room=mon_room_df, column_idx=3, 
                room_name="BIO-LAB", courses=["BIO 111", "BIO 312",
                                              "BIO 413","-","-","-",
                                              "-", "-","-", "-", "-"] 
               ):
    return df_room.insert(column_idx,room_name,courses)

# Select Single Row by Index
def select_single_row_by_index(df_room=mon_room_df,
                               idx=1):
    return df_room.iloc[idx]

# Select Single Row by name
def select_single_row_by_name(df_room=mon_room_df,
                              name="7.00AM-8.00AM"):
    return df_room.loc[name]

# Select Single Column by Index
def select_single_column_by_name(df_room=mon_room_df,
                              idx=1):
    return df_room.iloc[:, idx]

# Select Multiple Rows by Index
def select_multiple_rows_by_name(df_room=mon_room_df,
                              idx1=1, idx2=2):
    return df_room.iloc[[idx1,idx2]]

# Select Multiple Columns by Index
def select_multiple_columns_by_index(df_room=mon_room_df,
                              idx1=1, idx2=2, idx3=3 ):
    return df_room.iloc[:, [idx1,idx2,idx3]]

# Select Multiple Columns by Index
def select_multiple_columns_by_name(df_room=mon_room_df,
                              room_1="BOT-LAB", room_2="DC"):
    return df_room.loc[:,[room_1, room_2]]


# Assign Multiple Rows by Index
def assign_multiple_rows_by_index(df_room=mon_room_df,
                              idx1=1, idx2=2, assignment='MAT 001' ):
    df_rooms.iloc[[idx1,idx2]]= assignment
    return df_rooms.iloc[[idx1,idx2]]

# Assign Multiple Rows by Index
def assign_multiple_rows_by_name(df_room=mon_room_df, column="BOT-LAB",
                              row_1="9.00AM-10.00AM", row_2="11.00AM-12.00PM", 
                                 assignment='MAT 001'):
    df_room.loc[[row_1,row_2], [column]]=assignment
    return df_room.loc[[row_1,row_2], [column]]


# exclude_clashes
def exclude_clashing_indices(A = [2,6,8,9,1], B = [9,1]):
    C = []
    for item in A:
        if item not in B:
            C.append(item)
    return C




## References
# https://sparkbyexamples.com/pandas/pandas-iloc-usage-with-examples/
# https://sparkbyexamples.com/pandas/pandas-difference-between-loc-vs-iloc-in-dataframe/


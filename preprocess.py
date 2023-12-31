# _*_ coding: utf-8 _*_
"""
@Author: Crawler
@Time  : 2021/7/9 19:56
@FileName: deal_data.py
@Github: https://github.com/C-rawler
"""
import os
import pandas as pd
import numpy as np
import gc
path = './train/'
path1 = './new_train/'


def reduce_mem(df):
    start_mem = df.memory_usage().sum() / 1024 ** 2
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
    end_mem = df.memory_usage().sum() / 1024 ** 2
    print('{:.2f} Mb, {:.2f} Mb ({:.2f} %)'.format(start_mem, end_mem, 100 * (start_mem - end_mem) / start_mem))
    gc.collect()
    return df


for i in os.listdir(path):
    file = path + i
    data = pd.read_csv(file)
    data.columns = ['time', 'gun_no', 'W_Error', 'C_Cylinder_force', 'C_Differential_pressure', 'W_Friction',
                     'W_Maximum_aperture', 'W_Maximum_electrode_force', 'W_Start_friction', 'W_us2',
                     'W_Welding_point_count', 'W_position_count', 'area', 'in_Counterbalance_pressure',
                     'in_Electrode_force', 'in_Electrode_position', 'in_Sheet_thickness',
                     'in_Velocity', 'in_force_build_up', 'out_Cap_offset', 'out_Electrode_force',
                     'out_Electrode_position', 'out_force_build_up']
    data = reduce_mem(data)
    print(i.split('.')[0])
    data.to_pickle(path1 + i.split('.')[0] + '.pkl')
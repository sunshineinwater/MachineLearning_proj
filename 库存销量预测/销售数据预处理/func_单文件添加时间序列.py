import numpy as np;
import pandas as pd;

import 库存销量预测.样本时间序列处理库.时分秒_int数组_批量转化为字符串 as sts;


def process_datafile(datatime, read_file, write_file):
    '''
    读取csv数据
    '''
    fopen = open(read_file, encoding='UTF-8');
    data = pd.read_csv(fopen);
    '''
    时间格式处理
    '''
    arr = np.asarray(data['pay_time']);  # pay_time转化为numpy格式
    dts = sts.shift_time(datatime, arr);  # 时间格式转化为字符串
    bills_time = pd.to_datetime(dts);  # 订单时间批量转化为datetime格式
    # for i in range(10): print(bills_time[i],arr[i])  #测试转化过程中，顺序是否保持不变
    '''
    样本数据添加时间序列
    '''
    print(len(bills_time), len(data.index))
    data.index = bills_time
    data.to_csv(write_file, encoding='UTF-8')
    return data;
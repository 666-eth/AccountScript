import pandas as pd
import random
import time
import numpy as np

# Task Tags 生成脚本，根据输入的CSV文件，生成新的taskTags并保存为新的CSV文件

account_path = '/Users/lishuai/Documents/crypto/bockchainbot/AccountScript/output/carv.csv'
output_path = '/Users/lishuai/Documents/crypto/bockchainbot/AccountScript/output/all_tasks.csv'
tasks = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36]


df = pd.read_csv(account_path)

# 遍历DF以生成新的taskTags
new_task_data = pd.DataFrame()
for index, row in df.iterrows():
    shuffled_tasks = np.random.permutation(tasks)
    row['tasks'] = list(shuffled_tasks)
    new_task_data = pd.concat([new_task_data, pd.DataFrame(row).transpose()])

all_task_data = pd.DataFrame()
for i in range(len(tasks)):
    new_task_data = new_task_data.sample(frac=1)
    for index, row in new_task_data.iterrows():
        row['taskTag'] = str(row['tasks'][i])
        all_task_data = pd.concat([all_task_data, pd.DataFrame(row).transpose()])
del all_task_data['tasks']
all_task_data.to_csv(output_path, index=False)
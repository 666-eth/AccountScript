import pandas as pd
import random
import numpy as np

# 导入配置文件中的参数
import config

# 使用Pandas打开CSV文件，并根据开始行数和结束行数读取部分数据
df = pd.read_csv(config.input_file, skiprows=range(1, config.start_row), nrows=config.end_row)

# 使用sample函数对DataFrame进行随机打乱顺序
df_shuffled = df.sample(frac=1, random_state=random.seed())

# 为df_shuffled新增一列名为taskTag的列，生成的随机数需要检查是否在exclude_numbers中
taskTags = []
for _ in range(len(df_shuffled)):
    random_num = np.random.randint(config.lower_bound, config.upper_bound + 1)
    while random_num in config.exclude_numbers:
        random_num = np.random.randint(config.lower_bound, config.upper_bound + 1)
    taskTags.append(random_num)

df_shuffled['taskTag'] = taskTags

# 保存打乱顺序后的DataFrame为新的CSV文件
df_shuffled.to_csv(config.output_file, index=False)

print("已生成打乱顺序的CSV文件:", config.output_file)

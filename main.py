import pandas as pd
import random
import numpy as np

# 导入配置文件中的参数
import config

# 使用Pandas打开CSV文件，并根据开始行数和结束行数读取部分数据
df = pd.read_csv(config.input_file, skiprows=range(1, config.start_row), nrows=config.end_row)

# 初始化一个用于保存新taskTag的列表
new_taskTags = []

# 遍历DataFrame以生成新的taskTags
for index, row in df.iterrows():
    old_taskTag = row['taskTag']
    random_num = np.random.randint(config.lower_bound, config.upper_bound + 1)
    
    # 检查新生成的random_num是否与旧的taskTag或exclude_numbers相同
    while random_num == old_taskTag or random_num in config.exclude_numbers:
        random_num = np.random.randint(config.lower_bound, config.upper_bound + 1)
    
    new_taskTags.append(random_num)

# 将新生成的taskTags赋值给DataFrame的taskTag列
df['taskTag'] = new_taskTags

# 使用sample函数对DataFrame进行随机打乱顺序
df_shuffled = df.sample(frac=1, random_state=random.seed())

# 保存打乱顺序后的DataFrame为新的CSV文件
df_shuffled.to_csv(config.output_file, index=False)

print("已生成打乱顺序的CSV文件:", config.output_file)

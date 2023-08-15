import pandas as pd
import random
import numpy as np

# 指定输入和输出的文件名
input_file = 'input.csv'
output_file = 'output.csv'
start_row = 0  # 开始行数（包含）
end_row = None  # 结束行数（不包含）

# 设置随机整数的上限和下限
lower_bound = 10  # 这里设置为10，你可以根据需要调整
upper_bound = 100  # 这里设置为100，你可以根据需要调整

# 使用Pandas打开CSV文件，并根据开始行数和结束行数读取部分数据
df = pd.read_csv(input_file, skiprows=range(1, start_row), nrows=end_row)

# 使用sample函数对DataFrame进行随机打乱顺序
df_shuffled = df.sample(frac=1, random_state=random.seed())

# 为df_shuffled新增一列名为taskTag的列，其中的值为lower_bound至upper_bound的随机整数
df_shuffled['taskTag'] = np.random.randint(lower_bound, upper_bound + 1, size=len(df_shuffled))

# 保存打乱顺序后的DataFrame为新的CSV文件
df_shuffled.to_csv(output_file, index=False)

print("已生成打乱顺序的CSV文件:", output_file)

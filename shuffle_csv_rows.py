# 随机打乱钱包顺序脚本


import pandas as pd
import random

# 指定输入和输出的文件名
input_file = 'input.csv'
output_file = 'output.csv'
start_row = 0  # 开始行数（包含）
end_row = None  # 结束行数（不包含）

# 使用Pandas打开CSV文件，并根据开始行数和结束行数读取部分数据
df = pd.read_csv(input_file, skiprows=range(1, start_row), nrows=end_row)

# 使用sample函数对DataFrame进行随机打乱顺序
df_shuffled = df.sample(frac=1, random_state=random.seed())

# 保存打乱顺序后的DataFrame为新的CSV文件
df_shuffled.to_csv(output_file, index=False)

print("已生成打乱顺序的CSV文件:", output_file)

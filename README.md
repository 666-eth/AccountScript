# AccountScript

# 环境安装配置
## 安装 Anaconda
1. 首先，前往 Anaconda 官方网站的下载页面：https://www.anaconda.com/products/distribution
2. 选择 macOS 下的下载选项，下载相应的 Anaconda 安装包。
3. 打开下载的 .pkg 文件并遵循安装提示。
4. 安装完成后，可以在终端中输入 conda 检查是否成功安装
   
## 在 VSCode 中配置 Anaconda
1. 打开 VSCode。
2. 安装 Python 扩展。在左侧的扩展面板中（或使用快捷键 Cmd+Shift+X），搜索 “Python” 并安装由 Microsoft 提供的 Python 扩展。
3. 重启 VSCode。
4. 当你打开一个 Python 文件或开始一个新的 Python 项目时，VSCode 应该能够自动识别 Anaconda 中的 Python 解释器。如果没有，你可以手动选择解释器：
    1. 打开命令面板（Cmd+Shift+P）。
    2. 输入 “Python: Select Interpreter” 并选择这个命令。
    3. 从弹出的列表中选择一个 Anaconda 环境。

## 安装pandas库
1. 在终端中输入命令`pip instal pandas` 安装pandas库

# 程序运行
## 程序配置
1. 在config.py文件中配置参数：
    ``` python
      # 指定输入和输出的文件名
    input_file = 'input.csv'  # 导入的账户文件目录
    output_file = 'output.csv'  # 随机生成后的账户保存目录
    start_row = 0  # 账户开始行数（包含） 
    end_row = None  # 账户结束行数（不包含）
    
    # 设置随机任务的上限和下限
    lower_bound = 10
    upper_bound = 100
    
    # 设置要排除的数字列表，排除后任务不会在列表中生成
    exclude_numbers = [15, 25, 35]
    
    ```

2. 运行main.py 程序即可生成随机任务。
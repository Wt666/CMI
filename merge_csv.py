import os
import pandas as pd
from tqdm import tqdm

# 设置文件夹路径
folder_path = 'rate'

# 获取文件夹中的所有CSV文件
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]

# 创建一个空的DataFrame，用于存储合并后的数据
merged_data = pd.DataFrame()

# 遍历每个CSV文件并合并数据
for file in tqdm(csv_files):
    file_path = os.path.join(folder_path, file)
    # df = pd.read_csv(file_path)
    df = pd.read_excel(file_path)
    merged_data = merged_data.append(df)
# 将合并后的数据保存为一个新的CSV文件
# merged_data.to_csv('merged_data.csv', index=False, encoding='utf_8_sig')
# merged_data.to_excel('merged_data.xlsx', index=False, encoding='utf_8_sig')


du = merged_data.drop_duplicates('发布时间')
du = du.drop(['Unnamed: 0','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10'],axis=1).dropna()
du = du.sort_values('发布时间')
du.plot('发布时间',['现汇买入价','现汇卖出价'])
du.to_excel('du_merged_data.xlsx', index=False, encoding='utf_8_sig')


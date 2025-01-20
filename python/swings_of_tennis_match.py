import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 读取数据
data = pd.read_csv('G:\MCM_Latex2024\data\Wimbledon_featured_matches.csv')

# 选择特定的比赛
match_id = '2023-wimbledon-1301'
match_data = data[data['match_id'] == match_id]

# 转换时间格式
match_data['elapsed_time'] = pd.to_datetime(match_data['elapsed_time'], format='%H:%M:%S')

# 计算得分差
match_data['score_diff'] = match_data['p1_points_won'] - match_data['p2_points_won']

# 绘制折线图
plt.figure(figsize=(14, 7))

# 绘制折线图，去掉数据点
plt.plot(match_data['elapsed_time'], match_data['score_diff'], label='Score Difference', color='blue', linewidth=2)

# 填充折线图下方的区域，根据得分差的正负值使用不同颜色
plt.fill_between(match_data['elapsed_time'], match_data['score_diff'], where=(match_data['score_diff'] >= 0), 
                 color='lightgreen', alpha=0.5, label='Player1 Leads')
plt.fill_between(match_data['elapsed_time'], match_data['score_diff'], where=(match_data['score_diff'] < 0), 
                 color='lightcoral', alpha=0.5, label='Player2 Leads')

# 美化图表
plt.title(f'Score Difference Over Time - Match {match_id}', fontsize=16, pad=20)
plt.xlabel('Time', fontsize=14)
plt.ylabel('Score Difference (Player1 - Player2)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.xticks(rotation=45)
plt.legend(loc='upper left', fontsize=12)

# 显示图表
plt.tight_layout()
plt.show()
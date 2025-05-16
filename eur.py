import re

# 读取 Eur.m3u 文件
with open('Eur.m3u', 'r', encoding='utf-8') as file:
    m3u_content = file.read()

# 正则表达式，匹配小括号和方括号及其内容并删除
pattern = r'[\(\[].*?[\)\]]'

# 替换内容，删除方括号和小括号内的部分
updated_m3u_content = re.sub(pattern, '', m3u_content)

# 将更新后的内容写入到新的文件 eur.m3u
with open('eur.m3u', 'w', encoding='utf-8') as file:
    file.write(updated_m3u_content)

print("M3U 文件已更新并保存为 eury.m3u")

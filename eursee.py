with open(save_path, 'r', encoding='utf-8') as file:
    m3u_content = file.read()

# 正则表达式用于提取频道名称和播放链接
pattern = re.compile(r'#EXTINF:-1 tvg-logo="([^"]+)"(?: group-title="([^"]+)")?,(.+)\n(.+)')

new_m3u = ['#EXTM3U']  # 新的 M3U 文件内容，先加上 #EXTM3U 头部

# 遍历每一行 M3U 内容
for match in pattern.finditer(m3u_content):
    logo_url = match.group(1)
    group_title = match.group(2) if match.group(2) else "Unknown Category"
    channel_name = match.group(3).strip()  # 去除两边的空格
    stream_url = match.group(4).strip()

    # 进一步去除方括号 [ ] 和小括号 ( ) 以及其中的内容
    channel_name_clean = re.sub(r'\[.*?\]', '', channel_name)  # 移除方括号及其中的内容
    channel_name_clean = re.sub(r'\(.*?\)', '', channel_name_clean)  # 移除小括号及其中的内容
    channel_name_clean = re.sub(r'\s+', ' ', channel_name_clean)  # 去除多余的空格

    # 调试：打印处理后的频道名称
    print(f"原频道名称: {channel_name}, 处理后的频道名称: {channel_name_clean}")

    # 通过 STATIC_TV_NAMES 字典匹配频道名称并替换
    if channel_name_clean in STATIC_TV_NAMES:
        print(f"匹配到字典名称: {channel_name_clean}")
        channel_name = STATIC_TV_NAMES[channel_name_clean]  # 替换频道名称
    else:
        print(f"未匹配字典名称: {channel_name_clean}")  # 如果未匹配字典，保持原名称

    # 通过 STATIC_CATEGORIES 字典获取相应的分类，避免特殊字符问题
    category = STATIC_CATEGORIES.get(channel_name, "Unknown Category")
    
    # 调试：打印分类信息
    print(f"分类: {category}")

    # 通过 STATIC_LOGOS 字典获取相应的 logo
    logo = STATIC_LOGOS.get(channel_name, logo_url)

    # 调试：打印 logo
    print(f"Logo: {logo}")

    # 生成新的 EXTINF 行
    new_m3u.append(f'#EXTINF:-1 group-title="{category}" tvg-logo="{logo}", {channel_name}')
    new_m3u.append(stream_url)

# 输出新生成的 M3U 内容
new_m3u_content = "\n".join(new_m3u)

# 保存到文件
new_m3u_path = os.path.join(os.getcwd(), 'Eur.m3u')
with open(new_m3u_path, 'w', encoding='utf-8') as f:
    f.write(new_m3u_content)

print(f"新生成的 M3U 文件已保存为 {new_m3u_path}")

import os
import re
import subprocess

# 下载 M3U 文件
url = "https://raw.githubusercontent.com/hemzaberkane/ARAB-IPTV/refs/heads/main/ARABIPTV.m3u"
save_path = "ara.m3u"

# 使用 curl 下载文件
curl_command = f"curl -o {save_path} {url}"
try:
    subprocess.run(curl_command, shell=True, check=True)
    print(f"成功下载 M3U 文件并保存为 {save_path}")
except subprocess.CalledProcessError as e:
    print(f"下载失败，错误信息: {e}")
    exit()

# 读取下载的 M3U 文件内容
with open(save_path, 'r', encoding='utf-8') as file:
    m3u_content = file.read()

# 正则表达式：匹配所有的 #EXTINF:-1 行和其后的播放链接
pattern = re.compile(r'(#EXTINF:-1[^\n]*)(\n)(https?://[^\n]+)')

# 新的 M3U 文件内容，先加上 #EXTM3U 头部
new_m3u = ['#EXTM3U url-tvg="https://raw.githubusercontent.com/iptv-org/epg/master/sites/elcinema.com/elcinema.com_ar.channels.xml"']

# 遍历所有的 #EXTINF:-1 行和播放链接
for match in pattern.finditer(m3u_content):
    extinf_line = match.group(1)  # 获取 #EXTINF:-1 行的内容
    stream_url = match.group(3)   # 获取播放链接

    # 检查是否已经包含了 group-title
    if 'group-title' not in extinf_line:
        # 如果没有 group-title 标签，就加上
        new_extinf_line = extinf_line.replace('#EXTINF:-1', '#EXTINF:-1 group-title="🇦🇪阿拉伯"')
    else:
        # 如果已经包含 group-title 标签，则保留原样
        new_extinf_line = extinf_line
    
    # 将修改后的 #EXTINF:-1 行添加到新 M3U 文件内容中
    new_m3u.append(new_extinf_line)
    
    # 将播放链接添加到新 M3U 文件内容中（确保只添加一次）
    new_m3u.append(stream_url)

# 输出新生成的 M3U 内容
new_m3u_content = "\n".join(new_m3u)

# 保存到文件
new_m3u_path = os.path.join(os.getcwd(), 'ARAB.m3u')
with open(new_m3u_path, 'w', encoding='utf-8') as f:
    f.write(new_m3u_content)

print(f"新的 M3U 文件已保存为 {new_m3u_path}")

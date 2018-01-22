import md5 as sj

# 获取字符串md5
print(sj.md5("Hello world", mode='S'))

# 获取文件md5
print(sj.md5('./README.md', mode='F'))

# 获取文件sha1
print(sj.sha1('./README.md', mode='F'))


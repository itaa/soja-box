import soja_md5 as sj

# 获取字符串md5
print(sj.get_str_md5("Hello world"))

# 获取文件md5
print(sj.get_file_md5('./README.md'))

# 获取文件sha1
print(sj.get_file_sha1('./README.md'))


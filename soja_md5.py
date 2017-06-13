#!/usr/bin/env python3

import hashlib
import os
import sys


def get_str_md5(string):
    """
    一个字符串的MD5值
    返回一个字符串的MD5值
    """
    m0 = hashlib.md5()
    m0.update(string.encode('utf-8'))
    result = m0.hexdigest()
    return result


def get_big_file_md5(file_name):
    """
    较大文件的MD5值
    返回一个较大文件的MD5值
    """
    if not os.path.isfile(file_name):
        return
    hash_o = hashlib.md5()
    f = open(file_name, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        hash_o.update(b)
    f.close()
    return hash_o.hexdigest()


def get_file_sha1(file_path):
    """
    文件的sha1值
    返回一个文件的sha1值
    """
    with open(file_path, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash_o = sha1obj.hexdigest()
        return hash_o


def get_file_md5(file_path):
    """
    文件的md5值
    返回一个文件的md5值
    """
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash_o = md5obj.hexdigest()
        return hash_o


if __name__ == "__main__":
    if len(sys.argv) == 2:
        hash_file = sys.argv[1]
        if not os.path.exists(hash_file):
            hash_file = os.path.join(os.path.dirname(__file__), hash_file)
            if not os.path.exists(hash_file):
                print("cannot found file")
            else:
                get_file_md5(hash_file)
        else:
            get_file_md5(hash_file)
    else:
        print("no filename")

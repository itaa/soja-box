#!/usr/bin/env python3

import hashlib
import os
import sys


def __get_str_md5(string):
    """
    一个字符串的MD5值
    返回一个字符串的MD5值
    """
    m0 = hashlib.md5()
    m0.update(string.encode('utf-8'))
    result = m0.hexdigest()
    return result


def __get_big_file_md5(file_name):
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


def __get_file_sha1(file_path):
    """
    文件的sha1值
    返回一个文件的sha1值
    """
    with open(file_path, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash_o = sha1obj.hexdigest()
        return hash_o


def __get_file_md5(file_path):
    """
    文件的md5值
    返回一个文件的md5值
    """
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash_o = md5obj.hexdigest()
        return hash_o


def md5(str, mode='S'):
    """
    获取MD5方法
    :param str: 待hash的字符串，或者是文件的路径，
                如果是文件路径的时候需要设置mode='F'
    :param mode: 模式，'S', 获取字符串的MD5
                'F', 传入的str需要是文件的路径
                'B', 大文件的MD5,传入的str需要是文件的路径
    :return: 32位小写hash值
    """
    if mode.upper() == 'S':
        return __get_str_md5(str)
    if mode.upper() == 'F':
        return __get_file_md5(str)
    if mode.upper() == 'B':
        return __get_big_file_md5(str)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        hash_file = sys.argv[1]
        if not os.path.exists(hash_file):
            hash_file = os.path.join(os.path.dirname(__file__), hash_file)
            if not os.path.exists(hash_file):
                print("cannot found file")
            else:
                md5(hash_file, mode='F')
        else:
            md5(hash_file, mode='F')
    else:
        print("no filename")

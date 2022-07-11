# 读取yaml的数据
import json

import yaml


def load_yaml(file):
    files = open(file, 'r', encoding='utf-8')
    # 读取
    data = yaml.load(files, Loader=yaml.FullLoader)
    return data

a = load_yaml('../data/search.yaml')
print(a)
# encoding=utf-8
import json


def save(data, path='e://python/wyjj/wyjj10.json'):
    with open(path, 'w') as json_file:
        json_file.write("[\n")
        for val in data:
            json_file.write(json.dumps(val)+",")
            json_file.write("\n")
        json_file.write("]")


def load(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return data


# 数据清洗脚本1 :消灭年涨幅低于10%的一切基金

if __name__ == "__main__":
    data = load("E:/python/wyjj/wyjj.json")
    result_data = []
    for json_val in data:
        year_increment = json_val['year_increment'][0]
        if year_increment.startswith("-"):
            continue
        if float(year_increment[0:-1]) < 10:
            continue
        else:
            result_data.append(json_val)
    save(result_data)

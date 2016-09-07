# encoding=utf-8
import json


# 该模块用于排序信息


def save(data, path='e://python/wyjj/wyjjrank.json'):
    with open(path, 'a') as json_file:
        json_file.write("[\n")
        for x in range(20):
            json_file.write(json.dumps(data[x]))
            if x != 19:
                json_file.write(",")
            json_file.write("\n")
        json_file.write("]")


def load(path='e://python/wyjj/wyjj10.json'):
    with open(path) as json_file:
        data = json.load(json_file)
        return data


# 快速排序进行排序
def quick_sort(arr, increment):
    if len(arr) <= 1:
        return arr
    pivot = float(arr[len(arr) / 2]['%s' % increment][0][0:-1])

    left = [x for x in arr if float(x['%s' % increment][0][0:-1]) < pivot]
    middle = [x for x in arr if float(x['%s' % increment][0][0:-1]) == pivot]
    right = [x for x in arr if float(x['%s' % increment][0][0:-1]) > pivot]
    return quick_sort(right, increment) + middle + quick_sort(left, increment)


def week_increment(array):
    return quick_sort(temp_array, 'week_increment')


def month_increment(array):
    return quick_sort(temp_array, 'month_increment')


def season_increment(array):
    return quick_sort(temp_array, 'season_increment')


def half_increment(array):
    return quick_sort(temp_array, 'half_increment')


def year_increment(array):
    return quick_sort(temp_array, 'year_increment')


def this_year_increment(array):
    return quick_sort(temp_array, 'this_year_increment')


if __name__ == "__main__":
    temp_array = load()
    week_rank = week_increment(temp_array)[0:20]
    month_rank = month_increment(temp_array)[0:20]
    season_rank = season_increment(temp_array)[0:20]
    half_year_rank = half_increment(temp_array)[0:20]
    year_rank = year_increment(temp_array)[0:20]
    this_year_rank = this_year_increment(temp_array)[0:20]
    save(week_rank, path='e://python/wyjj/weekrank.json')
    save(month_rank, path='e://python/wyjj/monthrank.json')
    save(season_rank, path='e://python/wyjj/seasonrank.json')
    save(half_year_rank, path='e://python/wyjj/halfyearrank.json')
    save(year_rank, path='e://python/wyjj/yearrank.json')
    save(this_year_rank, path='e://python/wyjj/thisyearrank.json')

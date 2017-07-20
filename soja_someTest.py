from datetime import datetime


def how_many_days(other_day='2019-1-1'):
    """
    How many days today to other day.
    :param other_day: some day with string eg.:'2019-1-1'
    :return:
    """
    today_date = datetime.now()
    other_day_date = datetime.strptime(other_day, '%Y-%m-%d')
    date_count = other_day_date - today_date
    return date_count


# 正整数的因数
def factors(integer=30):
    """
    return the integer's factors.
    :param integer: some integer
    :return: factors
    """
    result = []
    for i in range(1, integer + 1):
        if integer % i == 0:
            result.append(i)
    return result


def cal_num(*numbers, **kv):
    """
    :param numbers:
    :param kv:
    :return:
    """
    if 'kind' in kv:
        kind_value = kv.get('kind')

    if 'ignore_max' in kv:
        ignore_max = kv.get('ignore_max')
        if ignore_max:
            numbers = list(sorted(numbers))
            if len(numbers) != 0:
                _ = numbers.pop(-1)
    result = 0

    for i in numbers:
        result += i
    if kind_value == 'sum':
        return result
    if kind_value == 'avg':
        return result / len(numbers)


if __name__ == '__main__':
    print(factors(100))
    print(how_many_days())
    numbers = [1, 3, 5, 7, 9]
    kv = {'kind': 'sum', 'ignore_max': False}
    print(cal_num(*numbers, **kv))



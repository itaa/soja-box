from datetime import datetime


def how_many_days(other_day='2019-1-1'):
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


if __name__ == '__main__':
    print(factors(100))
    print(how_many_days())




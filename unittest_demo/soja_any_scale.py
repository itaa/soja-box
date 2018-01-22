class Scale(object):
    # 常用的字母代表数字的字典
    dic = {'10': 'A',
           '11': 'B',
           '12': 'C',
           '13': 'D',
           '14': 'E',
           '15': 'F'}

    # 将weight进制的某一位的值对应的十进制的值算出来
    @staticmethod
    def place_value(n_value, scale, digits):
        # 某一位的权值,初始为1
        weight = 1
        for i in range(1, digits + 1):
            weight = scale * weight
        return n_value * weight

    # scale进制的值value转为对应10进制的值
    @staticmethod
    def n_2_decimal(value_, scale):
        sum_ = 0
        # 数值的位数长度
        n = len(str(value_))
        for i in range(1, n + 1):
            sum_ = sum_ + Scale.place_value(int(str(value_)[i - 1]), scale, n - i)
        return sum_

    # 10进制的值value转为对应scale进制的值
    @staticmethod
    def decimal_2_n(value_, scale):
        arr = []
        i = 0
        while value_ is not 0:
            rem = value_ % scale
            if rem >= 16:
                rem = "*" + str(rem) + "*"
            elif 10 <= rem <= 15:
                rem = Scale.dic[str(rem)]
            value_ = value_ // scale
            arr.append(rem)
            i += 1
        return arr

    @staticmethod
    def any_scale(scale1_, value_, scale2_):
        mid_value = Scale.n_2_decimal(value_, scale1_)
        fin_value = Scale.decimal_2_n(mid_value, scale2_)
        fin_value.reverse()
        fin_value = ''.join([str(x) for x in fin_value])
        return fin_value

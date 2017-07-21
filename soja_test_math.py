# 将以下脚本保存为 test_mymath.py，并运行

"""
构建unittest基本使用方法
1.import unittest 导入unittest库
2.定义一个继承自unittest.TestCase的测试用例类
3.定义setUp和tearDown，在每个测试用例前后做一些辅助工作
4.定义测试用例，函数名字以test开头
5.一个测试用例应该只测试一个方面，测试目的和测试内容应很明确。主要是调用assertEqual、assertRaises等断言方法判断程序执行结果和预期值是否相符。
6.调用unittest.main()启动测试
7.如果测试未通过，会输出相应的错误提示。如果测试全部通过则不显示任何东西，这时可以添加-v参数显示详细信息。
"""

import soja_math
import unittest


class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = soja_math.add(1, 2)
        self.assertNotEqual(result, 555)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = soja_math.add(10.5, 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = soja_math.add('abc', 'def')
        self.assertEqual(result, 'abcdef')
    def test_sub_int(self):
        """
        Test subtract
        :return:
        """

if __name__ == '__main__':
    unittest.main()




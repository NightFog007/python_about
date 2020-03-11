import unittest
from unittest.mock import patch
import function

class MyTestCase(unittest.TestCase):

    # def test_add_and_multiply(self):
    #     x = 3
    #     y = 5
    #     addition, multiple = function.add_and_multiply(x, y)
    #     self.assertEqual(8, addition)
    #     self.assertEqual(15, multiple)

    @patch("function.multiply")  #装饰器. 指定的对象将被替换为一个模拟（或其他对象），并在测试结束时还原。这里模拟function.py文件中multiply()函数。
    def test_add_and_multiply2(self, mock_multiply):
        x = 3
        y = 5
        mock_multiply.return_value = 15  #mock原来function.py里的multiply()方法返回15
        addition, multiple = function.add_and_multiply(x, y)
        mock_multiply.assert_called_once_with(3, 5)   #确认只被调用一次

        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)


if __name__ == "__main__":
    unittest.main()
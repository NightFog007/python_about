from unittest import mock

# Mock对象就是mock模块中的一个类的实例，这个类的实例可以用来替换其他的Python对象，来达到模拟的效果。


# client = mock.Mock()
# client.v2_client.get.return_value = '200'

# xx = client.v2_client.get()
# print(xx)
from unittest.mock import patch
@patch('module.ClassName2')
@patch('module.ClassName1')
def test(MockClass1, MockClass2):
      module.ClassName1()
      module.ClassName2()
      assert MockClass1 is module.ClassName1
      assert MockClass2 is module.ClassName2
      assert MockClass1.called
      assert MockClass2.called

test()

from unittest.mock import MagicMock

class ProductionClass():
    a=1

thing = ProductionClass()
thing.method = MagicMock(return_value=3)
xx = thing.method(3, 4, 5, key='value')
print(xx)

yy = thing.method.assert_called_with(3, 4, 5, key='value')
print(yy)

a = mock.Mock()(side_effect=KeyError('foo'))
a()
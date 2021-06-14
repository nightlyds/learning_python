import unittest
from unittest.mock import patch, Mock
import functions_mock_module

class TestCalculator(unittest.TestCase):
    @patch('functions_mock_module.sum', return_value=9)
    def test_sum(self, sum):
        print(sum(2, 3)) # Output: 9 | mocked to 9
        self.assertEqual(sum(5, 4), 9)

def mock_sum(a, b):
    # mock sum function without the long running time.sleep
    return a + b

class TestCalculator_2(unittest.TestCase):
    @patch('functions_mock_module.sum', side_effect=mock_sum)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 5)
        self.assertEqual(sum(7,3), 10)

class TestBlog(unittest.TestCase):
    @patch('functions_mock_module.Blog')
    def test_blog_posts(self, MockBlog):
        print(MockBlog) # <MagicMock name='Blog' id='139983058035040'>
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable  end  of the  western  spiral  arm  of  the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response)
        # {'userId': 1, 'id': 1, 'title': 'Test Title',
        # 'body': 'Far out in the uncharted backwaters of the
        # unfashionable  end  of the  western  spiral  arm
        # of  the Galaxy\\ lies a small unregarded yellow sun.'}
        # <class 'dict'>
        print(response[0], dict)
        self.assertIsInstance(response[0], dict)

        # Additional assertions
        assert MockBlog is functions_mock_module.Blog  # The mock is equivalent to the original

        assert MockBlog.called  # The mock was called

        blog.posts.assert_called_with()  # We called the posts method with no arguments

        blog.posts.assert_called_once_with()  # We called the posts method once with no arguments

        # blog.posts.assert_called_with(1, 2, 3) - This assertion is False and will fail since we called blog.posts with no arguments

        blog.reset_mock()  # Reset the mock object

        blog.posts.assert_not_called()  # After resetting, posts has not been called.


# this function takes an object as argument and calls a
# method on it
def function_with_call(some_obj, argument):
    return some_obj.some_method(argument)

class Function_With_Call_Mock(unittest.TestCase):

    def test_called(self):
        mock = Mock()
        mock.some_method = Mock(return_value="CALLED")

        print(function_with_call(mock, "foo bar")) # CALLED | because return_value is set on this

        # will return true if method was called one or more times
        mock.some_method.assert_called()
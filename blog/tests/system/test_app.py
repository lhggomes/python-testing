from unittest import TestCase
from unittest.mock import patch
from blog.app import print_blogs, blogs
from blog.blog import Blog


class AppTest(TestCase):

    @staticmethod
    def non_test_print_logs():
        blog = Blog('Test', 'Test Author')
        blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

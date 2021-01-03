from Blog import app
from unittest import TestCase
from unittest.mock import patch
from Blog.blog import Blog


class AppTest(TestCase):

    @staticmethod
    def non_test_print_logs():
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_print:
            mocked_print.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = Blog('Test', 'Test Author')
        blog.create_post('Test post', 'Test Content')
        app.blogs = {'Test': blog}

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])
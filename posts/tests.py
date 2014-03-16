from django.test import TestCase
from .models import Post

class PostsTest(TestCase):
    
    def test_simple_image_detection(self):
        post_simple = Post(submission={}, parent={},
            comment={'body':'http://i.imgur.com/dssdk23.jpg'})
        post_album = Post(submission={}, parent={},
            comment={'body':'http://imgur.com/dsdk23/'})
        post_combined = Post(submission={}, parent={},
            comment={'body':'(hop)[http://i.imgur.com/dssdk23.jpg]'})

        self.assertTrue(post_simple.is_simple_image_post())
        self.assertFalse(post_album.is_simple_image_post())
        self.assertTrue(post_combined.is_simple_image_post())
        
    def test_parsing(self):
        """Test that each post parse without errors"""
        for post in Post.objects.all():
            post.comment_as_html()  
            post.parent_as_title()

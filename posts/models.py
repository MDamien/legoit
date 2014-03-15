from django.db import models
from django_extensions.db.fields import json

import markdown, re


def parse_comment(text, display_images=False):
    html = markdown.markdown(text, safe_mode='remove')
    if display_images:
        html = re.sub(r"(http://i\.imgur\.com/[a-zA-Z0-9]*\.jpg)",
            r"<img class='inline_image img-thumbmail img-responsive' src='\1' />", html)
    return html

class Post(models.Model):
    submission = json.JSONField()
    parent = json.JSONField()
    comment = json.JSONField()
    created = models.IntegerField()

    def comment_to_html(self):
        return parse_comment(self.comment.get('body'), display_images=True)

    def parent_as_title(self):
        return parse_comment(self.parent.get('body'))

    def is_simple_image_post(self):
        return "i.imgur.com" in self.comment.get('body')

    def get_context_url(self):
        link = self.submission.get('permalink')
        comment_id = self.comment.get('id')#.split('_')[1]
        return "http://reddit.com/{}/{}/?context=2".format(link,comment_id)

    #TODO permalink

    def __str__(self):
        return "%s -> %s" % (self.parent.get('body'), self.comment.get('body'))

    class Meta:
        ordering = ('-created',)

import praw

from django.core.management.base import BaseCommand, CommandError
from posts.models import Post

class Command(BaseCommand):
    help = "Retrieve posts from reddit API"

    def handle(self, *args, **options):
        r = praw.Reddit(user_agent='logit')
        comments = r.request_json('http://www.reddit.com/user/icanlegothat/comments',
            params={'limit':1000}, as_objects=False)

        existing_ids = [post.comment.get('id') for post in Post.objects.all()]
        
        imported = 0
        for comment_raw in comments.get('data').get('children'):
            comment = comment_raw.get('data')
            comment_id = comment.get('id')
            if comment_id in existing_ids:
                break
            subreddit = comment.get('subreddit')
            submission_id = comment.get('link_id').split('_')[1]
            url = 'http://www.reddit.com/r/{sub}/comments/{sub_id}/_/{comment_id}/'.format(
                sub=subreddit, sub_id=submission_id, comment_id=comment_id)
            print("Call to %s..." % url)
            parent = r.request_json(url, params={'context':1}, as_objects=False)
            
            created = int(float(comment.get('created')))

            submission = parent[0].get('data').get('children')[0].get('data')
            parent_comment = parent[1].get('data').get('children')[0].get('data')
            print("Comment retrieved:")
            print(parent_comment.get('body'))
            print(comment.get('body'))

            parent_comment.pop('replies')

            Post(submission=submission, comment=comment, parent=parent_comment, created=created).save()

            imported +=1
        print("%d posts imported" % imported)

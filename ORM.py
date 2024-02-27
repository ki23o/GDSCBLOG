import os
import django
from BlogApp.models import Post
from CommentApp.models import Comment

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDSCBlog.settings')
django.setup()

# ORM operations for Posts
post1 = Post.objects.create(title='Title 1', content='Content 1', category='Category 1', tags=['Tag1', 'Tag2'])
post2 = Post.objects.create(title='Title 2', content='Content 2', category='Category 2', tags=['Tag3', 'Tag4'])
post3 = Post.objects.create(title='Title 3', content='Content 3', category='Category 1', tags=['Tag5', 'Tag6'])

category1_posts = Post.objects.filter(category='Category 1')
print("Posts in Category 1:")
for post in category1_posts:
    print(f"{post.title}: {post.content}")

post_to_update = Post.objects.get(title='Title 1')
post_to_update.content = 'Updated Content 1'
post_to_update.save()

post_to_delete = Post.objects.get(title='Title 2')
post_to_delete.delete()

# ORM operations for Comments
comment1 = Comment.objects.create(content='Comment 1', author='Author 1', published_date='2022-03-01', post=post1)
comment2 = Comment.objects.create(content='Comment 2', author='Author 2', published_date='2022-03-02', post=post2)
comment3 = Comment.objects.create(content='Comment 3', author='Author 3', published_date='2022-03-03', post=post3)

post1_comments = Comment.objects.filter(post=post1)
print("Comments related to Post 1:")
for comment in post1_comments:
    print(f"{comment.content} by {comment.author}")

comment_to_update = Comment.objects.get(content='Comment 1')
comment_to_update.content = 'Updated Comment 1'
comment_to_update.save()

comment_to_delete = Comment.objects.get(content='Comment 2')
comment_to_delete.delete()

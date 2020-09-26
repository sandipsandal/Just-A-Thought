from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# from django.contrib.sessions.models.Session 
# from blog import views
# from hitcount.models import HitCountMixin, HitCount
# from django.contrib.contenttypes.fields import GenericRelation
# from django.utils.encoding import python_2_unicode_compatible


class Category(models.Model):
    # cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

# @python_2_unicode_compatible
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    author = models.CharField(max_length = 13)
    slug = models.CharField(max_length = 130)
    views = models.IntegerField(default=0)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # timeStamp = models.DateTimeField(blank = True)
    timeStamp = models.DateTimeField(default = now)
    # category = models.CharField(max_length=255,default='Software')
    category = models.CharField(max_length=255)
    # category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # request.session['viewed_post_%s' % post.sno] = True
    # hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title + ' by ' + self.author

    
class BlogComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) # foriegn key = whhich user post the blog-post
    post  = models.ForeignKey(Post, on_delete=models.CASCADE) # if post has deleted comment autometic deleted
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True) # self foreign key == it's pointing to any blog comment(means it is a comment or reply of that comment)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..."+ " by " + self.user.username  #show the username in db model which user post comment [0:13] = means 0-12char.shows 





















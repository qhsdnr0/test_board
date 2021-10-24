from django.db    import models

from core.models  import TimeStamp

class Post(TimeStamp):
    title   = models.CharField(max_length=45)
    content = models.TextField(max_length=2000)

    class Meta:
        db_table = 'posts'

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    post      = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'
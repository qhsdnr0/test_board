from django.db import models

from test_board.core.models import TimeStamp

class Post(TimeStamp):
    title = models.CharField(max_length=45)
    content = models.TextField(max_length=2000)

    class Meta:
        db_table = 'posts'
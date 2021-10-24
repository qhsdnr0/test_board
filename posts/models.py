from django.db    import models

from core.models  import TimeStamp
from users.models import User

class Post(TimeStamp):
    title   = models.CharField(max_length=45)
    content = models.TextField(max_length=2000)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'posts'
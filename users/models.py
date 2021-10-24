from django.db              import models

from test_board.core.models import TimeStamp

class User(TimeStamp):
    name          = models.CharField(max_length=100)
    account       = models.CharField(max_length=45, unique=True)
    password      = models.CharField(max_length=250)
    date_of_birth = models.DateField(null=True)

    class Meta:
        db_table = 'users'
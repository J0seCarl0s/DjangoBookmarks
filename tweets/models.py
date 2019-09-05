from django.db import models
from user_profile.models import User

# Create your models here.
class Tweet(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	text = models.CharField(max_length=100)
	created_date = models.DateTimeField(auto_now_add="True")
	country = models.CharField(max_length=30)
	is_active = models.BooleanField(default = True)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    bio = models.CharField(max_length=100,null=True)
    followers = models.PositiveIntegerField(null=True,default=0)
    following = models.PositiveIntegerField(null=True,default=0)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username} Profile'

    
class Dweet(models.Model):
    dweet = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,related_name="Author",on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f'{self.user_id}"s Dweet'


class UserFollowing(models.Model):
    # Need to switch following followers names
    user_id = models.ForeignKey(User, related_name="following",on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(User, related_name="followers",on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id}"s relation'
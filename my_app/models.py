from django.db import models

# Create your models here.


class Twitts(models.Model):
    author_name = models.CharField(max_length=100)
    author_avatar = models.URLField(max_length=200)
    created_date = models.DateTimeField(blank=True, null=True)
    text = models.CharField(max_length=500)
    media = models.URLField(max_length=200)
    twit_raw_link = models.URLField(max_length=200)
    retweet_count = models.PositiveIntegerField()
    likes_count = models.PositiveIntegerField()

    def publish(self):
        self.published_date = self.created_date
        self.save()

    def __str__(self):
        return self.author_name

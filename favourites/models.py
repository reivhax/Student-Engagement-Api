from django.db import models

# Create your models here.
class Favourite(models.Model):
    article = models.ForeignKey('engagementApp.Articles', related_name='favourites')
    user_uuid = models.TextField()

    class Meta:
        unique_together = (('article', 'user_uuid'),)


class Comments(models.Model):
    article = models.ForeignKey(
        'engagementApp.Articles', related_name='comments')
    user_uuid = models.TextField()
    comment = models.TextField(blank=False, null=False)
    display_name = models.TextField()

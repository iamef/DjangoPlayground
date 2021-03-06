from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    """
    :param models.Model illustrates that it is a Django model
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Foreign key means that it links to another model
    title = models.CharField(max_length=200)  # text with a limited amount of characters
    text = models.TextField()  # text without any limit on number of characters
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
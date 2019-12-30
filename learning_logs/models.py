from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    # A TOPIC THE USER IS LEARNING ABOUT
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        # RETURN A STRING REPRESENTATION OF THE MODEL.
        return self.text

class Entry(models.Model):
    # SOMETHING SPECIFIC LEARNED ABOUT A TOPIC
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        # RETURN A STRING REPRESENTATION OF THE MODEL.
        return f"{self.text[:50]}..."

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField('Privat', default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


RATING = [
    ('★☆☆☆☆', '★☆☆☆☆'),
    ('★★☆☆☆', '★★☆☆☆'),
    ('★★★☆☆', '★★★☆☆'),
    ('★★★★☆', '★★★★☆'),
    ('★★★★★', '★★★★★')
]


class Review(models.Model):
    parent = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.CharField(max_length=7, choices=RATING)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

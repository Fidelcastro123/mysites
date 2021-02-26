from django.db import models

# Create your models here.
class Image(models.Model):
    caption=models.TextField(max_length=1000)
    image=models.ImageField(upload_to="img/%y")
    def __str__(self):
        return self.caption
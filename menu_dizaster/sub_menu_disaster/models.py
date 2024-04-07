from django.db import models
from django.urls import reverse


# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu_name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main', kwargs={'menu_slug': self.url})

    def save(self, *args, **kwargs):
        if self.url[0] != '/':
            self.url = '/' + self.url
        if self.url[-1] != '/':
            self.url = self.url + '/'

        super().save(*args, **kwargs)

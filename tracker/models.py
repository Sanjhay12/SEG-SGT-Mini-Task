from django.db import models


class Request(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

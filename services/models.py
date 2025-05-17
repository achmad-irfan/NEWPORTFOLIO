from django.db import models


class offer(models.Model):
    item = models.CharField(max_length=30)
    desc = models.TextField()
    icon = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.item)


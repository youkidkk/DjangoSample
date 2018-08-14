from django.db import models


class SampleModel(models.Model):
    number = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return "Number: {0}, Text: {1}".format(self.number, self.text)

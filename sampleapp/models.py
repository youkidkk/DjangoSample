from django.db import models


class SampleModel(models.Model):
    number = models.IntegerField()
    text = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    check = models.BooleanField()

    def __str__(self):
        return "Number: {0}, Text: {1}, Date: {2}, Time: {3}, Check: {4}".format(
            self.number, self.text, self.date, self.time, self.check)


class ForeignKeySampleModel(models.Model):
    sampleModel = models.ForeignKey(SampleModel, on_delete=models.CASCADE)
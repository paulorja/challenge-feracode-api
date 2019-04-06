from django.db import models

class Diapers(models.Model):

    model = models.CharField(max_length=255, null=False)

    size = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.model, self.size)




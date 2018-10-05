from django.db import models

class Maintainance(models.Model):
    set_maintainance_page = models.BooleanField()

    def save(self, *args, **kwargs):
      self.clean_fields()
      super(Maintainance, self).save(*args, **kwargs)

    def __str__(self):
        return 'Maintainance Period'


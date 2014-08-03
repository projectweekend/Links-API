from django.db import models


class Folder(models.Model):

    owner = models.ForeignKey('maker.Maker')
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Folder'
        verbose_name_plural = 'Folders'

    def __unicode__(self):
        return "{0}".format(self.name)

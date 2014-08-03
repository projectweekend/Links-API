from django.db import models


class Folder(models.Model):

    owner = models.ForeignKey('maker.Maker')
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Folder'
        verbose_name_plural = 'Folders'
        unique_together = ('owner', 'name',)

    def __unicode__(self):
        return "{0} by {1}".format(self.name, self.owner.identifier)

from django.db import models


class Link(models.Model):

    owner = models.ForeignKey('maker.Maker')
    folder = models.ForeignKey('folder.Folder', null=True, related_name='links')
    title = models.CharField(max_length=100)
    url = models.URLField()
    note = models.TextField(blank=True)
    photo_url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __unicode__(self):
        return "{0} by {1}".format(self.title, self.owner.identifier)

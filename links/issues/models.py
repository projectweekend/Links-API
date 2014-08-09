from django.db import models


OFFENSIVE_CONTENT = 'OFF'
BROKEN_LINK = 'BKN'
NOT_APPROPRIATE = 'NAP'


class ReportedLink(models.Model):

    CATEGORY_CHOICES = (
        (OFFENSIVE_CONTENT, 'Offensive Content'),
        (BROKEN_LINK, 'Broken Link'),
        (NOT_APPROPRIATE, 'Not Appropriate'),
    )

    reporter = models.ForeignKey('maker.Maker', related_name='links_reported')
    link = models.ForeignKey('link.Link', related_name='issues_reported')
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default=BROKEN_LINK)
    note = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Reported Link'
        verbose_name_plural = 'Reported Links'
        unique_together = ('reporter', 'link')

    def __unicode__(self):
        return "{0} by {1}".format(self.link.id, self.reporter.identifier)


class ReportedUser(models.Model):

    CATEGORY_CHOICES = (
        (OFFENSIVE_CONTENT, 'Offensive Content'),
        (NOT_APPROPRIATE, 'Not Appropriate'),
    )

    reporter = models.ForeignKey('maker.Maker', related_name='users_reported')
    user = models.ForeignKey('maker.Maker', related_name='issues_reported')
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default=NOT_APPROPRIATE)
    note = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'ReportedUser'
        verbose_name_plural = 'ReportedUsers'
        unique_together = ('reporter', 'user')

    def __unicode__(self):
        return "{0} by {1}".format(self.reporter.identifier, self.user.identifier)

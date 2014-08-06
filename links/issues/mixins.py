from issues.models import ReportedLink, ReportedUser
from issues.serializers import ReportedLinkSerializer, ReportedUserSerializer


class ReportedLinkAPI(object):

    serializer_class = ReportedLinkSerializer

    def get_queryset(self):
        return ReportedLink.objects.all()


class ReportedLinkSelfAPI(object):

    def get_queryset(self):
        return ReportedLink.objects.filter(reporter=self.request.user)

    def pre_save(self, obj):
        obj.reporter = self.request.user


class ReportedUserAPI(object):

    serializer_class = ReportedUserSerializer

    def get_queryset(self):
        return ReportedUser.objects.all()


class ReportedUserSelfAPI(object):

    def get_queryset(self):
        return ReportedUser.objects.filter(reporter=self.request.user)

    def pre_save(self, obj):
        obj.reporter = self.request.user

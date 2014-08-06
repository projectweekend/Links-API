from rest_framework import generics, status
from rest_framework.response import Response

from issues.mixins import (ReportedLinkAPI,
                            ReportedLinkSelfAPI,
                            ReportedUserAPI,
                            ReportedUserSelfAPI)


class ReportedLinkCreateView(ReportedLinkAPI, ReportedLinkSelfAPI,
                                generics.CreateAPIView):
    pass


class ReportedUserCreateView(ReportedUserAPI, ReportedUserSelfAPI,
                                generics.CreateAPIView):
    pass

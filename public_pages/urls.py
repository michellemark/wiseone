# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import url

from public_pages.views import HomeView, ComingSoonView

urlpatterns = [
    url(r'^home/', HomeView.as_view(), name='home'),
    url(r'^', ComingSoonView.as_view(), name='comingsoon'),
]

# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import url

from public_pages.views import HomeView, ComingSoonView, AboutWiseOneView, BuyersInfoView, SellersInfoView, \
    HomeEvaluationView

urlpatterns = [
    url(r'^free-home-evaluation/', HomeEvaluationView.as_view(), name='homeevaluation'),
    url(r'^home-sellers-info/', SellersInfoView.as_view(), name='sellersinfo'),
    url(r'^home-buyer/', BuyersInfoView.as_view(), name='buyersinfo'),
    url(r'^about/', AboutWiseOneView.as_view(), name='aboutus'),
    url(r'^home/', HomeView.as_view(), name='home'),
    url(r'^', ComingSoonView.as_view(), name='comingsoon'),
]

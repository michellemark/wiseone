from __future__ import unicode_literals

from cms.models.fields import PlaceholderField
from django.db import models


class HomeFeaturedArticlePlaceholder(models.Model):
    home_featured_article = PlaceholderField(slotname='home_featured_article', related_name='home_featured_article')

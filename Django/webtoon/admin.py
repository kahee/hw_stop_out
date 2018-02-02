from django.contrib import admin

# Register your models here.
from webtoon.models import Episode, Webtoon

admin.site.register(Webtoon)
admin.site.register(Episode)
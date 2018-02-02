from django.db import models
from django.utils import timezone


class Webtoon(models.Model):
    webtoon_id = models.CharField(max_length=40)
    title = models.CharField(max_length=288)


class Episode(models.Model):
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE)
    episode_id = models.CharField(max_length=40)
    title = models.CharField(max_length=288)
    rating = models.CharField(max_length=100)
    created_date = models.CharField(max_length=288)

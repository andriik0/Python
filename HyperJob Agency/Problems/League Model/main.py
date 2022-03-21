from django.db import models
from django.db.models import CharField, ForeignKey, IntegerField


class Team(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        app_label = 'tournament'


class League(models.Model):
    name = models.CharField(max_length=32)
    champion = models.ForeignKey(Team, related_name='champion_of', on_delete=models.CASCADE)
    number_of_teams = models.IntegerField()
    class Meta:
        app_label = 'tournament'
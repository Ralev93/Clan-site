from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.db.models.query import QuerySet
from basic.models import Member
import datetime


class Territory(models.Model):
    PLANET_CHOICES = (
        ('S', 'Syra'),
        ('T', 'Terra')
    )

    planet=models.CharField(max_length=1, choices=PLANET_CHOICES)
    name=models.CharField(max_length=50)
    time_for_preparation=models.DateTimeField(blank=True, null=True) #todo to be: models.DurationField?
    time_for_battle=models.DateTimeField(blank=True, null=True)

    def get_name(self):
        return self.name

    def __str__(self):
        return "{0}/{1}.".format(self.get_planet_display(), self.name)

class Battle(models.Model):
    STATUS_CHOICES = (
            ('O', 'Open'),
            ('C', 'Closed'),
            ('F', 'Future') 
        )

    date=models.DateField(default=datetime.date.today)
    status=models.CharField(
        max_length=1,
        choices=STATUS_CHOICES
    )

    class Meta:
        abstract = True


class TerritoryBattle(Battle):
   
    assigned_users = models.ManyToManyField(Member) #Maktia.assignedUsers.add('john')
    territory = models.ForeignKey(Territory, on_delete=models.PROTECT)
    # hypothesis = models.ManyToManyField(Hypothesis, default=0, blank=True)


    def __str__(self):
        return "Battle for " + str(self.territory)

    def calculateHypothesis():
        pass

class ClanWar(Battle):
    CLAN_WAR_TYPES = (
            ('XP', 'Experience'),
            ('RES', 'Resources'),
            ('DMG', 'Damage'),
            ('GL', 'Glory')
        )

    RESULT_CHOICES = (
            ('w', 'won'),
            ('l', 'lost'),
            ('p', 'proccesing')
        )

    war_type = models.CharField(
            max_length=3,
            choices=CLAN_WAR_TYPES)
    result = models.CharField(
        max_length=1,
        choices=RESULT_CHOICES)
    enemy_clans = models.CharField(max_length=120)


    def __str__(self):
        return "{0} war ({1})".format(self.get_war_type_display(),
         self.date)



class Hypothesis(models.Model):
    STAR_CHOICES = [(str(i), i) for i in range(0,4)]
    OPPONENTS = [i for i in range(1,11)]

    terittory_battle = models.ForeignKey(TerritoryBattle)
    teammate = models.ForeignKey(Member)
    opponent = models.PositiveSmallIntegerField()
    stars = models.CharField(max_length=1, choices=STAR_CHOICES)

    class Meta:
        unique_together = (("terittory_battle", "opponent", "stars"))


    def getHypothesis(self):
        return {self.teammate.get_username(): {self.opponent: self.stars}}

    def __str__(self):
        return str(self.terittory_battle) +" "+str(self.getHypothesis())



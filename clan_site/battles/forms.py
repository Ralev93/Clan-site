from django import forms
from django.contrib.admin.widgets import AdminDateWidget 
from django.forms import ModelForm
from basic.models import *
from battles.models import *
from itertools import chain

def getMemberAsOptions():
	members = Member.objects.all()
	return [(member.id, member.get_username()) for member in members]

def getTerritoriesAsOptions():
	territories = Territory.objects.all()
	return [(terittory.id, terittory.get_name()) for terittory in territories]


# todo: modelForm!!!
class Battle(forms.Form):
	status = forms.ChoiceField(Battle.STATUS_CHOICES)
	date = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget)

class TerritoryBattleForm(Battle):
	assigned_users = forms.MultipleChoiceField(choices=getMemberAsOptions(), widget=forms.CheckboxSelectMultiple())
	planet=forms.ChoiceField(Territory.PLANET_CHOICES)
	territory=forms.ChoiceField(choices=getTerritoriesAsOptions())

class ClanWarForm(Battle):
	clan_war_type = forms.ChoiceField(ClanWar.CLAN_WAR_TYPES)
	result = forms.ChoiceField(ClanWar.RESULT_CHOICES)
	enemy_clans=forms.CharField(max_length=50)


class HypothesisForm(forms.Form):
	def __init__(self, *args, **kwargs):
	        super(HypothesisForm, self).__init__(*args, **kwargs)
	        for i in Hypothesis.OPPONENTS:
	            self.fields['opponent_' + str(i)] = forms.ChoiceField(Hypothesis.STAR_CHOICES)
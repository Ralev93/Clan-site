from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name='battles'

urlpatterns = [
    url(r'^$', login_required(views.BattlesIndexView.as_view()), name='battles'),
    url(r'^clan_wars/$', login_required(views.ClanWarsView.as_view()), name='clan_wars'),
    url(r'^ter_battles/$', login_required(views.TerBattlesView.as_view()), name='ter_battles'),
    url(r'^clan_wars/(?P<pk>[0-9]+)/$', login_required(views.ClanWarDetailView.as_view()), name='clan_war_details'),
    url(r'^ter_battles/(?P<pk>[0-9]+)/$', login_required(views.TerBattleDetailView.as_view()), name='ter_battle_details'),
    url(r'^ter_battles/(?P<pk>[0-9]+)/$', views.assign_members, name='assign'),


    url(r'^add_territory_battle$', views.add_territory_battle, name='add_territory_battle'),
    url(r'^add_clan_war_battle$', views.add_clan_war_battle, name='add_clan_war_battle'),
    url(r'^add_hypothesis/(?P<battle_id>[0-9]+)/$', views.add_hypothesis, name='add_hypothesis'),

]
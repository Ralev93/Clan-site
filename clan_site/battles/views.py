from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import *
from battles.forms import *

from itertools import chain

class BattlesIndexView(generic.ListView):
    template_name = 'battles/battles.html'

    def get_queryset(self):
        return '';


class ClanWarsView(generic.ListView):
    template_name = 'battles/clan_wars.html'
    model = ClanWar

    def get_context_data(self, **kwargs):
        context = super(ClanWarsView, self).get_context_data(**kwargs)
        context['battles'] = ClanWar.objects.all()
        context['clan_war_form'] = ClanWarForm()

        return context


class TerBattlesView(generic.ListView):
    template_name = 'battles/ter_battles.html'
    model = TerritoryBattle

    def get_context_data(self, **kwargs):
        context = super(TerBattlesView, self).get_context_data(**kwargs)
        context['battles'] = TerritoryBattle.objects.all()
        context['territory_form'] = TerritoryBattleForm()

        return context


class ClanWarDetailView(generic.DetailView):
    template_name='battles/clan_war_details.html'
    model = ClanWar
    context_object_name='battle'

class TerBattleDetailView(generic.DetailView):
    template_name='battles/ter_battle_detail.html'
    model = TerritoryBattle
    context_object_name='battle'

    def get_context_data(self, **kwargs):
        context = super(TerBattleDetailView, self).get_context_data(**kwargs)
        context['form'] = HypothesisForm()
        return context
  

def add_territory_battle(request):
    if request.method == 'POST':
        form = TerritoryBattleForm(request.POST)
        if form.is_valid():
            status = form.cleaned_data['status']
            date = form.cleaned_data['date']
            assigned_users_ids=form.cleaned_data['assigned_users']
            assigned_users = [Member.objects.get(pk=user_id) for user_id in assigned_users_ids]
            # planet=form.cleaned_data['planet']
            terittory_id=form.cleaned_data['territory']
            terittory=Territory.objects.get(pk=terittory_id)

            new_territory_battle = TerritoryBattle(status=status, date=date, territory=terittory)
            new_territory_battle.save()

            for assigned_user in assigned_users:
                new_territory_battle.assigned_users.add(assigned_user)
            new_territory_battle.save()

            return HttpResponseRedirect(reverse('battles:ter_battles'))
    else:
        form = TerritoryBattleForm()

    return render(request, TerBattlesView.template_name, {'territory_form': form, 'battles': TerritoryBattle.objects.all()})
    #todo: Refactor!!!


def add_clan_war_battle(request):
    if request.method == 'POST':
        form = ClanWarForm(request.POST)
        if form.is_valid():
            war_type = form.cleaned_data['clan_war_type']
            result = form.cleaned_data['result']
            enemy_clans=form.cleaned_data['enemy_clans']

            new_clan_war = ClanWar(war_type=war_type, result=result, enemy_clans=enemy_clans)
            new_clan_war.save()

            return HttpResponseRedirect(reverse('battles:clan_wars'))
    else:
        form = ClanWarForm()

    return render(request, ClanWarsView.template_name, {'clan_war_form': form, 'battles':ClanWar.objects.all()})
    # todo Refactor the 'battles'


def add_hypothesis(request, battle_id):
    if request.method == 'POST':
        form = HypothesisForm(request.POST)
        if form.is_valid():
            battle = TerritoryBattle.objects.get(pk=battle_id)
            for i in Hypothesis.OPPONENTS:
                stars = form.cleaned_data['opponent_' + str(i)]
                
                m  = Member.objects.get(username=request.user.get_username())
                h = Hypothesis.objects.get_or_create(terittory_battle=battle, teammate=m, opponent=i)
                h[0].stars=stars
                h[0].save()

            return HttpResponseRedirect(reverse('battles:ter_battles'))
    else:
        form = HypothesisForm()

    return render(request, TerBattlesView.template_name, {'territory_form': form, 'battles': TerritoryBattle.objects.all()})
    #todo: Refactor!!!



def assign_members(request, battle_id):
    return render(request, TerBattlesView.template_name, {'territory_form': form, 'battles': TerritoryBattle.objects.all()})
    #todo: Refactor!!!
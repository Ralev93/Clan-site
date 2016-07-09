from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from basic.models import *
from .models import *

import datetime

# from .forms import *


class ScheduleIndexView(generic.ListView):
    template_name = 'memberSchedule/index.html'

    def get_queryset(self):
        return '';


@login_required
def add_availability(request):
    if request.method == 'POST':
        start, end, day = request.POST['start_time'], request.POST['end_time'], request.POST['day']

        m = Member.objects.get(username=request.user.get_username())
        # d = datetime.datetime(day, start, end) todo
        s = Schedule(member=m,available=timezone.now)
        # s.save()

    else:
        form = RulesForm()

    return render(request, ScheduleIndexView.template_name)
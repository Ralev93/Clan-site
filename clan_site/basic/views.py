from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import *


class IndexView(generic.ListView):
    template_name = 'basic/index.html'

    def get_queryset(self):
        return '';


class UsersView(generic.ListView):
    template_name = 'basic/users.html'
    context_object_name = 'users'

    def get_queryset(self):
        return Member.objects.order_by('first_name')


class RulesView(generic.ListView):
    template_name = 'basic/rules.html'
    # context_object_name = 'rules'
    model = Rules

    def get_context_data(self, **kwargs):
        context = super(RulesView, self).get_context_data(**kwargs)
        context['rules'] = Rules.objects.all()
        context['form'] = RulesForm()
        return context

#
# @login_required
class RulesDetailView(generic.DetailView):
    model = Rules
    context_object_name='rule'
    template_name = 'basic/rules_detail.html'


# @login_required
class DetailView(generic.DetailView):
    model = Member
    context_object_name='user'
    template_name = 'basic/detail.html'



# @login_required
def add_rule(request):
    if request.method == 'POST':
        form = RulesForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['rule_content']
            m  = Member.objects.get(username=request.user.get_username())
            new_rule = Rules(content=content, created_by=m)
            new_rule.save()
            return HttpResponseRedirect(reverse('basic:rules'))
    else:
        form = RulesForm()

    return render(request, 'basic/rules.html', {'form': form, 'rules': Rules.objects.all()})

  
def register_handle(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            # user = super(UserCreationForm, self).save(commit=False)
            # user.set_password(self.cleaned_data["password1"])
            # if commit:
                # user.save()
            m = Member(username=form.cleaned_data['username'], user_type="M")
            m.set_password(form.cleaned_data["password1"])
            m.save()
            return HttpResponseRedirect(reverse('login'))
            # return HttpResponseRedirect(reverse('basic:index'))

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')



def login_handle(request):
    # if request.method != 'POST':
    #     raise Http404('Only POSTs are allowed')
    # try:
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('basic:index'))
        else:
            return HttpResponse("Your account have been disabled :(")
    else:
        return HttpResponse("Your username and password didn't match")

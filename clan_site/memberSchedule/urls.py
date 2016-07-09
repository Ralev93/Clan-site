from django.conf.urls import url
from . import views

app_name='memberSchedule'

urlpatterns = [
    url(r'^$', views.ScheduleIndexView.as_view(), name='schedule'),
    url(r'^add_availability/$', views.add_availability, name='add_availability'),
    # url(r'^add_inavailability/$', views.add_inavailability.as_view(), name='add_inavailability')
]
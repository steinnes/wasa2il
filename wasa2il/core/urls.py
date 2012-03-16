from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required

from core.views import TopicListView
from core.models import Polity, Topic, Issue

urlpatterns = patterns('',
	(r'^$', 'core.views.home'),

	(r'^polities/$',					login_required(ListView.as_view(model=Polity, context_object_name="polities"))),
	(r'^polity/new/$',					login_required(CreateView.as_view(model=Polity, success_url="/polity/%(id)d/"))),
	(r'^polity/(?P<pk>\d+)/edit/$',				login_required(UpdateView.as_view(model=Polity, success_url="/polity/%(id)d/"))),
	(r'^polity/(?P<pk>\d+)/$',				login_required(DetailView.as_view(model=Polity, context_object_name="polity"))),

	(r'^polity/(?P<polity>\d+)/topics/$',			login_required(TopicListView.as_view(model=Topic, context_object_name="topics"))),
	(r'^polity/(?P<polity>\d+)/topic/new/$',		login_required(CreateView.as_view(model=Topic, success_url="/polity/%(polity__id)d/topic/%(id)d/"))),
	(r'^polity/(?P<polity>\d+)/topic/(?P<pk>\d+)/edit/$',	login_required(UpdateView.as_view(model=Topic, success_url="/polity/%(polity__id)d/topic/%(id)d/"))),
	(r'^polity/(?P<polity>\d+)/topic/(?P<pk>\d+)/$',	login_required(DetailView.as_view(model=Topic, context_object_name="topic"))),

	(r'^polity/(?P<polity>\d+)/issues/$',			login_required(ListView.as_view(model=Issue, context_object_name="issues"))),
	(r'^polity/(?P<polity>\d+)/issue/new/$',		login_required(CreateView.as_view(model=Issue, success_url="/polity/issue/%(id)d/"))),
	(r'^polity/(?P<polity>\d+)/issue/(?P<pk>\d+)/edit/$',	login_required(UpdateView.as_view(model=Issue, success_url="/issue/%(id)d/"))),
	(r'^polity/(?P<polity>\d+)/issue/(?P<pk>\d+)/$',	login_required(DetailView.as_view(model=Issue, context_object_name="issue"))),
)
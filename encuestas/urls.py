from django.conf.urls import patterns, url

from encuestas import views


urlpatterns = patterns('',
	url(r'^$', views.index, name="index"),
	url(r'^(?P<encuesta_id>\d+)/$', views.detalles, name="detalles"),
	url(r'^(?P<encuesta_id>\d+)/resultados/$', views.resultados, name="resultados"),
	url(r'^(?P<encuesta_id>\d+)/votos/$', views.votos, name="votos"),
	)
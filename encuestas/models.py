import datetime

from django.db import models
from django.utils import timezone


class Pregunta(models.Model):
	pregunta_texto = models.CharField(max_length=200)
	pregunta_fecha = models.DateTimeField('fecha Publicacion')

	def __str__(self):
		return self.pregunta_texto

	def publicado(self):
		return self.pregunta_fecha >= timezone.now() - datetime.timedelta(days=1)
 

class Eleccion(models.Model):
	pregunta = models.ForeignKey(Pregunta)
	eleccion_texto = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)

	def __str__(self):
		return self.eleccion_texto
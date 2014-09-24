from django.contrib import admin
from encuestas.models import Pregunta, Eleccion


class EleccionEnLinea(admin.TabularInline):
	model = Eleccion
	extra = 3

class PreguntaAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 		{'fields':['pregunta_texto']}),
		('Fecha:', 	{'fields':['pregunta_fecha']})
	]
	inlines = [EleccionEnLinea]
	list_display = ('pregunta_texto', 'pregunta_fecha', 'publicado')

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Eleccion)



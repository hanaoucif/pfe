from django.contrib import admin
from .models import *

from django.forms import TextInput, Textarea
from django.forms import ModelForm
from django.forms import BaseModelFormSet
from django.utils.html import format_html



admin.site.register(marche)
admin.site.register(Commission)
admin.site.register(mouvrage)

admin.site.register(tache_Agent)
admin.site.register(specialite)	      
admin.site.register(Projet)	 
admin.site.register(Tache)	 	 
admin.site.register(Document)	
admin.site.register(Direction)	
admin.site.register(Agent)
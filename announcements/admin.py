from django.contrib import admin
from .models import AdoptPet, FoundedPet, LostPet

admin.site.register(AdoptPet)
admin.site.register(FoundedPet)
admin.site.register(LostPet)

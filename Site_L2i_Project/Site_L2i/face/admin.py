from django.contrib import admin

from face.models import cours

@admin.register(cours)
class coursAdmin(admin.ModelAdmin):
    list_display=('titre','matiere','coef','auteur')
    search_fields=('niveau','matiere',)
    list_filter=('niveau','matiere',)


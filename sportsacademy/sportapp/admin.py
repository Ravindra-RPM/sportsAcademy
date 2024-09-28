from django.contrib import admin
from .models import Coach, Team, Player

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('uid', 'specialization')
    search_fields = ('uid__username', 'specialization')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'coach')
    search_fields = ('name',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'team')
    search_fields = ('first_name', 'last_name', 'team')


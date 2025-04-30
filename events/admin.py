from django.contrib import admin
from .models import Event, Participation

class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 0

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'participant_count')
    search_fields = ('title', 'description', 'location')
    list_filter = ('date',)
    inlines = [ParticipationInline]

@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'is_attending', 'registered_at')
    list_filter = ('is_attending', 'registered_at', 'event')
    search_fields = ('user__username', 'event__title')
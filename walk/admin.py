from django.contrib import admin
from walk.models import Trip, Segment

class SegmentAdmin(admin.ModelAdmin):
	list_display = ('time','log', 'lat', 'breath')
	search_fields = ('time',)
	list_filter = ('breath',)

admin.site.register(Trip)
admin.site.register(Segment, SegmentAdmin)
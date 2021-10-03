from django.contrib import admin
from .models import Team, Current, Planned, Finished, Failed

admin.site.register(Team)
admin.site.register(Current)
admin.site.register(Planned)
admin.site.register(Finished)
admin.site.register(Failed)

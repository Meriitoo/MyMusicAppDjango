from django.contrib import admin

from MyMusicApp.web.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


# Reni
# pass - reni123

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass

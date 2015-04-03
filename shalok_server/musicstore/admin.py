from django.contrib import admin
from musicstore.models import Musician,Album,Song,Playlist,User_Playlist
#Login,Playlist_Detail


admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Playlist)
#admin.site.register(Playlist_Detail)
#admin.site.register(Login)
admin.site.register(User_Playlist)
#admin.site.register(Sale)

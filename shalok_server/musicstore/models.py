from django.db import models
from django.contrib.auth.models import User



#Detail for Musician 
class Musician(models.Model):
    class Meta:
      app_label = 'musicstore'
      db_table = 'musician'

    name = models.CharField(max_length=50,primary_key=True)
    history = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

#Detail of Album
class Album(models.Model):
    class Meta:
      app_label = 'musicstore'
      db_table = 'album'

    HINDI = 'HINDI'
    ENGLISH = 'ENGLISH'
    TAMIL = 'TAMIL'
    TELGU = 'TELGU'
    MARATHI = 'MARATHI'
    PUNJABI ='PUNJABI'
    GUJRATI ='GUJRATI'
    BENGALI='BENGALI'
    KANNADA='KANNADA'
    MALAYALAM='MALAYALAM'
    BHOJPURI='BHOJPURI'
    ORIYA='ORIYA'
    RELEGION_TYPE_CHOICES = (
        (HINDI, 'HINDI'),
        (ENGLISH, 'ENGLISH'),
        (TAMIL, 'TAMIL'),
        (TELGU, 'TELGU'),
        (MARATHI, 'MARATHI'),
        (PUNJABI, 'PUNJABI'),
        (GUJRATI, 'GUJRATI'),
        (BENGALI, 'BENGALI'),
        (KANNADA, 'KANNADA'),
        (MALAYALAM, 'MALAYALAM'),
        (BHOJPURI, 'BHOJPURI'),
        (ORIYA, 'ORIYA'),
    )
    album_id = models.AutoField(primary_key=True)
    musician = models.ForeignKey(Musician)
    album_name = models.CharField(max_length=100)
    release_date = models.DateField(
            blank=True, null=True)
    favorite = models.IntegerField(default=0)
    relegion = models.CharField(max_length=10,
                                      choices=RELEGION_TYPE_CHOICES,
                                      default=HINDI)
    def __str__(self):
        return self.album_name

#Song related information
class Song(models.Model):
     class Meta:
       app_label = 'musicstore'
       db_table = 'songs'
       unique_together = ('album', 'song',)
     
     CLASSICAL='CLASSICAL'
     ROCK='ROCK'
     COUNTRY='COUNTRY'
     BALLADS='BALLADS'
     LOVE='LOVE'
     POP='POP'
     METAL='METAL'
     HIPHOP='HIPHOP'
     DANCE='DANCE'
     GOSPEL='GOSPEL'
     GENRE_TYPE_CHOICES = (
         (CLASSICAL, 'CLASSICAL'),
         (ROCK, 'ROCK'),
         (COUNTRY, 'COUNTRY'),
         (BALLADS, 'BALLADS'),
         (LOVE, 'LOVE'),
         (POP, 'POP'),
         (METAL, 'METAL'),
         (HIPHOP, 'HIPHOP'),
         (DANCE, 'DANCE'),
         (GOSPEL, 'GOSPEL'),
     )
     record_sold= models.IntegerField(default=0);
     album = models.ForeignKey(Album)
     song = models.CharField(max_length=50)
     size = models.DecimalField(max_digits=4, decimal_places=2)
     like = models.IntegerField(default=0);
     genre = models.CharField(max_length=10,
                                      choices=GENRE_TYPE_CHOICES,
                                      default=CLASSICAL)
     def __str__(self):
        return self.song

#Information related to playlist 
class Playlist(models.Model):
      class Meta:
        app_label='musicstore'
        db_table='playlist'

      playlist_name= models.CharField(max_length=100)
      playlist_id =models.AutoField(primary_key=True)
     
      def __str__(self):
        return str(self.playlist_id)

#Songs contain by individual playlist one playlist having many songs 
class User_Playlist(models.Model):
      class Meta:
        app_label='musicstore'
        db_table='userplaylist'
        unique_together = ('playlist', 'song_id',)

      playlist= models.ForeignKey(Playlist,related_name="idplaylist", null=True, blank=True)
      song_id= models.ForeignKey(Song)
      
      def __str__(self):
        return str(self.playlist)



#For login related information one to one relationship
#class Login(models.Model):
#      class Meta:
#        app_label='musicstore'
#        db_table='login'

#      username= models.CharField(max_length=50,primary_key=True)
#      password= models.CharField(max_length=50)
      
#      def __str__(self):
#        return str(self.username)

#Relation of playlist with user one to many relationship
#class Playlist_Detail(models.Model):
#      class Meta:
#        app_label='musicstore'
#        db_table='playlistdetail'
#        unique_together = ('username_for', 'playlist',)

#      username_for= models.ForeignKey(Login)
#      playlist= models.ForeignKey(Playlist,related_name="playlistid", null=True, blank=True)
      
#       def __str__(self):
#        return str(self.username_for)


     

   

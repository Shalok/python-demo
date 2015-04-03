true=True
false=False
import sys
import sqlite3 as lite
import json
import csv
import jsonschema
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth 
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework import views
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render_to_response
#from StringIO import StringIO
from django.conf import settings
from musicstore.models import Musician,Album,Song,User_Playlist,Playlist
from django.core import serializers
from django.core.context_processors import csrf
from django.template import RequestContext
from django.template import RequestContext





@api_view(['GET'])
def MAIN(request):
   if request.method == 'GET':
       #data = serializers.serialize("json", Song.objects.filter(musician))
       #display=data[0].pk
       album_list = Album.objects.all().order_by('-favorite')
       song_list = Song.objects.all().order_by('-like')
       song=Song.objects.get(id=1)
       dif= Album.objects.order_by('relegion').values('relegion').distinct()
       print(dif.count)
       #sale=Sale.objects.all().order_by('-record_sold')
       #print (sale)
       #print(sale['0'].record_sold)
       return render_to_response('welcome.html',{'albums': album_list,'songs': song_list}) 

@api_view(['GET'])
def filterAlbum(request,album,value):
       #print album
       print(value)
       play={}
       play=Playlist.objects.all();
       print(play)
       album_list = Album.objects.get(album_id=album)
       value=album_list.favorite
       value=value+1
       Album.objects.filter(album_id=album).update(favorite=value)
       song_list = Song.objects.all().filter(album=album).order_by('-like')
       return render_to_response('album.html',{'album': album_list,'songs': song_list,'playlist':play}) 

@api_view(['GET'])
def filterSong(request,song):
       song_list = Song.objects.get(id=song)
       value=song_list.like
       value=value+1
       print (value)
       Song.objects.filter(id=song).update(like=value)
       print(song_list)
       #song_list = Song.objects.all().filter(album=album).order_by('-like')
       return render_to_response('song.html',{'songs': song_list}) 

@api_view(['POST'])
def ADDtoPlaylist(request):
       a=request.POST.getlist('tasks[]')
       print (a)
       return Response('',status=201)

@api_view(['GET'])
def login(request):
       c={}
       c.update(csrf(request))
       return render_to_response('login.html',c)

@api_view(['POST'])
def auth_view(request):
       username=request.POST.get('username','')
       password=request.POST.get('password','')
       user= auth.authenticate(username=username,password=password)

       if user is not None:
          auth.login(request,user)
          return HttpResponseRedirect('/accounts/loggedin')
       else:
          return HttpResponseRedirect('/accounts/invalid')

@api_view(['GET'])
def loggedin(request):
       print(request.user)
       if request.user.is_authenticated():
          username = request.user.username
          
       return render_to_response('loggedin.html',{'full_name':request.user.username})

@api_view(['GET'])
def invalid_login(request):
       return render_to_response('invalid_login.html')

@api_view(['GET'])
def logout(request):
       auth.logout(request)
       return render_to_response('logout.html')


def register_user(request):
       if request.method == 'POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/accounts/register_success')

       args={}
       args.update(csrf(request))

       args['form'] = UserCreationForm()
       print (args)
       return render_to_response('register.html',args)

@api_view(['GET'])
def register_success(request):
       return render_to_response('register_success.html')


@api_view(['GET'])
def Trending(request):
       diff={}
       diff= Album.objects.order_by('relegion').values('relegion').distinct()
       print (diff)
       return render_to_response('trending.html',{'songs': diff}) 

@api_view(['GET'])
def TrendingCatagory(request,value):
       print(value)
       obj={}
       obj=Song.objects.filter(album__relegion=value).order_by('-record_sold')
       play={}
       play=Playlist.objects.all();
       for item in obj:
           print(item.id)
       print(obj[0])
       return render_to_response('topselling.html',{'songs': obj,'playlist':play}) 

#@api_view(['POST'])
#def ALBUM(request,value):
#   if request.method == 'POST':
#        p={}
#        p = Album.objects.get(pk=value)
#        print (p) 
#   return HttpResponse('My first view.')




      

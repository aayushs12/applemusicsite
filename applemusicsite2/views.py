from django.shortcuts import render,redirect
from django.http import HttpResponse
from applemusicsite2.models import register
from applemusicsite2.forms import stform
from django.contrib import messages
from django.contrib.auth.models import User, auth
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def index(request):
    return render(request,"applemusicsite2/index.html")
def features(request):
    return render(request,"applemusicsite2/features.html")
def insert(request):
    if request.method=="POST":
        if request.POST.get('firstName') and request.POST.get('lastName') and request.POST.get('emailAddress') and request.POST.get('phoneNumber') and request.POST.get('inlineRadioOptions') and request.POST.get('password') :
            savest=register()
            savest.firstname=request.POST.get('firstName')
            savest.lastname=request.POST.get('lastName')
            savest.email=request.POST.get('emailAddress')
            savest.phn=request.POST.get('phoneNumber')
            savest.plan=request.POST.get('inlineRadioOptions')
            savest.password=request.POST.get('password')
            if(register.objects.filter(email=savest.email).exists()):
                messages.warning(request,'Email is already in use')
                return redirect('signup')
            elif(register.objects.filter(phn=savest.phn).exists()):
                messages.warning(request,'Phone Number is already in use')
                return redirect('signup')
            else:
                savest.save()
                messages.success(request,"Registered Successfully")
                return render(request,"applemusicsite2/signup.html")
    else:
        return render(request,"applemusicsite2/signup.html")
def catalogue(request):
    if request.method=='POST':
        artist_uri = request.POST.get('uri')
        key,artist_uri2=idGenerator(artist_uri)
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='0dc0be6c2bbb46f5ac69c08a91f0db9c',client_secret='b25e6557407f43d287e0f113415d3cb0',))
        results = spotify.artist_top_tracks(artist_uri2)
        resultsalbum = spotify.artist_albums(artist_uri2, album_type='album')
        final_result=results['tracks'][:14]
        resultsalbum=resultsalbum['items'][:7]
        return render(request,'applemusicsite2/catalogue.html',{"results":final_result,"resultsalbum":resultsalbum,"artistname":artist_uri})
    else:
      return render(request,'applemusicsite2/catalogue.html',)


def idGenerator (search) :
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='0dc0be6c2bbb46f5ac69c08a91f0db9c',client_secret='b25e6557407f43d287e0f113415d3cb0',))
    names = search #chosen artist , song , playlist
    result = sp.search (names) #search query
    if result['tracks']['items'][0]['artists'][0]['name'] == 'names':
        id = result['tracks']['items'][0]['artists'][0]['id']
        type = result [ 'tracks' ] [ 'items' ] [ 0 ] [ 'artists' ] [ 0 ] [ 'id' ]
        return type , id
    elif result [ 'tracks' ] [ 'items' ] [ 0 ] [ 'type' ] == 'album' :
        id = result [ 'tracks' ] [ 'items' ] [ 0 ] [ 'id' ]
        type = result [ 'tracks' ] [ 'items' ] [ 0 ] [ 'type' ]
        return type , id
    elif result [ 'tracks' ] [ 'items' ] [ 0 ] [ 'type' ] == 'track' :
        id = result [ 'tracks' ] [ 'items' ] [ 0 ] [ 'artists' ] [ 0 ] [ 'id' ]
        type = result [ 'tracks' ] [ 'items' ] [ 0 ] [ 'artists' ] [ 0 ] [ 'type' ]
        return type , id
    else :
        id = "NOT"
        type = "found"
        return type , id

def login(request):
    if request.method == 'POST':
        username = request.POST['emailAddress']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if(register.objects.filter(email=username,password=password).exists()):
            messages.success(request,"Logged in successfully")
            return render(request,"applemusicsite2/login.html")
        else:
            messages.warning(request, 'Invalid Email or Password')
            return redirect('login')
    else:
        return render(request,"applemusicsite2/login.html")

from django.shortcuts import render
from myapp.models import Page, Post, Song, User
# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def show_user_data(request):
    data1 = User.objects.all()
    data2 = User.objects.filter(email = 'shivam@gmail.com')
    # page__page_cat>>> Page model __page_cat
    # filter those user for which page_cat is 'Programming'
    data3 = User.objects.filter(mypage__page_cat='Programming')
    data4 = User.objects.filter(
        mypost__post_publish_date = '2024-09-10')
    data5 = User.objects.filter(
        song__song_duration=3)
    return render(request, 'myapp/user.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5})

def  show_page_data(request):
    data1 = Page.objects.all()
    data2 = Page.objects.filter(page_cat = 'Programming')
    data3 = Page.objects.filter(user__email = 'shivam@gmail.com')
    return render(request, 'myapp/page.html',{'data1':data1, 'data2':data2, 'data3': data3})

def show_post_data(request):
    data1 = Post.objects.all()
    data2 = Post.objects.filter(post_publish_date = '2024-09-10')
    data3 = Post.objects.filter(user__username = 'sonam')
    return render(request, 'myapp/post.html',{'data1':data1, 'data2':data2, 'data3': data3})

def show_song_data(request):
    data1 = Song.objects.all()
    data2 = Song.objects.filter(song_duration=3)
    data3 = Song.objects.filter(user__username = 'sonam')
    return render(request, 'myapp/song.html',{'data1':data1, 'data2':data2, 'data3': data3})

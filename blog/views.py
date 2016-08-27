from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404,redirect
from .forms import PostForm,profileform,EmailForm
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html',{'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def SaveProfile(request):
   saved = False
   
   if request.method == "POST":
      #Get the posted form
      MyProfileForm = ProfileForm(request.POST, request.FILES)
      
      if MyProfileForm.is_valid():
         profile = Profile()
         profile.name = MyProfileForm.cleaned_data["name"]
         profile.picture = MyProfileForm.cleaned_data["picture"]
         profile.save()
         saved = True
         return redirect('showProfile')
   else:
      MyProfileForm = ProfileForm()
        
   return render(request, 'saved.html', locals())


def showProfile(request):
    profiles = Profile.objects.all()
    return render(request,'blog/profiles.html',{'profiles':profiles})


def addNotes(request):
    if request.method == "POST":
        form = profileform(request.POST,request.FILES)
        if form.is_valid():
            print('done')
            # profile = Profile()
            # profile.name = form.cleaned_data["name"]
            # profile.picture = form.cleaned_data["picture"]
            post = form.save(commit=False)
            #post.published_date = timezone.now()
            profile.save()
            return redirect('showProfile')
    else:
        form = profileform()
    return render(request, 'blog/newNotes.html', {'form': form})



def Email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = settings.DEFAULT_FROM_EMAIL
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            message = "HI";
            send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
                        [email], fail_silently=False)
            return redirect('showProfile')
    else:
        form = EmailForm()
    render(request,'blog/send_mail.html',{'eform':form})
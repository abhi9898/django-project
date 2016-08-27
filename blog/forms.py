from django import forms
from .models import Profile
from .models import Post,Profile

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

# class ProfileForm(forms.Form):
#    name = forms.CharField(max_length = 100)
#    picture = forms.ImageField()

class profileform(forms.ModelForm):

 	class Meta:
 		model = Profile
 		fields = ('name','picture')


class EmailForm(forms.Form):
	subject = forms.CharField(required=True,max_length=20)
	names = forms.CharField(required=True)
	email = forms.EmailField()
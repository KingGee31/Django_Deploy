# import the following
from django import forms
from blog.models import Post,Comment

# creating form dot models
class PostForm(forms.ModelForm):

#    creating a meta class
# Model Meta is basically used to change the behavior of your model fields
    class Meta():
        #connecting a model with form
        model = Post
        # the following are the fields that i want a user to be able to fill
        fields = ('author','title','text')
# widgets are used to style the input/title/button of the form.... in this case we ain't using html form but using databate attributes to generate html forms for us
        widgets = {
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})}
# this creates an comment html form
class CommentForm(forms.ModelForm):

  class Meta():
      # connecting to the database
    model = Comment
    # the following are the fields that i want a user to be able to fill in comment session
    fields = ('author','text')
    # widgets are used to style the input/title/button of the form.... in this case we ain't using html form but using databate attributes to generate html forms for us
    widgets = {
    'author': forms.TextInput(attrs={'class':'textinputclass'}),
    'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea '})}

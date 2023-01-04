from django.shortcuts import render, get_object_or_404,redirect
# indicating that i'll importing time "To get time"
from django.utils import timezone
# the following tells that i'll be using models from my app, i am importing tables that i'll be using
from blog.models import Post,Comment
# i am importing this to allow a super user to be able to login to the blog
from django.contrib.auth.mixins import LoginRequiredMixin
# this is the same thing as i explained above, the only difference it is from different django version
from django.contrib.auth.decorators import login_required
# the following line explains that i'll be importing forms that that i created under my blog that will take user input
from blog.forms import PostForm, CommentForm
# i am importing this following because i want to use class base views
from django.contrib.auth import views as auth_views
# i am importing the following because class base views needs to be redirected to another page after it have been used
from django.urls   import reverse_lazy
# here i am importing class base views that i'll be using
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)

# Create your views here.
# the following class base view will return the about html page
class AboutView(TemplateView):
# here i am paring my html page
    template_name = 'about.html'
# the following class base view retriev everything that is on the Post table and paste the data to post_list html page
class PostListView(ListView):
    # connecting my class base view with the database table
    model = Post

# the following method is a django sql statement , it select everything from the Post 'posts' table and order by a date
    def get_queryset(self):
       return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

# this view is connected to html file 'post_detail'
class PostDetailView(DetailView):
     model = Post

# the following view is the one used to create a post as it is contains PostForm model
class CreatePostView(LoginRequiredMixin,CreateView):

# the following is set as a restriction, a user should first loging before they can create a post
    login_url = '/login/'
    # After a user have Created a Post they'll be redirected to post_detail page
    redirect_field_name = 'blog/post_detail.html'
# here we are parsing all fields that the PostForm model have to our view as html form fields that a user should fill
    form_class = PostForm
# connecting the form to the post model so that the information recieved from the user can be saved into the table
    model = Post
# the following view is connected to the post_edit html file, it allows a user to update the post
class PostUpdateView(LoginRequiredMixin,UpdateView):
    # the user need to login first before they can make any changes to the post
    login_url = '/login/'
    # After some changes have take place the user is going to be redirected to another page
    redirect_field_name = 'blog/post_detail.html'
# the user will have all fields the PostForm modelForm have to update
    form_class = PostForm
# the view is connected to the model "Post"
    model = Post
# this class_base_view it is created to redirect a user to htm post_list page after the comment have bee deleted t
class PostDeleteView(LoginRequiredMixin,DeleteView):
    # connecting to the database because we'll be deleting from the database
    model = Post
    # redirecting a user to post_list page "Homepage" after deleting something in the database
    success_url = reverse_lazy('post_list')
# this class base view takes unsaved post to database but save it as draft
class DraftListView(LoginRequiredMixin,ListView):
    # super user should login to manipulate this view
    login_url = '/login/'
    # After some changes has been done, the user should be redirected to another page
    redirect_field_name = 'blog/post_list.html'
    # conneting to the model
    model = Post

# selecting every post insde the database that is saved as draft
    def get_queryset(self):
       return Post.objects.filter(published_date__isnull=True).order_by('created_date')




#####################################################
#####################################################
#####################################################
# the followingfunction is used to publish the post and only the super user have the ability to create and publish the post
@login_required
def post_publish(request,pk):
    # The following line is a shortcut that can save you the trouble of writing redundant code every time you need to query a particular object from the database.
    post = get_object_or_404(Post,pk=pk)
    # publishing the post 'pushing/commiting a post to the database'
    post.publish()
    # redirect the user to "Homepage" post_detail after publishing the post
    return redirect('post_detail',pk=pk)


#
@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
# Here we'll be checking if the user entered the correct/required data in the form
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            #comment.object = post
            # saving data to the database
            comment.save()
            # redirecting to the next page
            return redirect('post_detail',pk=post.pk)
# if the inserted/inputted data is no valid the user will be asked to re-enter the valid info
    else:
        form = CommentForm
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
#
def comment_approved(request,pk):
    # The following line is a shortcut that can save you the trouble of writing redundant code every time you need to query a particular object from the database.
    comment = get_object_or_404(Comment,pk=pk)
    # calling approve method from the model Comment
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@ login_required
def comment_remove(request,pk):
# The following line is a shortcut that can save you the trouble of writing redundant code every time you need to query a particular object from the database.
    comment = get_object_or_404(Comment,pk=pk)
    # taking a primary key of the comment that the user wants to delete
    post_pk = comment.post.pk
    # deleting the comment
    comment.delete()
    # redirecting a user to another page after the comment have been deleted
    return redirect('post_detail',pk=post_pk)

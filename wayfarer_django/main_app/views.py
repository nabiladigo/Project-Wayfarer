from django.shortcuts import redirect, render
from django.views import View 
from django.views.generic.base import TemplateView
from .models import Country, City, Post, Comment, Profile
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# @method_decorator(login_required, name='dispatch')
class Home(TemplateView):
     template_name = "home.html"


# @method_decorator(login_required, name='dispatch')

class About(TemplateView):
    template_name = "about.html"
    
# @method_decorator(login_required, name='dispatch') 

class CityList(TemplateView):
    template_name ="city.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["cities"] = City.objects.ilter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["cities"] = City.objects.all()
            context["header"] = "The Perfect place to visit."
        
        return context 

class Posts(TemplateView):
    template_name ="post.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["posts"] = Post.objects.ilter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["posts"] = Post.objects.all()
            context["header"] = "The Perfect place to visit."
        
        return context 

class PostCreate(CreateView):
    model = Post
    fields = ['title','image', 'content', 'city']
    template_name = "post_create.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('post')

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostUpdate(UpdateView):
    model = Post
    fields = ['title','content', 'city']
    template_name = "post_update.html"

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = "/posts/"


class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            return redirect("profile")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

          
class Profile(DetailView):
    model = Profile
    template_name ="profile.html"

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['username','bio']
    template_name = "profile_update.html"
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})


class Caribbean(TemplateView):

    template_name ="city.html"

class Morocco(TemplateView):
    template_name ="city.html"

class France(TemplateView):
    template_name = "city.html"

class Ocean(TemplateView):
    template_name  = "city.html"

class Emirate(TemplateView):
    template_name ="city.html"






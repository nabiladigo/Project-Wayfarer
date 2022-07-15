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



class Home(TemplateView):
     template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class Post(TemplateView):
    template_name = "post.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["posts"] = Post.objects.filter(Country.objects.filter(user=self.request.user),name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["posts"] = Post.objects.filter(Country.objects.filter(user=self.request.user))
            context["header"] = "The Perfect City to visit."
        return context


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content','date']
    template_name = "post_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context

class PostUpdate(UpdateView):
    model = Post
    fields = ['title','content','date']
    template_name = "post_update.html"

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete_confirmation.html"
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


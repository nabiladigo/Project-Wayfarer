from django.shortcuts import redirect, render
from django.views import View 
from django.views.generic.base import TemplateView
from .models import Country, City
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

# class Country(TemplateView):
#     template_name = "country.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         name = self.request.GET.get("name")
#         if name != None:
#             context["countries"] = Country.objects.filter(Country.objects.filter(user=self.request.user),name__icontains=name)
#             context["header"] = f"Searching for {name}"
#         else:
#             context["countries"] = Country.objects.filter(Country.objects.filter(user=self.request.user))
#             context["header"] = "The Perfect Gift for Loved One."
#         return context


# class CountryCreate(CreateView):
#     model = Country
#     fields = ['name', 'image', 'price']
#     template_name = "country_create.html"

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(CountryCreate, self).form_valid(form)

#     def get_success_url(self):
#         print(self.kwargs)
#         return reverse('country_detail', kwargs={'pk': self.object.pk})

# class CountryDetail(DetailView):
#     model = Country
#     template_name = "country_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context["giftset"] = GiftSet.objects.all()
#         return context

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
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


from django.db.models import fields
from django.shortcuts import render, reverse
from .models import Category, Product, Subcategories, Letter,
from django.contrib.auth.models import User
from django.views import generic
from django.utils import timezone

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'Topshop/index.html'
    context_object_name = 'categories'
    def get_queryset(self):
        return Category.objects.all()

class CategoriesView(generic.ListView):
    model = Category
    template_name = 'Topshop/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()

class SubcategoriesView(generic.ListView):
    model = Subcategory
    template_name = 'Topshop/subcategories.html'
    context_object_name = 'subcategories'

    def get_queryset(self):
        return Subcategory.objects.all()

class ProductsView(generic.ListView):
    model = Product
    template_name = 'Topshop/products.html'
    context_object_name = 'products'
    def get_queryset(self):
        return Product.objects.all()
  #......................................................        

class CreateProductView(generic.edit.CreateView):
    fields = ['name', 'body', 'subcategory', 'product']
    template_name = 'Topshop/create_products.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('Topshop:index')

class UpdateProductView(generic.edit.UpdateView):
    fields = ['name', 'body', 'subcategory', 'product']
    template_name = 'Topshop/update_products.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('Topshop:index')
    
class DeleteProductView(generic.edit.DeleteView):
    fields = ['name', 'body', 'subcategory', 'product']
    template_name = 'Topshop/delete_products.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('Topshop:index')
  #......................................................  

class IndexRecieverLetterView(generic.ListView):
    model = 'reciever_letters'
    template_name = 'Topshop/reciever_letters.html'

    def get_queryset(self):
        return Letter.objects.all()

class IndexSenderLetterView(generic.ListView):
    model = 'sender_letters'
    template_name = 'Topshop/sender_letters.html'

    def get_queryset(self):
        return Letter.objects.all()

class DetailLetterView(generic.DetailView):
    model = Letter
    template_name = 'Topshop/detail_letters.html'

    def get_queryset(self):
        return Letter.objects.all()
  #...................................................... 

class CreateLetterView(generic.edit.CreateView):
    fields = ['reciever', 'body']
    template_name = 'Topshop/create_letters.html'

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('Topshop:index')

class UpdateLetterView(generic.edit.UpdateView):
    fields = ['reciever', 'body']
    template_name = 'Topshop/update_letters.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('Topshop:index')

class DeleteLetterView(generic.edit.DeleteView):
    fields = ['reciever', 'body']
    template_name = 'Topshop/delete_letters.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('Topshop:index')

class UpdateProfileView(generic.edit.UpdateView):
    model = Profile
    template_name = "Topshop/update_profile.html"
    fields = ['phonenumber']

    def get_success_url(self):
        return reverse('Topshop:index')

    def get_object(self):
        return get_object(Profile, user=self.request.user)
    
    def form_valid(self, form):
        form.instance.phonenumber = self.request.POST.get(key='phone')
        return super().form_valid(form)

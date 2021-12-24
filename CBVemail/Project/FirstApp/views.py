from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator

from .models import Laptop
from .forms import LaptopForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.views import View





class AddView(LoginRequiredMixin,View):
    def get(self,request):
        form =LaptopForm()
        context={'form':form}
        template_name='addlap.html'
        return render(request, template_name, context)
    def post(self,request):
        form=LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_lap')



class ShowView(LoginRequiredMixin,View):
    def get(self,request):
        laptop=Laptop.objects.all()
        context={'laptop':laptop}
        template_name='showlap.html'
        return render(request, template_name, context)

class DeleteView(View):
    def get(self,request,i):
        laptop = Laptop.objects.get(id=i)
        context = {'laptop': laptop}
        template_name = 'delete.html'
        return render(request, template_name, context)

    def post(self,request, i):
        laptop = Laptop.objects.get(id=i)
        laptop.delete()
        return redirect('show_lap')


class Update(View):
    def get(self,request,i):
        laptop = Laptop.objects.get(id=i)
        form =LaptopForm(instance=laptop)
        context = {'form': form}
        template_name = 'addlap.html'
        return render(request, template_name, context)
    def post(self,request,i):
        laptop = Laptop.objects.get(id=i)
        form =LaptopForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('show_lap')

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .form import ItemForm
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
   context={
      "item":Item.objects.all()
   }
   return render(request,"food/index.html",context)

def detail(request,item_id):
   context={
      "item":Item.objects.get(pk=item_id)
   }

   return render(request,"food/details.html",context)
   
def item_form(request):
   form=ItemForm(request.POST or None)

   if form.is_valid():
      form.save()
      return redirect('food:index')
   return render(request,"food/item-form.html",{"form":form})

class CreateItem(CreateView):
    model = Item
    fields= ["item_name","item_desc","item_price","item_image"]
    template_name = 'food/item-form.html'
    def form_valid(self,form):
       form.instance.user_name=self.request.user

def update_item(request,id):
   item=Item.objects.get(id=id)
   form=ItemForm(request.POST or None,instance=item)

   if form.is_valid():
      form.save()
      return redirect('food:index')
   return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
   item=Item.objects.get(id=id)
   if request.method =="POST":
      item.delete()
      return redirect('food:index')
   return render(request,'food/delete-item.html',{"item":item})


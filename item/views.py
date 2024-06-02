from django.shortcuts import render,get_object_or_404
from django.shortcuts import render,redirect
from .models import Item,category
from .form import NewItemForm,EditItemForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def detail(request,pk):
    item=get_object_or_404(Item,pk=pk)
    related_item=Item.objects.filter(Category=item.Category,is_sold=False).exclude(pk=pk)[0:3]

    return render(request,'details.html',{'item':item,'related_item':related_item})


@login_required
def new(request):
    if request.method=='POST':
      form=NewItemForm(request.POST,request.FILES)

      if form.is_valid():
         item=form.save(commit=False)
         item.created_by=request.user
         item.save()
         return redirect('item:detail',pk=item.id)
    else:     
       form=NewItemForm()
    return render(request,'form.html',{'form':form})



@login_required
def delete(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()
    return redirect('dashboard:dashboard')


@login_required
def edit(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    if request.method=='POST':
      form=EditItemForm(request.POST,request.FILES,instance=item)

      if form.is_valid():
         form.save()
         return redirect('item:detail',pk=item.id)
    else:     
       form=EditItemForm(instance=item)
    return render(request,'form.html',{'form':form})

def items(request):
   query=request.GET.get('query','')
   category_id=request.GET.get('category',0)
   categories=category.objects.all()
   items=Item.objects.filter(is_sold=False)
   if category_id:
      items=items.filter(Category_id=category_id)
   if query:
      items=items.filter(name__icontains=query)
   return render(request,'items.html',{'items':items,'query':query,'categories':categories,'category_id':int(category_id)})
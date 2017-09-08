from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.template import loader
from django.views import generic

from .models import User

# Create your views here.
def index(request):
    user_list=User.objects.order_by('-join_date')[:5]
    output=', '.join([u.username for u in user_list])
    return HttpResponse(output)

def help(request):
    return HttpResponse("this is the help page")

# def notice(request):
#     user_list=User.objects.order_by('-join_date')[:5]
#     context={'user_list':user_list}
#     return render(request,'points/notice.html',context)
# #     user_list=User.objects.order_by('-join_date')[:5]
# #     template=loader.get_template('points/notice.html')
# #     context={
# #         'user_list':user_list
# #     }
# #     return HttpResponse(template.render(context,request))
class NoticeView(generic.ListView):
    template_name='points/notice.html'
    context_object_name='user_list'
    
    def get_queryset(self):
        return User.objects.order_by('-join_date')[:5]

# def detail(request,user_id):
#     user=get_object_or_404(User,pk=user_id) # 直接使用get_object_or_404来处理，调用get()
#     return render(request,'points/detail.html',{'user':user})
# #     try:
# #         user=User.objects.get(pk=user_id)
# #     except User.DoesNotExist:
# #         raise Http404("User does not exist")
# #     return render(request,'points/detail.html',{'user':user})
class DetailView(generic.DetailView):
    model=User
    template_name="points/detail.html"

def edit(request,user_id):
    user=get_object_or_404(User,pk=user_id) # 直接使用get_object_or_404来处理，调用get()
    return render(request,'points/edit.html',{'user':user})

def submit(request,user_id):
    user=get_object_or_404(User,pk=user_id)
    user.points_set.create(value=request.POST['value'],deriver=request.POST['deriver'])
#     return render(request,'points/detail.html',{'user':user})
    return HttpResponseRedirect(reverse('points:detail', args=(user.id,))) # 使用重定向



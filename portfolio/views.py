# importing modules
from email import message
from operator import contains
from urllib import request
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.core.mail import send_mail
# from django.shortcuts import render_to_response




# import models
from .models import *
from .forms import ContactForm
# from blog.models import Post
# from blog.forms import CommentForm


# Create your views here.

#Global variables
config_name = "MY PORTFOLIO CONFIG"

@csrf_protect
def home_view(request):
    """
    function based view for home page

    Args:
        request:
    """
    user_info = get_object_or_404(User_info, Portfolio__Portfolio_name=config_name)
    personlization_info = get_object_or_404(Personlization, Portfolio__Portfolio_name=config_name)
    social_info = get_object_or_404(Social_info, Portfolio__Portfolio_name=config_name)
    services_info = get_list_or_404(Services, Portfolio__Portfolio_name=config_name)
    experience_info = Experience.objects.first()
    experience_info_work = Work.objects.all()
    experience_info_education = Education.objects.all()
    portfolio_info = 4
    profession = [i.strip() for i in user_info.profession.split(',')]
    contact_info = get_object_or_404(Contact, Portfolio__Portfolio_name="MY PORTFOLIO CONFIG")
    # blog_info = Post.objects.all()
    if request.method == 'GET':
        form = ContactForm()
        context = {'user_info': user_info, 'profession': profession,
                'social_info': social_info,
                'personlization_info': personlization_info,
                'services_info': services_info,
                'experience_info': experience_info,
                'experience_info_work': experience_info_work,
                'experience_info_education': experience_info_education,
                'portfolio_info': portfolio_info,
                'contact_info':contact_info,
                # 'blog_info':blog_info,
                'form':form,
                
                }
        return render(request, "Homepages/index.html", context)

    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # try:
            # sending email to portfolio owner
            send_mail('EMail From Personal Website',
            message,
            email,
            [Contact.objects.all().get(Portfolio__Portfolio_name="MY PORTFOLIO CONFIG").E_mail]
            )
                #django message not used cause i don't find it attractive at the moment
            # except Exception as e:
            #     print(e)
        else:
            message_sent = 'False'
        
        context = {'user_info': user_info, 'profession': profession,
               'social_info': social_info,
               'personlization_info': personlization_info,
               'services_info': services_info,
               'experience_info': experience_info,
               'experience_info_work': experience_info_work,
               'experience_info_education': experience_info_education,
               'portfolio_info': portfolio_info,
               'contact_info':contact_info,
               'form':form,
        }
        return render(request, "Homepages/index.html", context)



# def blog_view(request, slug , *args):
#     """
#     function based view for blog post details page

#     Args:
#         request:
#     """
#     user_info = get_object_or_404(User_info, Portfolio__Portfolio_name=config_name)
#     personlization_info = get_object_or_404(Personlization, Portfolio__Portfolio_name=config_name)
#     social_info = get_object_or_404(Social_info, Portfolio__Portfolio_name=config_name)
#     post_info = get_object_or_404(Post, slug=slug)

#     if request.method == 'GET':
#         # comment_form = CommentForm()
#         context = {'user_info': user_info,
#                'social_info': social_info,
#                'personlization_info': personlization_info,
#                 'post_info':post_info,
#                 # 'comment_form':comment_form,
#                }
#         return render(request, "Homepages/blog_single.html", context)
    
    # elif request.method == 'POST':
    #     comment_form = CommentForm(request.POST)
    #     if comment_form.is_valid():


def handler404(request, exception=None):
    context = {}
    return render(request, "error_404.html", context)

def handler500(request, exception=None):
    context = {}
    return render(request, "error_404.html", context)
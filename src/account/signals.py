import os
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.urls import reverse
from django.template import loader
from django.contrib import messages



def create_admin(sender, *args, **kwargs):
    if sender.models['user'].objects.count() == 0:
        u = sender.models['user'].objects.create_superuser(
            username=os.getenv('USERNAME'), email=os.getenv('EMAIL'), password=os.getenv('PASSWORD'))
        u.email_user('username and password',
                     f"USERNAME\t{os.getenv('USERNAME')}\nEmail\t{os.getenv('EMAIL')}\nPASSWORD\t{os.getenv('PASSWORD')}\nHappy Coodding!!!")
        print("User created")
    else:
        pass

@receiver(user_logged_in)
def user_is_login(request, user, **kwargs):
    data = {}
    data['ip']  = request.META.get('HTTP_X_FORWARDED_FOR')
    data['USER_AGENT'] = request.META['HTTP_USER_AGENT']
    data['user'] = user
    data['prourl'] = request.build_absolute_uri(user.prourl)
    data['login'] = request.build_absolute_uri(reverse('account:signin'))
    data['update'] = request.build_absolute_uri(user.get_update_url)
    body = loader.render_to_string("account/email/login.html", data)
    user.email_user("New Login at e_library", body, html_message=body)
    messages.success(request, 'You are Success to Login.')


@receiver(user_logged_out)
def user_is_logout(request, user, **kwargs):
    messages.success(request, 'You are Success to Logout.')


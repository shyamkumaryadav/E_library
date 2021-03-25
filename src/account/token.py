from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.utils.encoding import force_bytes
from django.urls import reverse_lazy


# https://raw.githubusercontent.com/LeoneBacciu/django-email-verification/master/email_flow.png

class EmailActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        login_timestamp = '' if user.last_login is None else user.last_login.replace(microsecond=0, tzinfo=None)
        return f"{user.pk}{login_timestamp}{user.is_active}{user.email}{timestamp}"

token_generator = EmailActivationTokenGenerator()

def send_mail(user, request=None, subject_template_name="account/email/subject.txt", email_template_name="account/email/body.html", html_email_template_name="account/email/body.html", from_email=None):
        """
        Send a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        to_email = getattr(user, 'email')
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)
        
        context= {
            'email': to_email,
            'uid': uid,
            'user': user,
            'token': token,
        }
        if request:
            context['url'] = request.build_absolute_uri(reverse_lazy('account:email_confirm', kwargs={'uid':uid, 'token':token}))
            
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')
        email_message.send()
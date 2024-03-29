from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail

# from django.core.mail import send_mail

# subject = 'Asunto del correo'
# message = 'Hola, este es un correo de prueba enviado desde Django.'
# email_from = 'tucorreo@gmail.com'  # Debes reemplazarlo con tu dirección de correo electrónico de Gmail
# recipient_list = ['destinatario1@example.com', 'destinatario2@example.com']

# send_mail(subject, message, email_from, recipient_list, fail_silently=False)



from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView
)

from django.views.generic.edit import (
    View,
    FormView
)

from .forms import (
    UserRegisterForm, 
    LoginForm,
    UpdatePasswordForm,
    VerificationForm
)

from .models import User

from .functions import code_generator


class UserRegisterView(FormView):
    template_name='users/register.html'
    form_class = UserRegisterForm
    success_url='/'
    
    def form_valid(self, form):
        
        # generamos el codigo aleatorio
        codigo = code_generator()
    
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero'],
            codregistro=codigo
        )
        
        # enviar el codigo al email del usuario
        asunto='Confirmación de Email'
        mensaje='Código de verificación: '+codigo
        email_remitente = 'correodemarcelopalacios@gmail.com'
        email_destino1 = 'correodemarcelopalacios@gmail.com'
        #email_destino1 = form.cleaned_data['email']
        send_mail(asunto,mensaje,email_remitente,[email_destino1,])
        # redirigir a pantalla de validacion
        return HttpResponseRedirect(
            reverse(
                'users_app:user-verification'
            )
        )
    
class LoginUser(FormView):
    template_name='users/login.html'
    form_class = LoginForm
    success_url=reverse_lazy('home_app:panel')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        
        return super(LoginUser, self).form_valid(form)    
    
class LogoutView(View):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )
        
 
class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name='users/update.html'
    form_class = UpdatePasswordForm
    success_url=reverse_lazy('users_app:user-login')
    login_url  =reverse_lazy('users_app:user-login')
    
    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1']
        )
        if user:
            new_password=form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
            
        logout(self.request)    
        return super(UpdatePasswordView, self).form_valid(form)        
    
class CodeVerificationView(FormView):
    template_name='users/verification.html'
    form_class = VerificationForm
    success_url=reverse_lazy('users_app:user-login')

    def form_valid(self, form):

        
        return super(CodeVerificationView, self).form_valid(form)  
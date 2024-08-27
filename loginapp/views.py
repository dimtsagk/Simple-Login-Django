from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import logout


# Αρχική σελίδα
def index(request):
    return render(request, 'index.html')

# Φόρμα Εγγραφής Χρήστη
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def custom_logout(request):
    logout(request)
    return redirect('/login/')


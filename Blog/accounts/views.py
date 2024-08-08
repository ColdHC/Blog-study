from django.shortcuts import render
from django.views import View

# Create your views here.
class LoginView(View):
    
    def get(self, request):
        context = {
            'title': 'Login',
            'sub_title': 'Login to your account',  
        }

        return render(request, 'login.html', context)
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

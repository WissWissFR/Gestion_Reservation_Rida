from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Evenement, Reservation
from django.views.generic import TemplateView
from django.contrib.auth import logout

# Create your views here.

class ConnexionView(TemplateView):
    template_name = 'home.html'
    
class RegisterView(TemplateView):
    template_name = 'register.html'

class ReservationView(TemplateView):
    template_name = 'reservation.html'
    
class EcoleView(TemplateView):
    template_name = 'ecole.html'

# def connexion_view(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('evenements')
#         else:
#             error_message = "Invalid email or password"
#             return render(request, 'home.html', {'error_message': error_message})
#     else:
#         return render(request, 'home.html')

def inscription_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('evenements')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def inscription_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('evenements')
    else:
        form = UserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')

def reservation_view(request):
    return render(request, 'reservation.html')

def reserver_view(request, evenement_id):
    evenement = get_object_or_404(Evenement, id=evenement_id)
    reservation = Reservation(evenement=evenement, user=request.user)
    reservation.save()
    return redirect('ecole')

def annuler_view(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    reservation.delete()
    return redirect('ecole')

def ecole_view(request):
    ecole = Ecole.objects.get(nom="Nom de l'école") # remplacez "Nom de l'école" par le nom de l'école concernée
    reservations = ecole.reservation_set.all()
    return render(request, 'ecole.html', {'reservations': reservations})

def logout_view(request):
    logout(request)
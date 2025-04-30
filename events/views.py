from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Event, Participation
from .forms import UserRegistrationForm, ParticipationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compte créé avec succès. Vous pouvez maintenant vous connecter.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        return redirect('event_list')
    return redirect('login')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    participation = None
    form = None
    
    if request.user.is_authenticated:
        participation, created = Participation.objects.get_or_create(
            event=event,
            user=request.user,
            defaults={'is_attending': False}
        )
        
        if request.method == 'POST':
            form = ParticipationForm(request.POST, instance=participation)
            if form.is_valid():
                form.save()
                messages.success(request, 'Votre choix a été enregistré.')
                return redirect('event_detail', event_id=event.id)
        else:
            form = ParticipationForm(instance=participation)
    
    context = {
        'event': event,
        'participation': participation,
        'form': form,
        'participant_count': event.participant_count
    }
    
    return render(request, 'events/event_detail.html', context)
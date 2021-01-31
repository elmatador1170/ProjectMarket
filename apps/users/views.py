from django.shortcuts import render, reverse
from .forms import CreateUser, UpdateInformation
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, Http404
from apps.project_market.models import Project, Review
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    """Der Besucher kann ein Konto anlegen und sich registrieren."""
    # Hier checken wir ab der Benutzer ein Formular anfordert oder seine Daten abschickt.
    if request.method != 'POST':
        form = CreateUser()
    else:
        # Das Formular wird vom Benutzer ausgefüllt und dann verarbeitet.
        form = CreateUser(data=request.POST)

        if form.is_valid():
            # Neuer Benutzer wird gespeichert.
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('project_market:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)


def logout_view(request):
    """Der Benutzer wird ausgeloggt."""
    logout(request)
    return HttpResponseRedirect(reverse('project_market:index'))


@login_required
def account(request):
    """Account des Benutzers und jegliche Informationen über ihn werden ausgegeben."""
    projects = Project.objects.filter(owner=request.user)
    reviews = Review.objects.filter(owner=request.user)
    number_of_projects = len(projects)
    number_of_reviews = len(reviews)
    pending_requests = 0

    context = {'projects': projects, 'number_of_projects': number_of_projects,
               'pending_requests': pending_requests, 'number_of_reviews': number_of_reviews}

    return render(request, 'users/account.html', context)


def add_user_info(request):
    """Kontoinformationen aktualisieren."""
    if request.method != 'POST':
        form = UpdateInformation(instance=request.user)
    else:
        form = UpdateInformation(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:account'))

    context = {'form': form}
    return render(request, 'users/update_info.html', context)

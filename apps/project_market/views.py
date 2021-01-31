from django.shortcuts import render, reverse
from .models import Project, Review
from .forms import ProjectForm, ReviewForm
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login_required


# Create your views here.
def index(request):
    return render(request, 'project_market/index.html')


def projects(request):
    projects = []

    for project in Project.objects.all().order_by('pub_date'):
        if request.user == project.owner or not project.is_private:
            projects.append(project)

    context = {'projects': projects}
    return render(request, 'project_market/projects.html', context)


def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    reviews = Review.objects.filter(parent=project)
    context = {'project': project, 'reviews': reviews}
    return render(request, 'project_market/project.html', context)


def new_project(request):
    """"Neues Projekt erstellen."""

    if request.method != 'POST':
        form = ProjectForm()
    else:
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            new_project_ = form.save(commit=False)
            new_project_.owner = request.user
            new_project_.save()
            return HttpResponseRedirect(reverse('project_market:projects'))

    context = {'form': form}
    return render(request, 'project_market/new_project.html', context)


def edit_project(request, project_id):
    project = Project.objects.get(pk=project_id)

    if request.method != 'POST':
        form = ProjectForm(instance=project)
    else:
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('project_market:project', args=[project_id]))

    context = {'form': form, 'project': project}
    return render(request, 'project_market/edit_project.html', context)


def delete_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    project.delete()
    return HttpResponseRedirect(reverse('project_market:projects'))


def review_project(request, project_id):
    project = Project.objects.get(pk=project_id)

    if request.method != 'POST':
        form = ReviewForm()
    else:
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.parent = project
            review.owner = request.user
            review.save()
            return HttpResponseRedirect(reverse('project_market:project', args=[project_id]))

    context = {'form': form, 'project': project}
    return render(request, 'project_market/review_project.html', context)



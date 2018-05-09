from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

 # Create your views here.

def index(request):
    return render(request, 'index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    category = Category.objects.order_by('order')
    context = {'topics': topics, 'category' : category}
    return render(request, 'forums/topics.html', context)



def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    category = topic.category

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries, 'category' : category}
    return render(request, 'forums/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('forum:topics'))

    context = {'form': form}
    return render(request, 'forums/new_topic.html', context)

def view_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    try:
        comment = Comments.objects.filter(entry= entry_id).order_by('-date_added')
    except Comments.DoesNotExist:
        comment = None

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            view_entry = form.save(commit=False)
            view_entry.entry = entry
            view_entry.owner = request.user
            view_entry.save()
            return HttpResponseRedirect(reverse('forum:view_entry', args=[entry_id]))

    context = {'form': form,'topic': topic, 'entry': entry, 'comment': comment}
    return render(request, 'forums/view_entry.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id = topic_id)

    if request.method != 'POST':
        #No Data Submitted
        form = EntryForm()
    else:
        #Data Submitted; process the data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('forum:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'forums/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if entry.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance = entry)
    else:
        form = EntryForm(instance = entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('forum:view_entry', args=[entry.id]))

    context = {'form': form, 'entry': entry, 'topic': topic}
    return render(request, 'forums/edit_entry.html', context)

def deleted_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    if entry.owner != request.user:
        return  HttpResponseRedirect('forum:disallowed')
    else:
        entry.delete()
        
    context = {'entry': entry}
    return render(request, 'forums/deleted_entry.html', context)
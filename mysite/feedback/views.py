from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import widgets
from django import forms

# Create your views here.
from .models import Feedback

class FeedbackView(LoginRequiredMixin, CreateView):
    model = Feedback
    template_name = 'feedback/index.html'
    fields = ['topic', 'user', 'grade','good', 'bad', 'ideas']

    success_url = 'thanks/'


class FeedbackForm(forms.Form):
    TOPIC_CHOICES = ( 
    (1,"Ruoka"), 
    (2,"Palvelu"), 
    (3,"Muu"), 
)

    GRADE_CHOICES = (
        (1,"1"),
        (1,"2"),
        (3,"3"),
        (4,"4"),
        (5,"5"),
)
    topic = forms.ChoiceField(choices=TOPIC_CHOICES, label='Aihe', widget=widgets.Select)
    grade = forms.ChoiceField(label='Arvosana 1-5', choices = GRADE_CHOICES)

    good = forms.CharField(label='Hyvää', max_length=500,
                           widget=forms.Textarea(attrs={'cols': '35', 'rows': '5'}))
    bad = forms.CharField(label='Huonoa', max_length=500,
                          widget=forms.Textarea(attrs={'cols': '35', 'rows': '5'}))
    ideas = forms.CharField(label='Ideoita', max_length=500,
                            widget=forms.Textarea(attrs={'cols': '35', 'rows': '5'}))


@login_required(login_url='/login/')
def feedback(request):
    user = request.user
    form = FeedbackForm(initial={'user':user})
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            topic = form.cleaned_data['topic']
            grade = form.cleaned_data['grade']
            good = form.cleaned_data['good']
            bad = form.cleaned_data['bad']
            ideas = form.cleaned_data['ideas']
            f = Feedback(user=user, topic=topic, grade=grade, good=good, bad=bad, ideas=ideas)
            f.save()
            # redirect to a new URL:
            return HttpResponseRedirect('thanks/')
    else:
        form = FeedbackForm()
        return render(request, 'feedback/index.html', {'form': form})
        
def thanks(request):
    return render(request, 'feedback/thanks.html', {})
                                                    
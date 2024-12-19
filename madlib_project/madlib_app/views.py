import random
from django.shortcuts import render
from .forms import MadLibForm
from .models import MadLib

def create_madlib(request):
    if request.method == 'POST':
        form = MadLibForm(request.POST)
        if form.is_valid():
            story = random.choice(MadLib.objects.all())

            filled_story = story.template.format(
                noun=form.cleaned_data['noun'],
                verb=form.cleaned_data['verb'],
                adjective=form.cleaned_data['adjective'],
                adverb=form.cleaned_data['adverb'],
                place=form.cleaned_data['place'],
                famous_person=form.cleaned_data['famous_person'],
                color=form.cleaned_data['color']
            )
            context = {'story': filled_story}
            return render(request, 'madlib_app/madlib_result.html', context)
    else:
        form = MadLibForm()
    return render(request, 'madlib_app/madlib_form.html', {'form': form})

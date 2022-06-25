from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
import json
import random
from .models import Subject, Question, Choice
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def choose_subject(request, subjectid):
    law = Subject.objects.all()
    const_law = Subject.objects.get(id=subjectid)
    const_law_tests = const_law.question_set.all()
    random_question = random.choice(const_law_tests)
    test_choices = random_question.choice_set.all()
    dict_test_choices = {}
    for choice in test_choices:
        text = choice.choice_text
        is_true = choice.is_correct
        dict_test_choices[text] = is_true
    list_dict_test_choices = dict_test_choices.items()

    context = {
        'law' : law,
        'question' : random_question,
        'choices' : dict_test_choices
    }
    
    return JsonResponse({"html": render_to_string("test.html", context, request=request)})
    #return render(request, 'index.html', context)

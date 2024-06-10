# from django.http import Http404
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render,HttpResponse
from django.urls import reverse
from django.views import generic
# from django.template import loader
from .models import Question, Choice

# from flask_ask import question


# def index(request):
#     return HttpResponse("<h1>Hello there, Welcome to this poll!</h1>")


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('mypollapp/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


class IndexView(generic.ListView):
    template_name = "mypollapp/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]
    

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "mypollapp/index.html", context)

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

#     try:
#         question = Question.objects.get(pk=question_id) 
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "mypollapp/detail.html", {"question": question})


class DetailView(generic.DetailView):
    model = Question
    template_name = "mypollapp/detail.html"


# def detail (request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'mypollapp/detail.html', {'question': question})



class ResultsView(generic.DetailView):
    model = Question
    template_name = "mypollapp/results.html"
    
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'mypollapp/results.html', {'question': question})



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "mypollapp/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("mypollapp:results", args=(question.id,)))

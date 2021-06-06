#English Modules

from django.shortcuts import render, redirect, reverse
from django.views.generic.list import ListView
from django.http import JsonResponse

from .models import *
from main.models import eng_quiz_result, eng_question_result

#Main Page
def main(request):
    if request.user.groups.filter(name='cheung_family').exists():
        return render(request, 'eng/main.html')
    else:
        return redirect('index')

class quiz_list(ListView):
    model = eng_quiz
    template_name = 'eng/eng_quiz_list.html'

    def test_func(self):
        return self.request.user.groups.filter(name='cheung_family').exists()
    
    def handle_no_permission(self):
        return redirect('index')

def quiz_view(request, pk):
    if request.user.groups.filter(name='cheung_family').exists():
        quiz = eng_quiz.objects.get(id = pk)
        return render(request, 'eng/eng_quiz.html', locals())
    else:
        return redirect('index')

def quiz_data_view(request, pk):
    quiz = eng_quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        #questions.append({str(q): answers})
        questions.append({'id':q.id, 'question':str(q), 'answers':answers})
    #print(questions)
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

def quiz_save_view(request, pk):
    if request.is_ajax():
        data = request.POST
        #print(data)
        data_ = dict(data.lists())
        #print(data_)

        data_.pop('csrfmiddlewaretoken')
        
        user = request.user
        quiz = eng_quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.no_of_questions
        results = []
        correct_answer = None

        for d_key, d_value in data_.items():
            
            question = eng_question.objects.get(id=d_key)
            if d_value[0] != "":
                
                question_answers = eng_answer.objects.filter(question=question)
                for a in question_answers:
                    question_correct = 0
                    if d_value[0] == a.text:
                        if a.correct:
                            score +=1 
                            correct_answer = a.text
                            question_correct = 1
                            break
                    else:
                        if a.correct:
                            correct_answer = a.text
                results.append({'id':d_key, 'correct': question_correct, 'correct_answer': correct_answer, 'answered': d_value[0]})
            else:
                results.append({'id':d_key, 'correct': 0, 'correct_answer': correct_answer, 'answered': d_value[0]})
        #print(results)
        score = score * multiplier
        #print(score)

        pass_score = quiz.pass_score

        if pass_score is None:
            pass_score = 0

        if score >= pass_score:
            quiz_pass = 1
        else:
            quiz_pass = 0

        quiz_result = eng_quiz_result.objects.create(quiz=quiz, user=user, score=score, quiz_pass=quiz_pass)

        for r in results:
            question = eng_question.objects.get(id=r['id'])
            eng_question_result.objects.create(user=user, quiz = quiz_result, question=question, correct = r['correct'], answer_selected=r['answered'], answer_correct=r['correct_answer'])
        print(quiz_result.id)
        #return redirect('eng-quiz-result-view', pk = quiz_result.id)
        return JsonResponse({'url': reverse('eng-quiz-result-view', args=[quiz_result.id])})

def quiz_result_view(request, pk):
    if request.user.groups.filter(name='cheung_family').exists():
        quiz = eng_quiz_result.objects.get(id = pk)
        quiz_question = eng_question_result.objects.filter(quiz=quiz)
        return render(request, 'eng/eng_quiz_result.html', locals())
    else:
        return redirect('index')
            

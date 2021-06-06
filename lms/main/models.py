from django.db import models
from django.contrib.auth.models import User
from learn_eng.models import eng_quiz, eng_question, eng_vocab

yes_no = (
    (0, 'N'), (1, 'Y'),
)

#User's profile
class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    picture = models.ImageField(upload_to = 'user', null=True, blank=True)
    family = models.CharField(max_length=120, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user) + ' profile'

    class Meta:
        verbose_name_plural = 'User Profile'

#Store Result
##English
class eng_quiz_result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(eng_quiz, on_delete=models.CASCADE)
    score = models.FloatField('分數', null=True, blank=True)
    quiz_pass = models.IntegerField(choices=yes_no, default = 0, null=True, blank=True)

    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.quiz) + ' by ' + str(self.user) + ': ' + str(self.quiz_pass)
    
    class Meta:
        verbose_name_plural = 'English Quiz Results'

class eng_question_result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(eng_question, on_delete=models.CASCADE)
    quiz = models.ForeignKey(eng_quiz_result, on_delete=models.CASCADE, null=True, blank=True)
    correct = models.IntegerField(choices=yes_no, default = 0, null=True, blank=True)
    answer_selected = models.CharField(max_length=120, null=True, blank=True)
    answer_correct = models.CharField(max_length=120, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.question) + ': ' + str(self.correct)
    
    class Meta:
        verbose_name_plural = 'English Quiz Question Results'

class eng_vocab_result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vocab = models.ForeignKey(eng_vocab, on_delete=models.CASCADE)
    correct = models.IntegerField(choices=yes_no, default = 0, null=True, blank=True)
    test_type = (
        (1, 'Read'), (2, 'Spell')
    )
    test = models.IntegerField(choices=test_type, default = 0, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.vocab) + ': ' + str(self.correct)
    
    class Meta:
        verbose_name_plural = 'English Vocabulary Results'


#User's Redeem Score
class redeem_type(models.Model):
    name = models.CharField(max_length=120)
    score = models.IntegerField(null=True, blank=True)
    type_choice = (
        (0, '初始積分'), (1, '增加積分'), (-1, '扣減積分'),
    )
    type = models.IntegerField(choices=type_choice)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) + ' (' + str(self.score) + ')'

    class Meta:
        verbose_name_plural = 'Redeem Type'

class redeem(models.Model):
    user = models.ForeignKey(user_profile, on_delete=models.CASCADE)
    type = models.ForeignKey(redeem_type, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    score = models.FloatField('積分', null=True, blank=True)
    content = models.CharField(max_length=120, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ': ' + str(self.type)

    class Meta:
        verbose_name_plural = 'Redeem Record'

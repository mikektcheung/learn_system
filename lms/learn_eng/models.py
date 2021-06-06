from django.db import models

# English Model

grade = (
    (1, 'K1'),
    (2, 'K2'),
    (3, 'K3'),
    (11, 'P1'),
    (12, 'P2'),
    (13, 'P3'),
)

class eng_quiz_topic(models.Model):
    name = models.CharField(max_length=120)
    remark = models.CharField(max_length=255, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_quizs(self):
        return self.eng_quiz_set.all()
    
    def get_questions(self):
        return self.eng_question_set.all()

    class Meta:
        verbose_name_plural = 'English Topics'



class eng_quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.ForeignKey(eng_quiz_topic, on_delete=models.CASCADE)
    content = models.TextField("題目內容", null=True, blank=True)
    picture = models.ImageField(upload_to = 'eng_quiz', null=True, blank=True)
    no_of_questions = models.IntegerField(null=True, blank=True)
    pass_score = models.IntegerField(help_text="合格分數", null=True, blank=True)
    time = models.IntegerField(help_text="Quiz時間")
    difficulty = models.IntegerField(choices=grade)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.topic}"
    
    def get_questions(self):
        return self.eng_question_set.all()

    class Meta:
        verbose_name_plural = 'English Quizes'

class eng_question(models.Model):
    text = models.CharField(max_length=200)
    picture = models.ImageField(upload_to = 'eng_quiz', null=True, blank=True)
    quiz = models.ForeignKey(eng_quiz, on_delete=models.CASCADE, null=True, blank=True)
    topic = models.ForeignKey(eng_quiz_topic, on_delete=models.CASCADE, null=True, blank=True)
    difficulty = models.IntegerField(choices=grade)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.eng_answer_set.all()

    class Meta:
        verbose_name_plural = 'English Questions'

class eng_answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(eng_question, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

class eng_vocab_topic(models.Model):
    name = models.CharField(max_length=120)
    remark = models.CharField(max_length=255, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'English Vocabulary Topic'



class eng_vocab(models.Model):
    vocab = models.CharField(max_length=200)
    topic = models.ForeignKey(eng_vocab_topic, on_delete=models.CASCADE, null=True, blank=True)
    difficulty = models.IntegerField(choices=grade)
    picture = models.ImageField(upload_to = 'eng_quiz', null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.vocab)
    
    class Meta:
        verbose_name_plural = 'English Vocabulary'
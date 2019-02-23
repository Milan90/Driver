from django.db import models


class Advice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_or_video = models.FileField(upload_to="videos/", blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created',)


class Quiz(models.Model):
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.advice.title


class QuizQuestion(models.Model):
    question = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Answers(models.Model):
    answer_text = models.CharField(max_length=150)
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images/answers/", blank=True)

    def __str__(self):
        return self.answer_text


class ForumQuestion(models.Model):
    question = models.TextField()
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class ForumAnswer(models.Model):
    answer = models.TextField()
    question = models.ForeignKey(ForumQuestion, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer

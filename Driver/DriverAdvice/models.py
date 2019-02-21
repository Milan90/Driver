from django.db import models


class Advice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created',)


class Images(models.Model):
    image = models.ImageField(upload_to="images/", blank=True)
    advice = models.ForeignKey(Advice, related_name='images', on_delete=models.CASCADE)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name


class Video(models.Model):
    video_file = models.FileField(upload_to="videos/", blank=True)
    advice = models.ForeignKey(Advice, related_name='videos', on_delete=models.CASCADE)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_file.name


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
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.answer_text


class ForumQuestion(models.Model):
    question = models.TextField()
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class ForumAnswer(models.Model):
    answer = models.TextField()
    question = models.ForeignKey(ForumQuestion, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

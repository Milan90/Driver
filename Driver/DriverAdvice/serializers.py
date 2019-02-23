from rest_framework import serializers
from .models import *


class AdviceSerializer(serializers.HyperlinkedModelSerializer):
    image_or_video = serializers.FileField(allow_empty_file=True, use_url=True, default='')

    class Meta:
        model = Advice
        fields = ('id', 'title', 'description', 'image_or_video',)


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = '__all__'


class QuizAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'


class ForumQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumQuestion
        fields = '__all__'


class ForumAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumAnswer
        fields = '__all__'

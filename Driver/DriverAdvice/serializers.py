from rest_framework import serializers
from .models import *


class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = '__all__'


class AdviceSerializer2(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    image = serializers.IntegerField()
    video = serializers.FileField()

    def create(self, validated_data):
        title = validated_data.get('title')
        description = validated_data.get('description')
        advice = Advice.objects.create(title=title, description=description)
        try:
            image_file = validated_data.get('image')
            image = Images.objects.create(image=image_file, advice=advice)
        except Exception:
            pass
        try:
            video_file = validated_data.get('video')
            video = Video.objects.create(video_file=video_file, advice=advice)
        except Exception:
            pass

        return advice




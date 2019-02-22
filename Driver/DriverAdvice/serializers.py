from rest_framework import serializers
from .models import *


class AdviceSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_empty_file=True, use_url=True, default='')
    video = serializers.FileField(allow_empty_file=True, use_url=True, default='')

    class Meta:
        model = Advice
        fields = '__all__'


"""
    def create(self, validated_data):
        print("validated data:", validated_data)
        try:
            image_data = validated_data.pop('image')
        except KeyError:
            image_data = None
        try:
            video_data = validated_data.pop('video')
        except KeyError:
            video_data = None

        advice = Advice.objects.create(**validated_data)

        print("image:", image_data)
        if image_data:
            Images.objects.create(advice=advice, image=image_data)
        print("video:", video_data)
        if video_data:
            Video.objects.create(advice=advice, video_file=video_data)

        return advice
"""

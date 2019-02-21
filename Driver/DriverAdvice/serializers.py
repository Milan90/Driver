from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class AdviceSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, required=False)
    video = VideoSerializer(many=True, required=False)

    class Meta:
        model = Advice
        fields = '__all__'

    def create(self, validated_data):
        try:
            images_data = validated_data.pop('images')
        except KeyError:
            images_data = None
        try:
            videos_data = validated_data.pop('video')
        except KeyError:
            videos_data = None

        advice = Advice.objects.create(**validated_data)

        if images_data:
            for image_data in images_data:
                Images.objects.create(advice=advice, **image_data)

        if videos_data:
            for video_data in videos_data:
                Video.objects.create(advice=advice, **video_data)

        return advice

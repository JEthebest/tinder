from rest_framework import serializers


from .models import Questionnaire, Like, Photo


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = (
            'id',
            'nickname',
            'name',
            'surname',
            'birthday',
            'gender',
            'description',
            'sex',
            'user',
            'phone'
        )


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'like',
            'dislike',
            'rating'
        )

        
class PhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            'image',
            'questionnaire'
        )
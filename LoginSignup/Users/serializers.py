from rest_framework import serializers
from .models import Question,Producer

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class ProducerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producer
        fields = '__all__'
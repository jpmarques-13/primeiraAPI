from rest_framework import serializers

from TestandoAPI.models import BlogPost


class  BlogPostSerializer(serializers.ModelSerializer):  #forms.ModelForm
    class Meta:
        model = BlogPost
        fields = [
            'pk',
            'user',
            'title',
            'content',
            'timestamp',
        ]
#converts to JSON
#validations for data passed

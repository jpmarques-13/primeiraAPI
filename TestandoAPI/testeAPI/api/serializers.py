from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from testeAPI.models import BlogPost


class  BlogPostSerializer(serializers.ModelSerializer):  #forms.ModelForm
    url             = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = BlogPost
        fields = [
            'url',
            'id',
            'user',
            'title',
            'content',
            'timestamp',
        ]
        read_only_fields = ['id', 'user']
#converts to JSON
#validations for data passed

    def get_url(self,obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

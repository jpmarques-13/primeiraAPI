#generic
from rest_framework import generics


from TestandoAPI.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostRudViews(generics.RetrieveUpdateDestroyAPIView):#DetailView
    pass
    lookup_field            = 'pk'  #Regular expression(r'^?P<pk>\d+')
    #queryset                = BlogPost.objects.all()
    serializer_class        = BlogPostSerializer
    

    def get_queryset(self):
        return BlogPost.objects.all()

    #def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return BlogPost.objects.get(pk=pk)

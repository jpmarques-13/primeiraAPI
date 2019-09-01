#generic
from rest_framework import generics, mixins
from django.db.models import Q
from .permissions import IsOwnerOrReadOnly

from testeAPI.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostRudViews(generics.RetrieveUpdateDestroyAPIView):#DetailView
    pass
    lookup_field            = 'pk'  #Regular expression(r'^?P<pk>\d+')
    #queryset                = BlogPost.objects.all()
    serializer_class        = BlogPostSerializer
    permissions_classes     = [IsOwnerOrReadOnly]


    def get_queryset(self):
        return BlogPost.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}

    #def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return BlogPost.objects.get(pk=pk)


class BlogPostAPIViews(mixins.CreateModelMixin, generics.ListAPIView):#DetailView
    pass
    lookup_field            = 'pk'  #Regular expression(r'^?P<pk>\d+')
    #queryset                = BlogPost.objects.all()
    serializer_class        = BlogPostSerializer


    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)|
            Q(content__icontains=query)).distinct()
        return qs

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}

    #def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return BlogPost.objects.get(pk=pk)

from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from blog.api.serializers import PostSerializer, UserSerializer
from blog.models import Post
from blango_auth.models import User
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    print('authentication_classes--', authentication_classes)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BlogPost

class PostApiView(APIView):
    def get(self, request, format=None):
        """Returns a list of all posts"""
        posts = []
        for post in BlogPost.objects.all():
            post_dict={"id":post.id, "title":post.title, "content":post.content, "thumbnail":post.thumbnail, "post_date":post.post_date}
            posts.append(post_dict)

        return Response(posts)

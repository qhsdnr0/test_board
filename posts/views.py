import json

from django.http  import JsonResponse
from django.views import View

from .models      import Post
from utils        import login_required

class PostView(View):
    @login_required
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            Post.objects.create(
                title   = data['title'],
                content = data['content'],
                user    = user,
            )

            return JsonResponse({'message' : 'CREATED'}, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

    def get(self, request):
        try:
            post      = Post.objects.all()
            limit     = int(request.GET.get('limit', 4))
            offset    = int(request.GET.get('offset', 0))
            post_info = post.values()[offset:limit+offset]

            return JsonResponse({'message' : 'SUCCESS', 'result' : list(post_info)}, status = 200)

        except Post.DoesNotExist:
            return JsonResponse({'message' : 'POST_DOES_NOT_EXIST'}, status = 400)

    @login_required
    def delete(self, request, post_id):
        try:
            user = request.user
            post = Post.objects.get(id=post_id)
            if not post.user == user:
                return JsonResponse({'message' : 'INVALID_USER'})

            post.delete()

            return JsonResponse({'message' : 'DELETED'}, status = 200)

        except Post.DoesNotExist:
            return JsonResponse({'message' : 'POST_DOES_NOT_EXIST'}, status = 400)

    @login_required
    def put(self, request, post_id):
        try:
            data = json.loads(request.body)
            user = request.user
            post = Post.objects.get(id=post_id)

            if not post.user == user:
                return JsonResponse({'message' : 'INVALID_USER'})

            post.title = data.get('title', post.title)
            post.content = data.get('content', post.content)
            post.save()

            return JsonResponse({'message' : 'UPDATED'}, status = 200)

        except Post.DoesNotExist:
            return JsonResponse({'message' : 'POST_DOES_NOT_EXIST'}, status = 400)

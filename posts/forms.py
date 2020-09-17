from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]
        labels = {
            'title': ('제목'),
            'content': ('내용'),
            'image': ('이미지'),
        }
        help_texts = {
            'title': ('제목을 입력해주세요.'),
            'content': ('내용을 입력해주세요.'),
        }
    def save(self, **kwarg):
        post = super().save(commit=False)
        post.user = kwarg.get('user', None)
        post.save()
        return post
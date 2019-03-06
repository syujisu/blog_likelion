# # Blog class를 기반으로 만들 것이기 때문에 blog 안에 forms.py를 만들어준 것! models.py 여기 있자너
# from django import forms
# from .models import Blog 

# class BlogPost(forms.ModelForm): 
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault('label_suffix', '')
#         super(BlogPost, self).__init__(*args, **kwargs)
        
#     class Meta:
#         model = Blog #blog 모델의
#         fields = ['title', 'body'] #title과 body를 입력받을 공간
#         labels = {
#             "title": "제목",
#             "body": "내용"
#         }

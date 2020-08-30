from django.conf import settings
from django.db import models
from django.utils import timezone


#models 는 Post가 장고 모델임을 의미함
# 장고는 Post가 데이터베이스에 저장되어야 한다는 것을 알게됨
class Post(models.Model) :
	'''
	models.CharField - 글자수가 제한된 텍스트를 정의하는 경우 이용 (ex. 글제목)
	models.TextField - 글자수에 제한이 없는 긴 텍스트 (ex.블로그 글)
	models.DateTimeField - 날짜와 시간 의미
	models.ForeignKey - 다른 모델에 대한 링크
	'''
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)


	#method이름은 _를 통해 구분해줌 
	#ex. calculate_average_price
	def publish (self) :
		self.published_date = timezone.now()
		self.save()





	#Post모델의 제목을 돌려줌
	def __str__(self) :
		return self.title


def approved_comments(self) :
   	return self.comments.filter(approved_comment = True)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

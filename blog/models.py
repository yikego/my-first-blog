from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
	# Post는 Model 임을 정의. 이로 인해 장고는 Post가 DB에 저장되어야 한다고 인식.
	# 모델 만든 후
	# python manage.py makemigrations blog (DB에 반영할수 있도록 mig파일을 생성)
	# python manage.py migrate blog (실제 모델 추가한것을 반영)
	# 해줄 것
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 다른모델의 링크란다. 그냥 외래키라고 하지.
	title = models.CharField(max_length=200)  # 글자수가 제한되는 경우 사용
	text = models.TextField()  # 글자수 제한이 없는 경우 (그래도 DB가 blob, clob이 아니면 제한해야하지 않을까?)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	# 이하 메서드 정의
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title

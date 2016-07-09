from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.utils import timezone


class Member(User):
	MEMBER_CHOICES = (
			('M', 'Member'),
			('O', 'Officer'),
			('C', 'Co_leader'),
			('L', 'Leader'), 
		)
	user_type=models.CharField(
		max_length=1,
		choices=MEMBER_CHOICES
	)
	photo=models.ImageField(blank=True) #todo resize

	def __str__(self):
		return "{0} {1} with username: {2} and type: {3}".format(self.first_name,
		 self.last_name, self.username, self.user_type)


class Rules(models.Model):
	content = models.CharField(max_length=1000)
	created_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
	date_created = models.DateTimeField(default=timezone.now)

	def setContent():
		pass
	def getContent():
		pass

	def __str__(self):
		return self.content

# ------------------------------------------


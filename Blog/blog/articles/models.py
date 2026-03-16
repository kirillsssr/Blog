from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.author}: {self.title}"

    def get_excerpt(self) -> str:
        return f"{self.text[:140]}..." if len(self.text) > 140 else self.text

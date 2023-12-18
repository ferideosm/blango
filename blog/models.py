from django.db import models
from django.conf import settings

class Tag(models.Model):
  values = models.TextField()

  class Meta:
      ordering = ["values"]

  def ___str__(self):
    return self.values


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True, db_index=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField(unique=True)
    summary = models.TextField(max_length=500)
    content = models.TextField()
    # tags = models.ManyToManyField(Tag, related_name="posts", null=True)
    value = models.TextField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
  created_at = models.DateTimeField(auto_now=True)
  creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True)
  content_object = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
  content = models.TextField(max_length=1000, )


class AuthorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.TextField()

    def __str__(self):
        return f"{self.__class__.__name__} object for {self.user}"
      
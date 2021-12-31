from django.db import models
from apps.users.models import Member


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    image = models.ImageField("Image", upload_to="blog", default="blog/default/Ruslan_Korneev.PNG", blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.identifier

    def save(self, *args, **kwargs):
        self.slug = slugify(self.identifier)
        super().save(*args, **kwargs)
        pass 



# class Post(models.Model):

#     STATUS_CHOICES = (
#         ("draft", "Draft"),
#         ("published", "Published")
#     )

#     # DB Fields
#     title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=300, unique=True, editable=False)
#     author = models.ForeignKey(
#         get_user_model(), on_delete=models.CASCADE, related_name="blog_posts"
#     )
#     body = models.TextField()

#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     status = models.CharField(
#         max_length=10, choices=STATUS_CHOICES, default="draft"
#     )

#     class Meta:
#         ordering = ("-publish",)

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super().save(*args, **kwargs)
#         pass 

#     def __str__(self):
#         return self.title
    
#     def get_absolute_url(self):
#         return reverse("blog:post_detail", kwargs={"slug": self.slug})





    # STATUS_CHOICES = (
    #     ("draft", "Draft"),
    #     ("published", "Published")
    # )

    # DB Fields
    # status = models.CharField(
    #     max_length=10, choices=STATUS_CHOICES, default="draft"
    # )

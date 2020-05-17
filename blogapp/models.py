from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class ArticleManager(models.Manager):
    def get_articles(self):
        return super(ArticleManager, self).get_articles().filter(status='active')

class Article(models.Model):
    STATUS_OPTIONS = ( ('active', 'Active'), ('notactive', 'Notactive') )

    title = models.CharField(max_length=255)

    slug = models.SlugField(max_length=250,
                            unique_for_date='created')

    writer = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name='articles')

    body = models.TextField()

    created = models.DateTimeField(default=timezone.now)

    status = models.CharField(max_length=9,
                            choices=STATUS_OPTIONS)

    picture = models.CharField(max_length=40)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogapp:article_full',
                        args = [self.slug])

    def get_picture(self):
        return '../../static/img/'+self.picture

    objects = models.Manager()
    active = ArticleManager()

class Comment(models.Model):
    ACTIVE_CHOICES = (
        ('Yes', 'yes'),
        ('No', 'no'),
    )

    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name="comments")
    name = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.CharField(max_length=3,
                            choices= ACTIVE_CHOICES)

    class Meta():
        ordering = ('-created',)

    def __str__(self):
        return f"comment by {self.name} on {self.created}"
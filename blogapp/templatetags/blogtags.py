from django import template
from ..models import Article

register = template.Library()

@register.inclusion_tag('blogapp/article/links.html')
def show_links():
    links = Article.active.order_by('-created')[:4]
    return {'links': links}
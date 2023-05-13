from django import template
from django.urls import resolve

register = template.Library()


@register.inclusion_tag('nav.html', takes_context=True)
def navigation(context):
    request = context['request']
    namespace, url_name = resolve(request.path_info).namespace, resolve(request.path_info).url_name
    active = f'{namespace}:{url_name}'
    if request.user.is_authenticated:
        nav_links = [
            {'url': 'users:profile', 'label': request.user},
            {'url': 'users:logout', 'label': 'Выйти'},
        ]
    else:
        nav_links = [
            {'url': 'users:login', 'label': 'Войти'},
            {'url': 'users:register', 'label': 'Зарегистрироваться'},
        ]
    for link in nav_links:
        link['is_active'] = True if active == link['url'] else False

    return {'nav_links': nav_links, 'request': request}

from django import template
from ..models import Menu
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = Menu.objects.filter(menu_name=menu_name, parent__isnull=True).prefetch_related('children')
    return mark_safe(render_menu(menu_items, request.path))


def render_menu(menu_items, current_path, level=0, target_level=1000):
    html = f'<ul class="level-{level}">'

    for item in menu_items:
        css_class = "active" if current_path == item.url else ''
        target_level = level if current_path == item.url else target_level
        html += f'<li><a class="{css_class}" href="{item.url}">{item.title}</a>'

        if (item.children.exists() and
           level <= target_level and
           ((current_path in item.url) or (item.url in current_path)) and
           current_path != '/'):

            html += render_menu(item.children.all(), current_path, level + 1, target_level)

        html += '</li>'
    html += '</ul>'
    return html

from django import template
from minerals.models import Mineral

register = template.Library()

@register.inclusion_tag('minerals/mineral_group_nav.html')
def nav_group_list():
    '''Dictionary of mineral groups for display on nav pane'''
    groups = []
    minerals = Mineral.objects.all()
    for mineral in minerals:
        if mineral.group not in groups:
            groups.append(mineral.group)
    group_count = int(len(groups))
    return {'group_count':group_count}

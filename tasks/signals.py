from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from tasks.models import TodoItem, Category, Priority
from collections import Counter
from django.db.models import Count
from django.db.models import F

@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats_added(sender, instance, action, model, **kwargs):
    if action in ["pre_add", "pre_remove"]:
        for cat in instance.category.all():
            slug = cat.slug
            Category.objects.filter(slug=slug).update(todos_count=F('todos_count') - 1)

    if action in ["post_add", "post_remove"] :
        for cat in instance.category.all():
            slug = cat.slug
            Category.objects.filter(slug=slug).update(todos_count=F('todos_count') + 1)


@receiver(post_save, sender=TodoItem)
def save_todoitem(sender, instance, **kwargs):
    result = (TodoItem.objects
        .values('priority')
        .annotate(total=Count('id')))

    no_pry=[r['priority'] for r in result]
    Priority.objects.all().exclude(item__in=no_pry).update(todos_count=0)

    for res in result:
        obj, created = Priority.objects.get_or_create(
            item = res['priority'],
            todos_count =  res['total'],
        )
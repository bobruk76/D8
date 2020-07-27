from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from tasks.models import TodoItem, Category, Priority
from collections import Counter
from django.db.models import Count

@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats_added(sender, instance, action, model, **kwargs):
    if action != "post_add":
        return

    for cat in instance.category.all():
        slug = cat.slug

        new_count = 0
        for task in TodoItem.objects.all():
            new_count += task.category.filter(slug=slug).count()

        Category.objects.filter(slug=slug).update(todos_count=new_count)


@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats_removed(sender, instance, action, model, **kwargs):
    if action == "post_remove":
        cat_counter = Counter()
        for t in TodoItem.objects.all():
            for cat in t.category.all():
                cat_counter[cat.slug] += 1

        for slug, new_count in cat_counter.items():
            Category.objects.filter(slug=slug).update(todos_count=new_count)


    if action == "pre_remove":
        for cat in instance.category.all():
            slug = cat.slug
            Category.objects.filter(slug=slug).update(todos_count=0)


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
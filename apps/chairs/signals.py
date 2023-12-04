from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal
from apps.chairs.models import Chair

@receiver(post_save, sender=Chair)
def update_discounted_price(sender, instance, **kwargs):
    update_fields = kwargs.get('update_fields')
    if update_fields is None or 'discounted_price' not in update_fields:
        print(f"Сигнал получен для стула с id = {instance.pk}")
        instance.discounted_price = instance.price * (Decimal(1) - instance.discount / Decimal(100))
        instance.save(update_fields=['discounted_price'])

post_save.connect(update_discounted_price, sender=Chair)



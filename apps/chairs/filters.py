from django_filters import FilterSet, NumberFilter, ChoiceFilter

from .models import Chair

class ChairFilter(FilterSet):
    price_min = NumberFilter(field_name='price', lookup_expr='gte', label="Минимальная цена")
    price_max = NumberFilter(field_name='price', lookup_expr='lte', label="Максимальная цена")
    discount_range = ChoiceFilter(
        field_name='discount',
        choices=[(10, '10%'), (30, '30%'), (50, '50%')],
        lookup_expr='gte',
        label='Скидка',
    )

    class Meta:
        model = Chair
        fields = ('price_min', 'price_max')
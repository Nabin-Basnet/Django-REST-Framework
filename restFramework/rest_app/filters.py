import django_filters
from .models import Address

class AddressFilter(django_filters.FilterSet):
    district = django_filters.CharFilter(lookup_expr='iexact')  # case-insensitive exact match
    city = django_filters.CharFilter(lookup_expr='iexact')      # case-insensitive exact match
    id=django_filters.RangeFilter(field_name='id')
    add_min=django_filters.CharFilter(method="filter_by_id_range",label='from address num')
    add_max=django_filters.CharFilter(method="filter_by_id_range",label='to address num')
    class Meta:
        model=Address
        fields=['district','city','id','add_min','add_max']
    

    def filter_by_id_range(self,queryset,name,value):
        if name=='add_min':
            return queryset.filter(add_num__gte=value)
        elif name=='add_max':
            return queryset.filter(add_num__lte=value)
        return queryset
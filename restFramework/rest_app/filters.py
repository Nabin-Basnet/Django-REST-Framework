import django_filters
from .models import Address

class AddressFilter(django_filters.FilterSet):
    district = django_filters.CharFilter(lookup_expr='iexact')  # case-insensitive exact match
    city = django_filters.CharFilter(lookup_expr='iexact')      # case-insensitive exact match
    class Meta:
        model=Address
        fields=['district','city']
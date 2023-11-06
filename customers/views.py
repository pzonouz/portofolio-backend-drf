from rest_framework.generics import ListAPIView

from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

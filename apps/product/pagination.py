from rest_framework.pagination import PageNumberPagination

class ProductsPagination(PageNumberPagination):
  page_size = 10
  page_query_param = 'p'
from rest_framework.pagination import PageNumberPagination


class StandardPagination(PageNumberPagination):
    """ Standard pagination """
    page_size_query_param = 'page_size'
    page_size = 10
    max_page_size = 100

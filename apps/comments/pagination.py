from rest_framework.pagination import PageNumberPagination
from rest_framework.utils.urls import replace_query_param

class CommentsPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    
    # Construye la ruta de paginacion a la vista de obtener los comentaros de un producto
    def get_next_link(self):
        if not self.page.has_next():
            return None
        url = self.request.build_absolute_uri()
        new_url = url.replace('products', 'comment')
        page_number = self.page.next_page_number()
        
        return replace_query_param(
            new_url, 
            self.page_query_param, 
            page_number
        )
        
      

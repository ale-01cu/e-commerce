from apps.product.serializers import ProductSerializerList
import numpy as np
from django.db.models import Case, CharField, When
from .recommendations import RelatedProductsSystem
from rest_framework import views, status
from rest_framework.response import Response

# Recive el id de un producto y devuelve los productos similares
class RelatedProductAPIView(views.APIView):

    def get_serializer_class(self):
        return ProductSerializerList

    def get_queryset(self, pk=None):
        if pk:
            return self.get_serializer_class().Meta.model.objects.filter(
                pk=pk,
                status=True, 
                stock__gt=0
            ).first()
            
        return None

    def get(self, request, product_id=None, k=5): 
        if not product_id:
            return Response(
                {'error': 'Product id not recived'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
           
        try:
            product = self.get_queryset(product_id)
            product_serializer = self.get_serializer_class()
            
            if not product:
                return Response(
                    status=status.HTTP_404_NOT_FOUND
                )
            # k son la cantidad de productos parecidos que quiero
            # Leer el archivo CSV de los índices ordenados
            # Leer el archivo CSV de las similitudes ordenadas
            recommendationSystemInstance = RelatedProductsSystem()
            recommendationSystemInstance.load_model()
            order_product_cosine_sim_by_row = recommendationSystemInstance.get_order_product_cosine_sim_by_row()
            cosine_sims_sorted = recommendationSystemInstance.get_cosine_sims_sorted()
            dict_products_index = recommendationSystemInstance.get_dict_products_index()
            dict_index_products = recommendationSystemInstance.get_dict_index_products()
            
            if order_product_cosine_sim_by_row is not None and cosine_sims_sorted is not None:
                cosine_sims_row = dict_products_index[product_id]
                sorted_list_sim_products = order_product_cosine_sim_by_row[cosine_sims_row]
                sorted_list_sim = cosine_sims_sorted[cosine_sims_row]
                top_k = sorted_list_sim_products[:k]
                cosine_sims_top_k = sorted_list_sim[:k]
                
                product_ids = [
                    dict_index_products[i] 
                    for i, similarity in zip(top_k, cosine_sims_top_k) 
                    if not (np.isnan(similarity) or (similarity == -0.0))
                ]

                # Obtener los objetos Producto correspondientes a los PKs
                ordering = Case(
                    *[When(id=product_id, then=pos) for pos, product_id in enumerate(product_ids)],
                    output_field=CharField()
                )
                # Ordena los productos segón el orden de product_ids
                sorted_products = product_serializer.Meta.model.objects.filter(
                    id__in=product_ids).order_by(ordering)
                
                serializerProducts = product_serializer(sorted_products, many=True)

                # Agrega la similitud a cada producto
                for i, s in zip(serializerProducts.data, cosine_sims_top_k):
                    i['similitud'] = s
                    
                return Response(
                    serializerProducts.data,
                    status=status.HTTP_200_OK
                )
                
            else:
                return Response(
                    status=status.HTTP_204_NO_CONTENT
                )

        except Exception as e:
            print(f"Error al obtener los productos relacionados al producto: {product.name}", e)
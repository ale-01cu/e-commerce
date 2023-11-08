from django.db import models

class Searches(models.Model):
    class Meta:
        verbose_name = 'Busqueda'
        verbose_name_plural = 'Busquedas'
        ordering = ('-number_searches', )               # Ordena los elemntos por el numero de veces buscada
        
    search_text = models.CharField(                     # Texto de la busqueda
        max_length=255,
        verbose_name='Texto de la busqueda'
    )
    
    processed_search_text = models.CharField(           # Texto de la busqueda procesado
        max_length=255,
        verbose_name='Texto de la busqueda procesado'
    )
    
    number_searches = models.PositiveIntegerField(      # Cantidad de veces de realizada la busqueda
        verbose_name='Numero de busquedas',
        default=1
    )
    
    last_time_searched = models.DateTimeField(          # Ultima vez que fue buscada
        verbose_name='Fecha de creado',
        auto_now=True
    )
    
    # Metodo para actualizar el modelo de las busquedas
    # (si no esta la busqueda la crea y si esta actualiza el campo number_searches)
    @classmethod
    def model_update(self, search_terms: list, processed_search_terms: list) -> None:
        try:
            search_text = " ".join(search_terms)
            processed_search_text = " ".join(processed_search_terms)
            instance = Searches.objects.filter(
                processed_search_text=processed_search_text
            ).first()
            
            if instance:
                instance.number_searches += 1
                instance.save()
            else:
                new_instance = Searches.objects.create(
                    search_text=search_text,
                    processed_search_text=processed_search_text
                )
                new_instance.save()
                
        except Exception as e:
            print("Error al actualizar el modelo de las Busquedas ", e)
    
    def __str__(self):
        return self.search_text
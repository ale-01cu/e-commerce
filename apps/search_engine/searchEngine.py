from rest_framework import filters
from django.db import models
from functools import reduce
import operator
from rest_framework.compat import distinct
from nltk.corpus import stopwords
from nltk.tokenize import regexp_tokenize
from nltk.stem import SnowballStemmer
from .models import Searches

# Clase para realizar la busqueda de los productos
class SearchEngine(filters.SearchFilter):
    # Metodo para procesar el texto de la busqueda
    def text_process(self, text):
        stop_words = set(stopwords.words('spanish'))
        pattern = r'\w+|[^\w\s]'
        tokens = regexp_tokenize(text, pattern)
        stemmer = SnowballStemmer('spanish')
        clean_tokens =  set([ 
            stemmer.stem(token.lower()) 
            for token in tokens 
            if token.isalnum() and token.lower() not in stop_words 
        ])
        return list(clean_tokens)
    
    # Metodo para realizar la busqueda
    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_search_fields(view, request)
        search_terms = self.get_search_terms(request)
        processed_search_terms = self.text_process(" ".join(search_terms))

        if not search_fields or not search_terms:
            return queryset

        orm_lookups = [
            self.construct_search(str(search_field))
            for search_field in search_fields
        ]

        base = queryset
        conditions = []
        for search_term in processed_search_terms:
            queries = [
                models.Q(**{orm_lookup: search_term})
                for orm_lookup in orm_lookups
            ]
            conditions.append(reduce(operator.or_, queries))
        queryset = queryset.filter(reduce(operator.and_, conditions))

        if self.must_call_distinct(queryset, search_fields):
            queryset = distinct(queryset, base)
            
        # Actualiza el modelo con la nueva busqueda
        Searches.model_update(search_terms, processed_search_terms)
        return queryset
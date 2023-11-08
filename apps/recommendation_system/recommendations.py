from nltk.corpus import stopwords
from nltk.tokenize import regexp_tokenize
from nltk.stem import SnowballStemmer
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from apps.product.models import Product

# Sistema de recomendaciones basado en contenido para productos relacionados
class RelatedProductsSystem:
    def __init__(self) -> None:
        self.ids_products_list = Product.objects.values_list('id', flat=True)

        self.dict_index_products = dict(enumerate(self.ids_products_list))
        self.dict_products_index = dict(
            zip(
                self.dict_index_products.values(), 
                self.dict_index_products.keys()
            )
        )

        self.products_names = None
        self.products_descriptions = None
        self.products_brands = None
        self.products_keywords = None 
        self.products_category = None

        # Variables necesarias para el Procesamiento de lenguaje naturañ
        self.stop_words = set(stopwords.words('spanish'))
        self.pattern = r'\w+|[^\w\s]'
        self.stemmer = SnowballStemmer('spanish')
        
        self.order_product_cosine_sim_by_row = None
        self.cosine_sims_sorted = None
        
        del self.ids_products_list


    def get_dict_index_products(self):
        return self.dict_index_products
    
    
    def get_dict_products_index(self):
        return self.dict_products_index
    
    
    def get_order_product_cosine_sim_by_row(self):
        return self.order_product_cosine_sim_by_row
    
    
    def get_cosine_sims_sorted(self):
        return self.cosine_sims_sorted
    
    
    def update_dicts_index(self, new_product_id):
        keys = list(self.dict_index_products.keys())
        new_index = 0
        
        if keys:
            last_index = list(self.dict_index_products.keys())[-1]
            new_index = last_index + 1
            
        self.dict_index_products[new_index] = new_product_id
        self.dict_products_index[new_product_id] = new_index
        

    def preprocess_text(self, text):
        tokens = regexp_tokenize(text, self.pattern)
        clean_tokens = [
            self.stemmer.stem(token.lower()) 
            for token in tokens 
            if token.isalpha() and token.lower() not in self.stop_words 
        ]
        return " ".join(clean_tokens)


    def train_model(self):
        try:
            
            # Devuelve una lista con el contenido de cada campo de los productos de la BD
            self.products_names = Product.objects.values_list('name', flat=True)
            self.products_descriptions = Product.objects.values_list('description', flat=True)
            self.products_brands = Product.objects.values_list('brand__name', flat=True)
            self.products_keywords = Product.objects.values_list('keywords', flat=True)
            self.products_category = Product.objects.values_list('category__name', flat=True)
            
            
            # bag of words de cada campo
            names_counter = CountVectorizer(preprocessor=self.preprocess_text, min_df=1)
            names_counter.fit(self.products_names)
            names_bag_of_words = names_counter.fit_transform(self.products_names).toarray()
            names_col = [tup[0] for tup in sorted(names_counter.vocabulary_.items(), key=lambda x: x[1])]


            descriptions_counter = CountVectorizer(preprocessor=self.preprocess_text)
            descriptions_counter.fit(self.products_descriptions)
            descriptions_bag_of_words = descriptions_counter.fit_transform(self.products_descriptions).toarray()
            descriptions_col = [tup[0] for tup in sorted(descriptions_counter.vocabulary_.items(), key=lambda x: x[1])]


            brands_counter = CountVectorizer(preprocessor=self.preprocess_text)
            brands_counter.fit(self.products_brands)
            brands_bag_of_words = brands_counter.fit_transform(self.products_brands).toarray()
            brands_col = [tup[0] for tup in sorted(brands_counter.vocabulary_.items(), key=lambda x: x[1])]


            keywords_counter = CountVectorizer(preprocessor=self.preprocess_text)
            keywords_counter.fit(self.products_keywords)
            keywords_bag_of_words = keywords_counter.fit_transform(self.products_keywords).toarray()
            keywords_col = [tup[0] for tup in sorted(keywords_counter.vocabulary_.items(), key=lambda x: x[1])]


            category_counter = CountVectorizer(preprocessor=self.preprocess_text)
            category_counter.fit(self.products_category)
            category_bag_of_words = category_counter.fit_transform(self.products_category).toarray()
            category_col = [tup[0] for tup in sorted(category_counter.vocabulary_.items(), key=lambda x: x[1])]


            # concatenar ambos bag of words
            both_bag_of_words = np.hstack((
                names_bag_of_words, 
                descriptions_bag_of_words,
                brands_bag_of_words,
                keywords_bag_of_words,
                category_bag_of_words
            ))
            both_bag_of_words_df = pd.DataFrame(
                both_bag_of_words, 
                columns=names_col+descriptions_col+brands_col+keywords_col+category_col, 
                index=self.products_names
            )

            tf_idf = TfidfTransformer()

            tf_idf_products = tf_idf.fit_transform(both_bag_of_words_df).toarray()
            tf_idf_products_df = pd.DataFrame(
                tf_idf_products, 
                columns=names_col+descriptions_col+brands_col+keywords_col+category_col,
                index=self.products_names
            )

            # # calcular la similitud del coseno entre los productos
            cosine_sim = cosine_similarity(tf_idf_products_df)

            matrix_sim_df = pd.DataFrame(
                cosine_sim,
                index=self.products_names,
                columns=self.products_names
            )

            # eliminar la similitud de una pelicula consigo misma qeu siempre es del 100%
            np.fill_diagonal(matrix_sim_df.values, np.nan)

            # ordenar desde la mas similar a la menos por cada producto
            order_product_cosine_sim_by_row = np.argsort((-cosine_sim), axis=1)
            cosine_sims_sorted = np.sort(-cosine_sim, axis=1)

            # guardar los archivos CSV de los índices ordenados y las similitudes ordenadas
            df_index_sorted = pd.DataFrame(order_product_cosine_sim_by_row)
            df_index_sorted.to_csv('apps/recommendation_system/data/ordered_indexes.csv', index=False)

            df_sims_sorteds = pd.DataFrame(cosine_sims_sorted)
            df_sims_sorteds.to_csv('apps/recommendation_system/data/ordered_similarities.csv', index=False)
            
            print("Se actualizo el modelo de recomendaciones")
            
        except Exception as e:
            print(e)
            
    # Leer los archivos CSV de los índices ordenados y las similitudes ordenadas   
    def read_model(self):
        # Leer el archivo CSV de los índices ordenados
        df_index_sorted = pd.read_csv('apps/recommendation_system/data/ordered_indexes.csv')
        self.order_product_cosine_sim_by_row = df_index_sorted.values
        # Leer el archivo CSV de las similitudes ordenadas
        df_sims_sorted = pd.read_csv('apps/recommendation_system/data/ordered_similarities.csv')
        self.cosine_sims_sorted = df_sims_sorted.values
    
        equals_data = len(self.order_product_cosine_sim_by_row) == len(self.cosine_sims_sorted)
        if Product.objects.count() != 0 and not (equals_data and len(self.cosine_sims_sorted) == Product.objects.count()):
            self.train_model()
            self.read_model()
        
    # Cargar el modelo en memoria
    def load_model(self):
        try:
            self.read_model()
            
        except FileNotFoundError:
            if Product.objects.exists():
                self.train_model()
                self.read_model()
                
        except Exception as e:
            print("Error al cargar los modelos", e)


# Reentrena el modelo del sistema de recomendaciones
def re_train_model():
    RecommendationSystemInstance = RelatedProductsSystem()
    RecommendationSystemInstance.train_model()
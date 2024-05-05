# from django_elasticsearch_dsl import Document
# from django_elasticsearch_dsl.registries import registry
# from .models import Filmwork, Genre, Person


# @registry.register_document
# class FilmWorkDocument(Document):

#     class Index:
#         name = 'film'
#         settings = {'number_of_shards': 1, 'number_of_replicas': 0}
    
#     class Django:
#         model = Filmwork
#         fields = ['title', 'description']


# @registry.register_document
# class GenreDocument(Document):

#     class Index:
#         name = 'genre'
#         settings = {'number_of_shards': 1, 'number_of_replicas': 0}
    
#     class Django:
#         model = Genre
#         fields = ['name', 'description']


# @registry.register_document
# class PersonDocument(Document):

#     class Index:
#         name = 'person'
#         settings = {'number_of_shards': 1, 'number_of_replicas': 0}

#     class Django:
#         model = Person
#         fields = ['full_name']
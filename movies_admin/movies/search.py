from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch

# from .models import Filmwork, Genre, Person

connections.create_connection(hosts=['https://elasticsearch:9200'])

class FilmworkIndex(Document):
    title = Text()
    description = Text()

    class Meta:
        index = 'film'


class GenreIndex(Document):
    name = Text()
    description = Text()

    class Meta:
        index = 'genre'


class PersonIndex(Document):
    full_name = Text()

    class Meta:
        index = 'person'


# def bulk_films_indexing():
#     FilmworkIndex.init()
#     es = Elasticsearch()
#     bulk(client=es, actions=(b.indexing for b in Filmwork.objects.all().iterator()))


# def bulk_genre_indexing():
#     GenreIndex.init()
#     es = Elasticsearch()
#     bulk(client=es, actions=(b.indexing for b in Genre.objects.all().iterator()))


# def bulk_person_indexing():
#     PersonIndex.init()
#     es = Elasticsearch()
#     bulk(client=es, actions=(b.indexing for b in Person.objects.all().iterator()))
from typing import Any
from django.core.management.base import BaseCommand
from movies.models import Filmwork
from elasticsearch_dsl.connections import connections
from movies.documents import FilmWorkDocument


class Command(BaseCommand):
    help = 'Перенос данных из PostgreSQL в Elasticsearch'

    def handle(self, *args: Any, **options: Any) -> str | None:
        es = connections.create_connection(hosts=['http://elasticsearch:9200'], timeout=20)
        FilmWorkDocument.init() 

        for film in Filmwork.objects.all():
            film_document = FilmWorkDocument(meta={'id': film.id})
            film_document.title = film.title
            film_document.description = film.description
            film_document.save()
        
        self.stdout.write(self.style.SUCCESS('\nДанные успешно проиндексированы!\n'))
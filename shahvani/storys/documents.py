from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from shahvani.storys.models import StoryModel


@registry.register_document
class StoryDocument(Document):
    class Index:
        name = 'storys'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}
    
    class Django:
        model = StoryModel 
        fields = [
            'title',
            'content'
        ]
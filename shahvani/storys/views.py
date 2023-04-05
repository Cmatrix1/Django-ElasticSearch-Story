from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.db.models import Q 
from rest_framework.views import APIView
from rest_framework.response import Response

from shahvani.storys.models import StoryModel, TagModel
from shahvani.storys.documents import StoryDocument
from shahvani.storys.serilizers import StorySerializer

from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MultiMatch, Match
from django.http import JsonResponse

class DetailStoryView(DetailView):
    model = StoryModel
    template_name = "storys/detail.html"
    context_object_name = "story"


class ListStoryView(ListView):
    model = StoryModel
    template_name = "storys/list.html"
    context_object_name = "storys"
    paginate_by = 21


    def get_queryset(self):
        search = self.request.GET.get('q', '')
        if search:
            query = MultiMatch(query=search, fields=['title'], operator="and", fuzziness="1")
            s = StoryDocument.search().query(query)[:28].execute()

            hits = []
            for hit in s.hits:
                result = {
                    'id': hit.meta.id,
                    'title': hit.title,
                    'content': hit.content[:80]
                }
                hits.append(result)
            return hits
        return super().get_queryset()
    

    def render_to_response(self, context):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(context["object_list"], safe=False)
        else:
            return super().render_to_response(context)


class SearchView(APIView):
    def get(self, request):
        search = request.GET.get('q', '')
        query = Match(title=search)
        s = StoryDocument.search().query(query)[:10].execute()

        hits = []
        for hit in s.hits:
            result = {
                'title': hit.title
            }
            hits.append(result)

        return Response(hits)


# from django.template.defaultfilters import slugify
# json_file = open("shahvani\\storys\\all_data.json", "r", encoding="utf-8")
# storys = json.load(json_file)

# for index, story in enumerate(storys):
#     try:
#         story_obj = StoryModel.objects.get_or_create(title=story["title"], link=story["link"], content=story["content"])[0]
#         for tag in story["tags"]:
#             tag = TagModel.objects.get_or_create(title=tag)[0]
#             story_obj.tag.add(tag)
#             tag.save()
#             story_obj.save()
#         print("[+] Create Story", index)    
#     except:
#         print("[!] Erorr Story", index)    


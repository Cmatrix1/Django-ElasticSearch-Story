from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.db.models import Q 

from shahvani.storys.models import StoryModel, TagModel


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
        name = self.request.GET.get("s")
        if name:
            return super().get_queryset().filter(Q(title__icontains=name))
        return super().get_queryset()

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


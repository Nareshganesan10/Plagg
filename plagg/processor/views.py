from django.shortcuts import render
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from processor.serializers import FileSerializer
import wikipedia


@api_view(["GET"])
@csrf_exempt
def index(request):
    return Response("Yep, working")


@api_view(["GET", "POST"])
@csrf_exempt
def post_file(request):
    if request.method == "POST":
        text = (request.data).split(".")
        sentence_dict = {i+1: text[i] for i in range(len(text))}
        # wiki_wiki = wikipediaapi.Wikipedia('Plagg (nareshganesan83@gmail.com)','en')\
        for sentence_number in sentence_dict:
            result = wikipedia.search(sentence_dict[sentence_number])
            return Response(result)
            # print(sentence_dict[sentence_number])
            # print(str(result)[:-16])
            # if result:
            #     return Response(str(result))
            # else:
            #     return Response("what noooooooo")
    return Response(request.method)
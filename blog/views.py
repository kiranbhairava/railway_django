from django.shortcuts import render

# Create your views here.


# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Person
# from .serializers import PersonSerializer  # You'll need to create this serializer

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET'])
# def get_persons(request):
#     """
#     Retrieve a list of all persons.
#     """
#     persons = Person.objects.all()
#     serializer = PersonSerializer(persons, many=True)  # Use your serializer here
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_person(request):
#     """
#     Create a new person.
#     """
#     serializer = PersonSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def person_list(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
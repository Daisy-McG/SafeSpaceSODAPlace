from django.shortcuts import render
from django.contrib import messages
from .models import Topic, Comment

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializer, TopicSerializer


def discussions(request):
    """
    A view to return the 
    discussions page.
    """
    return render(request, "discussions/discussion.html")


@api_view(['GET'])
def topic_list(request):
    """
    REST framework for Django to serialize
    & return all topics in list form.
    """
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def topic_details(request, pk):
    """
    REST framework for Django to serialize
    & return a single topic details.
    """
    topic = Topic.objects.get(id=pk)
    serializer = TopicSerializer(topic, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def topic_create(request):
    """
    REST framework for Django to serialize
    & create a single topic.
    """
    serializer = TopicSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def topic_update(request, pk):
    """
    REST framework for Django to serialize
    & update a single topic details.
    """
    topic = Topic.objects.get(id=pk)
    serializer = TopicSerializer(instance=topic, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def topic_delete(request, pk):
    """
    REST framework for Django to serialize
    & delete a single topic.
    """
    topic = Topic.objects.get(topic_id=pk)
    topic.delete()

    messages.warning(request,('The topic is removed'))

    return Response('The topic is removed')


@api_view(['GET'])
def commentList(request):
    """
    REST framework for Django to serialize
    & return all comments in list form.
    """
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)

    return Response(serializer.data)

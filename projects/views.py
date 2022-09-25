from rest_framework import viewsets, permissions, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Project
from .serializers import ProjectSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('created_on')
    serializer_class = ProjectSerializer
    

class ProjectsList(ListAPIView):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    
    def get(self,request):
        queryset = Project.objects.all().order_by('created_on')
        serializer = ProjectSerializer(queryset,many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self,request):
        queryset = Project.objects.all().order_by('created_on')
        
        try:  
            if (request.data['tags'] != None and request.data['tags'] != [""] and type(request.data['tags'])==list):
                queryset = queryset.filter(tags__contains=request.data['tags'])
            else:
                None      
        except: None
        try:  
            if (request.data['language'] != None and request.data['language'] != [""] and type(request.data['language'])==list):
                queryset = queryset.filter(language__contains=request.data['language'])
            else:
                None      
        except: None
        try:   
            if request.data['keywords'] != None:
                keywords = request.data['keywords']
                queryset = queryset.filter(content__icontains=keywords)
            else:None      
        except: None 
        try:   
            if request.data['slug'] != None:
                slug = request.data['slug']
                queryset = queryset.filter(slug=slug)
            else:None       
        except:None
        
        serializer = ProjectSerializer(queryset,many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
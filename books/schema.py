from tokenize import String
import graphene
from graphene_django import DjangoObjectType 
#Formats our Django object into a format that can be utilized by GraphQL
from .models import Books #Don't forget to import the Model!

class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ("id", "title", "except")

class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)
    def resolve_all_books(root, info):
        return Books.objects.all()
        #return Books.objects.filter(title="django")

schema = graphene.Schema(query=Query)

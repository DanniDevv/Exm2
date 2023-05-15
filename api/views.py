from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import generics

from rest_framework import viewsets


from tienda.models import Categoria,Producto
from .serializers import(
    CategoriaSerializer,
    ProductoSerializer
)

#  class IndexView(APIView):
# # # AQUI SE ESTA  INCORPORANDO EL METODO GET   
#      def get(self,request):
#          lista_categorias = Categoria.objects.all()
#          serializer_categoria = CategoriaSerializer(lista_categorias,many=True)
#          return Response(serializer_categoria.data)
    
# # SE TIENE QUE IMPORTAR  from rest_framework import generics
# class CategriaView(generics.ListCreateAPIView):
#     queryset = Categoria.objects.all()
#     serializer_class = CategoriaSerializer

# #AQUI SE ESTA INCORPORANDO EL METODO ELIMINAR
# class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Categoria.objects.all()
#     lookup_url_kwarg = "categoria_id"
#     serializer_class = CategoriaSerializer
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


#AQUI SE IMPLEMENTA LOS METODOS POST,GET,DELETE,UPDATE
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
from django.db import models
from django.utils import timezone
# Create your models here.

LISTA_CATEGORIAS = (
    ("ANIMACAO", "Animação",),
    ("SERIES", "Séries"),
    ("COMEDIA", "Comédia"),
    ("OUTROS", "Outros"),
)
#criar os filmes
class Filme(models.Model):
      titulo = models.CharField(max_length=100)
      thumb = models.ImageField(upload_to='thumb_filmes')
      categoria = models.CharField(max_length=15, choices= LISTA_CATEGORIAS)
      descricao = models.TextField(max_length=1000)
      visualizacoes = models.IntegerField(default=0)
      data_criacao = models.DateTimeField(default=timezone.now)
                        #idependente de qual projeto streaming for, sempre adicionar deste jeito que está para não dar erro no banco de dados sql
      def __str__(self):
          return self.titulo




#criar os episódios
class Episódios(models.Model):
    filme = models.ForeignKey("Filme", related_name="episódios", on_delete=models.CASCADE)
    título = models.CharField(max_length=100)
    vídeo = models.URLField()


    def __str__(self):
        return self.filme.titulo + "-" + self.titulo

#criar os usuários

#para pausar o servidor aperte Ctrl+C


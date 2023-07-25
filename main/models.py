
from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    comentario = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autor'
        db_table_comment = 'Cadastro dos Autores'


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'categoria'
        db_table_comment = 'categorias de livro'


class Editora(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'editora'
        db_table_comment = 'Cadastro de editoras'


class Livro(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    data_lancamento = models.DateField(blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    autor = models.ForeignKey(Autor, models.DO_NOTHING, db_column='autor', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria', blank=True, null=True)
    editora = models.ForeignKey(Editora, models.DO_NOTHING, db_column='editora', blank=True, null=True)
    capa = models.TextField(blank=True, null=True)
    data_compra = models.DateField(blank=True, null=True)
    avaliacao = models.CharField(max_length=5, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'livro'
        db_table_comment = 'cadastro de livros'

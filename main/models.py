
from django.db import models
from django.contrib.auth import get_user_model

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    comentario = models.TextField(blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data_cadastro = models.DateField(auto_now_add=True)
    
    class Meta:
        managed = False
        db_table = 'autor'
        db_table_comment = 'Cadastro dos Autores'
    
    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data_cadastro = models.DateField(auto_now_add=True)
    
    class Meta:
        managed = False
        db_table = 'categoria'
        db_table_comment = 'categorias de livro'

    def __str__(self):
        return self.nome
    

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data_cadastro = models.DateField(auto_now_add=True)
    
    class Meta:
        managed = False
        db_table = 'editora'
        db_table_comment = 'Cadastro de editoras'
    
    def __str__(self):
        return self.nome


class Livro(models.Model):
    
    STATUS = (
        ('1','Pessimo'),
        ('2','Ruim'),
        ('3','Regular'),
        ('4','Bom'),
        ('5','Otimo'),
    )   
    
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    data_lancamento = models.DateField(blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    autor = models.ForeignKey(Autor, models.DO_NOTHING, db_column='autor', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria', blank=True, null=True)
    editora = models.ForeignKey(Editora, models.DO_NOTHING, db_column='editora', blank=True, null=True)
    capa = models.ImageField(_upload_to=None, height_field=None, width_field=None, max_length=None)                   
    data_compra = models.DateField(blank=True, null=True)
    avaliacao = models.CharField(max_length=1, blank=True, null=True, choices=STATUS)
    descricao = models.TextField(blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data_cadastro = models.DateField(auto_now_add=True)
    
    class Meta:
        managed = False
        db_table = 'livro'
        db_table_comment = 'cadastro de livros'

    def __str__(self):
        return self.titulo
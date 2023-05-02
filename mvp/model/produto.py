from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from model import Base, Comentario

class Produto(Base):
    __tablename__ = 'produto'

    id = Column("pk_produto", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    quantidade = Column(Integer)
    valor = Column(Float)

    # Definição do relacionamento entre o produto e o comentário.
    # Essa relação é implicita, não está salva na tabela 'produto',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    comentarios = relationship("Comentario")

    def __init__(self, nome: str, quantidade: int, valor: float):
        """
        Cria um Produto

        Arguments:
            nome: nome do produto.
            quantidade: quantidade que se espera comprar daquele produtona
            valor: valor esperado para o produto
        """
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

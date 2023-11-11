from flask import Blueprint
from .produtosManager import ProdutosManager

produtos = Blueprint('produtos', __name__)
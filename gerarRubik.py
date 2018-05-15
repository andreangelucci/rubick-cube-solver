from vision.analiseCores import gerarRubikImagem
from rubik.rubik import *
from rubik.algKociemba import resolver

#gera uma classe tipo Rubik de acordo com a imagem
#e as configuracoes de coordenadas informada
#gerarRubikImagem('./fotos/frente.jpg', './coordenadas.conf').representacaoGrafica()
cubo = rubikMontado()
cubo.representacaoGrafica()
cubo.movimentosRandom(5)
cubo.representacaoGrafica()
resolver(cubo)
cubo.representacaoGrafica()

from sys import stdin, stdout

# A primeira linha deve conter o número de cubinhos com nenhuma face pintada de preto.
# A segunda linha deve conter o número de cubinhos com exatamente uma face pintada.
# A terceira linha deve conter o número de cubinhos com exatamente duas faces pintadas.
# A quarta e última linha deve conter o número de cubinhos com exatamente três faces pintadas.

ladoCubo = int(stdin.readline())

tesLado = 8 # sempre as vértices; um cubo sempre tem 8 vértices

dosLado = (ladoCubo-2)*12 # um cubo tem sempre 12 arestas; 
# estarão pintadas todas elas tirando os vértices (que já foram contados)
# então é um lado do cubo, tirando os vértices vezes a quantidade de arestas

umLado = (ladoCubo-2)**2*6 # face do cubo que não é a borda
# forma-se então um quadrado x/x em cada face, a qual x é o número de lados diminuindo dois (que são as bordas)
# multiplica então a área desse quadrado pela quantidade de faces

zeroLado = (ladoCubo-2)**3 # é o completo inferior do cubo; forma-se um cubo menor tirando o exterior do cubo maior
# é o volume de um cubo com dois lados a menos que o cubo maior (esses lados seriam as bordas pintadas)

stdout.write(str(zeroLado)+"\n")
stdout.write(str(umLado)+"\n")
stdout.write(str(dosLado)+"\n")
stdout.write(str(tesLado)+"\n")
# importa as bibliotecas necessárias para fazer a análize de frequência de palavras e colocações
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.text import Text

# faz o download do tokenizer "punkt" da biblioteca nltk
nltk.download('punkt')

# abre o arquivo CSV com opção de codificação utf-8 e lê seu conteúdo
with open(r'C:\Users\marcu\Downloads\Projetos\Chatbot\donaflor_tratado.csv', encoding='utf-8') as file:
    text = file.read()

# gera os tokens a partir do texto lido
tokens = word_tokenize(text)

# gera a distribuição de frequência das palavras nos tokens
fd = FreqDist(tokens)

# cria um objeto de texto a partir dos tokens
text_obj = Text(tokens)

# encontra as colocações (pares de palavras) no texto e imprime
print('PARES DE PALAVRAS FREQUENTES')
print(text_obj.collocations())

# imprime as vinte palavras mais frequentes
print('30 PALAVRAS MAIS FREQUENTES: ')
print(fd.most_common(30))

# importa a biblioteca matplotlib para gerar o gráfico de frequência
import matplotlib.pyplot as plt

# define o tamanho da figura do gráfico e gerá o gráfico com as trinta palavras mais frequentes adicionando o título
plt.figure(figsize= (13,8))
fd.plot(30, title = 'Frequência de Palavras')

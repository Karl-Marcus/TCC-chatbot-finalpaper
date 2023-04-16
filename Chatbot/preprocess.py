# importa as bibliotecas necessárias para o pré-processamento de texto
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from unidecode import unidecode

# baixa as stopwords em português e o WordNet para lematização
nltk.download('stopwords')
nltk.download('wordnet')
stopwords = nltk.corpus.stopwords.words('portuguese')

# abre o arquivo de input em modo de leitura com encoding UTF-8
with open(r'C:\\Users\marcu\Downloads\Projetos\Chatbot\donaflor.csv', encoding='utf-8') as file:
    text = file.read()

# faz a tokenização das palavras e das sentenças
tokens = word_tokenize(text)
sent_tokens = sent_tokenize(text)

# usa o WordNet para fazer a lematização das palavras
wn1 = WordNetLemmatizer()
[wn1.lemmatize(t) for t in tokens]

# define a função de pré processamento que remove as stopwords e caracteres não alfabéticos, converte as letras para minúsculas e une as palavras novamente em uma única string
def pre_processamento(text):
    texto_sem_acentos = unidecode(text)
    letras_min = re.findall(r'\b[A-zÀ-úü]+\b', texto_sem_acentos.lower())
    stopwords = nltk.corpus.stopwords.words('portuguese')
    stopwords.extend(['la', 'lo'])
    stop = set(stopwords)
    sem_stopwords = [w for w in letras_min if w not in stop]
    texto_limpo= " ".join(sem_stopwords)
    return texto_limpo

# aplica a função de pré-processamento ao texto original
texto_limpo = pre_processamento(text)

# abre o arquivo de output em modo de escrita com encoding UTF-8 e escreve o texto pré-processado
with open('C:\\Users\\marcu\\Downloads\\Projetos\\Chatbot\\donaflor_tratado.csv', 'w', encoding='utf-8') as file:
    file.write(texto_limpo)

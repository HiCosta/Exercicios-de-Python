import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não está disponível no momento')
else:
    print('Tudo OK com o site')
    print(site.read())      # ler conteúdo do site

import urllib
import urllib.error
import urllib.request

lk = str(input('Coloque o link do site aqui: '))
try:
    site = urllib.request.urlopen(lk)
except urllib.error.URLError: 
    print('Este site esta dando ERRO!')
else:
    print('Este site esta acessivel, TUDO CERTO!')
    #print(site.read())
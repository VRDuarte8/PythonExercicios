import webbrowser
try:
    webbrowser.open("http://pudim.com.br/")
except:
    print("\033[1;31mO site Pudim não está acessível no momento.")
else:
    print("\033[1;33mO site Pudim foi acessado com sucesso!")

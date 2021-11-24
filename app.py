from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = [
    {"texto": "Volkswagen Gol 2013", "concluida": "R$ 29.900,00"},
    {"texto": "Porsche 911 2021", "concluida": "R$ 2.159.990,00"},
    {"texto": "Jaguar F-Type 2016", "concluida": "R$ 379.900,00"},
    {"texto": "Ford Mustang 2021", "concluida": "R$ 594.000,00"},
]

@app.route('/')
def index():
    return render_template('index.html', lista=tarefas)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    texto = request.form['texto']  
    status = request.form['status']    # <input name="texto"/>
    tarefa = { "texto": texto, "concluida": status }
    tarefas.append(tarefa)

    return redirect('https://5000-ivory-squirrel-yi6vyyb0.ws-us17.gitpod.io/')

@app.route('/busca', methods=['POST'])
def pes():
    result = []
    resultado = request.form['pesquisa']
    resultado = resultado.lower()
    if resultado == "":
        return render_template('erro.html') 
    for i in tarefas:
        if resultado in i['texto'].lower():            
            result.append(i)     
    for i in tarefas:
        if resultado in i['concluida'].lower():            
            result.append(i)  
    if not result:
        return render_template('erro.html') 

    return render_template('busca.html', lista2=result)  

@app.route('/teste_delete')
def teste_delete():
    return render_template('teste_delete.html')

@app.route('/apagar',methods=['POST'])
def apagar():
    texto=request.form['texto']
    lista_deletada=0
    for i in tarefas:
        if texto == i['texto']:
            tarefas.remove(i)
            lista_deletada+=1
    if lista_deletada==0:
        return render_template('erro.html')
    return render_template('index.html',lista=tarefas)
       
app.run(debug=True)


# Implementar o DELETE!! (2,0 pontos)   
# Implementar uma pesquisa (3,0 pontos)


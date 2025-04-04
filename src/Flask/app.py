from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'segredo'

palavras = ['pera', 'banana', 'zago', 'creatina', 'isabela', 'joao', 'dedo', 'paralelepipedo', 'abacaxi']


@app.route("/", methods=["GET", "POST"])
def index():
    if "palavra" not in session:
        session["palavra"] = random.choice(palavras)
        session["acertos"] = []
        session["erros"] = []
    
    palavra = session["palavra"]
    acertos = session["acertos"]
    erros = session["erros"]
    status = ""

    if request.method == "POST":
        letra = request.form.get("letra", "").lower()

        if letra in palavra and letra not in acertos:
            acertos.append(letra)
        elif letra not in palavra and letra not in erros:
            erros.append(letra)

        session["acertos"] = acertos
        session["erros"] = erros

        if len(erros) >= 6:
            status = "Foi por pouco! A palavra era: " + palavra
        elif all(l in acertos for l in palavra):
            status = "Parabéns! Você ganhou!"

    exibicao = [l if l in acertos else "_" for l in palavra]
    imagem = f"forca{len(erros)}.png"

    return render_template("index.html", exibicao=exibicao, imagem=imagem, status=status, erros=erros)

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

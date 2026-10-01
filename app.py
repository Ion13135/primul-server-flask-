from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def acasa():
    return "Bine ai venit pe primul meu server Flask!"


@app.route("/despre")
def despre():

    nume = "Ion Sobraneschi"

    mesaj = """
    Sunt in curs de a deveni Python Developer si Data Analyst.
    Invat programare, analiza de date si dezvoltare web.
    """

    tehnologii = [
        "Python",
        "Flask",
        "HTML",
        "CSS",
        "JavaScript"
    ]

    return render_template(
        "despre.html",
        nume=nume,
        mesaj=mesaj,
        tehnologii=tehnologii
    )


@app.route("/proiecte")
def proiecte():

    lista_proiecte = [
        "Primul-proiect",
        "primul-website",
        "Sales-Business-Intelligence"
    ]

    return render_template(
        "proiecte.html",
        proiecte=lista_proiecte
    )


@app.route("/salut/<nume>")
def salut(nume):
    return f"Salut, {nume}! Ma bucur sa te vad aici."


if __name__ == "__main__":
    app.run(debug=True)

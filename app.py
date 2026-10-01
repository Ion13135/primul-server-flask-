from flask import Flask

app = Flask(__name__)


@app.route("/")
def acasa():
    return "Bine ai venit pe primul meu server Flask!"


@app.route("/despre")
def despre():
    return """
    Ma numesc Ion Sobraneschi.

    Sunt in curs de a deveni Python Developer si Data Analyst.

    Invat programare, analiza de date si dezvoltare web.
    """


@app.route("/proiecte")
def proiecte():
    return """
    Proiectele mele:

    - Primul-proiect
    - primul-website
    - Sales-Business-Intelligence
    """


@app.route("/salut/<nume>")
def salut(nume):
    return f"Salut, {nume}! Ma bucur sa te vad aici."


if __name__ == "__main__":
    app.run(debug=True)
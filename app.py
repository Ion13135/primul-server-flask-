from flask import Flask, render_template, request

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


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        nume = request.form.get("nume")
        email = request.form.get("email")
        mesaj = request.form.get("mesaj")

        print(
            f"Mesaj primit de la {nume} ({email}): {mesaj}"
        )

        return render_template(
            "contact_succes.html",
            nume=nume
        )

    return render_template("contact.html")


@app.route("/salut/<nume>")
def salut(nume):
    return f"Salut, {nume}! Ma bucur sa te vad aici."


if __name__ == "__main__":
    app.run(debug=True)

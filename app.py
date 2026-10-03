from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

mesaje = []

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
        mesaj_text = request.form.get("mesaj")

        mesaj_nou = {
            "nume": nume,
            "email": email,
            "mesaj": mesaj_text
        }

        mesaje.append(mesaj_nou)

        print(
            f"Mesaj nou primit de la {nume} ({email}): {mesaj_text}"
        )

        return redirect(
            url_for("contact_success", nume=nume)

        )

    return render_template("contact.html")


@app.route("/contact-success")
def contact_success():

    nume = request.args.get("nume")

    return render_template(
        "contact_success.html",
        nume=nume
    )
    
@app.route("/mesaje")
def afiseaza_mesaje():

    return render_template(
        "mesaje.html",
        mesaje=mesaje
    )


@app.route("/salut/<nume>")
def salut(nume):
    return f"Salut, {nume}! Ma bucur sa te vad aici."




if __name__ == "__main__":
    app.run(debug=True)

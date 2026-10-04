from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mesaje.db"

db = SQLAlchemy(app)



class Mesaj(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nume= db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        nullable=False
    )

    continut = db.Column(
        db.Text,
        nullable=False
    )

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
        email= request.form.get("email")
        mesaj_text = request.form.get("mesaj")

        mesaj_nou = Mesaj(
            nume=nume,
            email=email,
            continut=mesaj_text
        )

        db.session.add(mesaj_nou)
        db.session.commit()

        print(
            f"Mesaj nou salvat in baza de data: {nume}, {email})"
        )

        return redirect(url_for("contact_success", nume=nume))

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

    toate_mesajele = Mesaj.query.all()

    return render_template(
        "mesaje.html",
        mesaje=toate_mesajele
    )


@app.route("/salut/<nume>")
def salut(nume):
    return f"Salut, {nume}! Ma bucur sa te vad aici."

with app.app_context():
    db.create_all()




if __name__ == "__main__":
    app.run(debug=True)

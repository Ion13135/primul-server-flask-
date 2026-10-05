from flask import Flask, render_template, request, redirect, url_for, jsonify
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

@app.route("/api/mesaje")
def api_toate_mesajele():

    toate = Mesaj.query.all()

    rezultat = []

    for mesaj in toate:

        rezultat.append({
            "id": mesaj.id,
            "nume": mesaj.nume,
            "email": mesaj.email,
            "continut": mesaj.continut
        })

        return jsonify(rezultat)


@app.route("/api/mesaje", methods=["POST"])
def api_creeaza_mesaj():

    date = request.get_json()

    if (
        not date
        or not date.get("nume")
        or not date.get("email")
        or not date.get("continut")
    ):
        return jsonify({
            "eroare": "Lipsesc campuri obligatorii"
        }), 400

    mesaj_nou = Mesaj(
        nume=date["nume"],
        email=date["email"],
        continut=date["continut"]
    )

    db.session.add(mesaj_nou)
    db.session.commit()

    return jsonify({
        "id": mesaj_nou.id,
        "nume": mesaj_nou.nume,
        "email": mesaj_nou.email,
        "continut": mesaj_nou.continut
    }), 201



@app.route("/api/mesaje/<int:id>")
def api_un_mesaj(id):

    mesaj = Mesaj.query.get(id)

    if mesaj is None:

        return jsonify({
            "eroare": "Mesajul nu a fost gasit"
        }), 404

    return jsonify({
        "id": mesaj.id,
        "nume": mesaj.nume,
        "email": mesaj.email,
        "continut": mesaj.continut
    })


@app.route("/api/mesaje/<int:id>", methods=["PUT"])
def api_actualizeaza_mesaj(id):

    mesaj = Mesaj.query.get(id)

    if mesaj is None:

        return jsonify({
            "eroare": "Mesajul nu a fost gasit"
        }), 404

    date = request.get_json()

    if "nume" in date:
        mesaj.nume = date["nume"]

    if "email" in date:
        mesaj.email = date["email"]

    if "continut" in date:
        mesaj.continut = date["continut"]

    db.session.commit()

    return jsonify({
        "id": mesaj.id,
        "nume": mesaj.nume,
        "email": mesaj.email,
        "continut": mesaj.continut
    })

@app.route("/api/mesaje/<int:id>", methods=["DELETE"])
def api_sterge_mesaj(id):

    mesaj = Mesaj.query.get(id)

    if mesaj is None:

        return jsonify({
            "eroare": "Mesajul nu a fost gasit"
        }), 404

    db.session.delete(mesaj)
    db.session.commit()

    return jsonify({
        "mesaj": f"Mesajul cu id-ul {id} a fost sters."
    })


@app.route("/salut/<nume>")
def salut(nume):
    return f"Salut, {nume}! Ma bucur sa te vad aici."

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/sport31", methods=["GET", "POST"])
def sport31():

    if request.method == "POST":

        sport = request.form.get("sport")
        team = request.form.get("team")

        return render_template(
            "result31.html",
            sport=sport,
            team=team
        )

    return render_template("index31.html")

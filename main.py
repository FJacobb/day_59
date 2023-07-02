from flask import Flask, render_template, request
import smtplib
# import requests

app = Flask(__name__)

# response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
# data = response.json()
# num = len(data)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")
@app.route("/contact.html")
def contact():
    return render_template("contact.html")
# @app.route("/post.html/1")
# # def post():
# #     return render_template("post.html", value=data[0])
# # @app.route("/post.html/2")
# # def post2():
# #     return render_template("post.html", value=data[1])
# # @app.route("/post.html/3")
# # def post3():
# #     return render_template("post.html", value=data[2])
@app.route("/form-entry.html", methods=["POST"])
def form():
    name= request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    data = f"""
    name:{name},
    email:{email},
    phone:{phone},
    message:{message}
    """

    my_email = 'projectfestus@gmail.com'
    sender_pass = 'iyfikarcqyergruh'
    with smtplib.SMTP("smtp.gmail.com", 587) as emai:
        emai.starttls()
        emai.login(my_email,sender_pass)
        emai.sendmail(msg=data, to_addrs="festusj52@gmail.com", from_addr=my_email)
    return render_template("form-entry.html")


if __name__=="__main__":
    app.run(debug=True)

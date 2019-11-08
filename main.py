from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
# from flask_mail import Mail


app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/arambhroad'
db = SQLAlchemy(app)

class Contact(db.Model):
    '''sno	name	email	phone msg	date '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(20), unique=False, nullable=False)
    phone = db.Column(db.String(12), unique=False, nullable=False)
    msg = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(30), nullable=True)


class Enquiry(db.Model):
    '''sno	comp_name	contact_person	designation	address	phone	email	descrip_material
    	from_place	to_dest	method_pack	no_pkg	actual_wt	length	height	width	weight
        value	insured	dc	dd	pay_by	gst_reg	dispatch_by	special_ser	other_ser
        exp_date_book	date'''
    sno = db.Column(db.Integer, primary_key=True)
    comp_name = db.Column(db.String(30), unique=False, nullable=False)
    contact_person = db.Column(db.String(20), unique=False, nullable=False)
    designation = db.Column(db.String(30), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(db.String(15), unique=False, nullable=False)
    eamil = db.Column(db.String(20), unique=False, nullable=False)
    descrip_material = db.Column(db.String(120), unique=False, nullable=False)
    from_place = db.Column(db.String(20), unique=False, nullable=False)
    to_dest = db.Column(db.String(20), unique=False, nullable=False)
    method_pack = db.Column(db.String(20), unique=False, nullable=False)
    no_pkg = db.Column(db.String(20), unique=False, nullable=False)
    actual_wt = db.Column(db.String(20), unique=False, nullable=False)
    length = db.Column(db.String(20), unique=False, nullable=False)
    height = db.Column(db.String(20), unique=False, nullable=False)
    width = db.Column(db.String(120), unique=False, nullable=False)
    weight = db.Column(db.String(20), unique=False, nullable=False)
    value = db.Column(db.String(20), unique=False, nullable=False)
    insured = db.Column(db.String(20), unique=False, nullable=False)
    pay_by = db.Column(db.String(20), unique=False, nullable=False)
    gst_reg = db.Column(db.String(20), unique=False, nullable=False)
    dispatch_by = db.Column(db.String(20), unique=False, nullable=False)
    special_ser = db.Column(db.String(20), unique=False, nullable=False)
    other_ser = db.Column(db.String(30), unique=False, nullable=False)
    exp_date_book = db.Column(db.String(20), unique=False, nullable=False)
    date = db.Column(db.String(30), nullable=True)

@app.route('/')
def home():
    return render_template('index.html' )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def service():
    return render_template('services.html')


@app.route('/network')
def network():
    return render_template('network.html')

@app.route("/contact", methods=["GET","POST"])
def contact():
    if (request.method == "POST"):
        '''add quiry to data base'''
        '''sno	name	email	phone msg	date '''
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        '''sno	name	email	phone_num	mes	date '''
        entry = Contact(name = name, email = email, phone = phone, msg = message, date=datetime.now())
        db.session.add(entry)
        db.session.commit() 


    return render_template('contact.html')

@app.route('/enquiry')
def enquiry():
    # if (request.method == "POST"):
    # '''sno	comp_name	contact_person	designation	address	phone	email	descrip_material
    # from_place	to_dest	method_pack	no_pkg	actual_wt	length	height	width	weight
    # value	insured	dc	dd	pay_by	gst_reg	dispatch_by	special_ser	other_ser
    # exp_date_book	date'''
    #     comp_name  = request.form.get("company")
    #     contact_person = request.form.get("cperson")
    #     designation = request.form.get("designation")
    #     address = request.form.get("address")
    #     phone = request.form.get("phone")
    #     email = request.form.get("eamil")
    #     descrip_material = request.form.get("dmaterials")
    #     from_place = request.form.get("disfrom")
    #     to_dest = request.form.get("sentto")
    #     method_pack = request.form.get("packing")
    #     no_pkg = request.form.get("nopkgs")
    #     actual_wt = request.form.get("tonnage")
    #     length = request.form.get("lengthd")
    #     height = request.form.get("heightd")
    #     width = request.form.get("widthd")
    #     value = request.form.get("materials")
    #     insured = request.form.get("nsured")
    #     dc = request.form.get("address")
    #     dd = request.form.get("address")
    #     pay_by = request.form.get("address")
    #     gst_reg = request.form.get("address")
    #     dispatch_by = request.form.get("address")
    #     special_ser = request.form.get("address")
    #     other_ser = request.form.get("address")
    #     exp_date_book = request.form.get("address")
    #     date = request.form.get("address")

    return render_template('enquiry.html')

@app.route('/blog')
def blog():
    return render_template('form.html')

app.run(debug=True)
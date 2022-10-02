from flask import Blueprint,render_template
import json
from webScraping import final

views = Blueprint(__name__,"views")

@views.route("/")
def home():  # put application's code here
    return render_template("index.html")

@views.route("/city")
def city():
    final()
    activity = open('Activities.json')
    activity = json.load(activity)
    hotel = open('Hotels.json')
    hotel = json.load(hotel)
    summary = open('Summary.json')
    summary = json.load(summary)

    name = summary['Name']
    background = summary['Img']
    sum = summary['Summary']
    Act1 = activity['Img'][1]
    Act2 = activity['Img'][2]
    Act3 = 	activity['Img'][3]
    Act4 = activity['Img'][4]
    Act1_i = activity['Item'][1]
    Act2_i = activity['Item'][2]
    Act3_i = activity['Item'][3]
    Act4_i = activity['Item'][4]
    Act1_a = activity['Address'][1]
    Act2_a = activity['Address'][2]
    Act3_a = activity['Address'][3]
    Act4_a = activity['Address'][4]
    hot1 = hotel['Img'][1]
    hot2 = hotel['Img'][2]
    hot3 = hotel['Img'][3]
    hot1_i = hotel['Item'][1]
    hot2_i = hotel['Item'][2]
    hot3_i = hotel['Item'][3]
    hot1_a = hotel['Address'][1]
    hot2_a = hotel['Address'][2]
    hot3_a = hotel['Address'][3]



    return render_template("city.html",
                           name = name,
                           background=background,
                           sum = sum,
                           Act1=Act1,
                           Act2=Act2,
                           Act3=Act3,
                           Act4=Act4,
                           Act1_i=Act1_i,
                           Act2_i=Act2_i,
                           Act3_i=Act3_i,
                           Act4_i=Act4_i,
                           Act1_a=Act1_a,
                           Act2_a=Act2_a,
                           Act3_a=Act3_a,
                           Act4_a=Act4_a,
                           hot1=hot1,
                           hot2 = hot2,
                           hot3 = hot3,
                           hot1_i = hot1_i,
                           hot2_i = hot2_i,
                           hot3_i = hot3_i,
                           hot1_a = hot1_a,
                           hot2_a = hot2_a,
                           hot3_a = hot3_a,
                           )


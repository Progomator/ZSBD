from datetime import date, datetime
from turtle import right
from typing import Type
import Menu
from WebServer import WebServer, db
from flask import render_template, request
from DB_Connector import session
import DB_Connector
import DB_TableModels
from DB_TableModels import *
import Forms
from flask import flash
from Menu import menu

# TODO: Validators! : If exist, etc.

@WebServer.route("/base/create", methods=["GET", "POST"]) 
def base_create():
    db.create_all()




@WebServer.route("/base/init", methods=["GET", "POST"]) 
def base_init():
    session.add_all([
        AnimalList(animalType="Krowa mleczna - HF"),
        AnimalList(animalType="Krowa mięsna - Limousine"),
        AnimalList(animalType="Krowa mięsna - Angus"),
        BonitationsList(bonitationType = "klasa I"),
        BonitationsList(bonitationType = "klasa II"),
        BonitationsList(bonitationType = "klasa IIIa"),
        BonitationsList(bonitationType = "klasa IIIb"),
        BonitationsList(bonitationType = "klasa IVa"),
        BonitationsList(bonitationType = "klasa IVb"),
        BonitationsList(bonitationType = "klasa V"),
        BonitationsList(bonitationType = "klasa VI"),
        BonitationsList(bonitationType = "klasa VIz"),
        LandDevelopment(destination = "R - grunt orny"),
        LandDevelopment(destination = "S - sad"),
        LandDevelopment(destination = "Ł - łąka trwała"),
        LandDevelopment(destination = "Ps - pastwisko"),
        LandDevelopment(destination = "Br - grunt rolny zabudowany"),
        LandDevelopment(destination = "Wsr - grunt rolny pod stawem"),
        LandDevelopment(destination = "Lzr - grunt rolny zadrzewiony/zakrzewiony"),
        PossessionRights(right = "Własność"),
        PossessionRights(right = "Dzierżawa"),
        PossessionRights(right = "Nieuregulowane"),
        Expenses(date = datetime.today(), category="test", subCategory="test2", sum = 1293)]
    )
    session.commit()
    return render_template("page_init.html")




@WebServer.route("/home", methods=["GET", "POST"]) # /<typ: parametr> np. /<int: wiek>
def home():
    return render_template("page_home.html")



###################################################################
###################################################################



@WebServer.route("/animals/add", methods=["GET", "POST"])
def animals_add():

    active_item = {
        "headbar_active" : "Zwierzęta",
        "leftbar_active" : "Dodawanie zwierząt",
    }

    form = Forms.AnimalsAddForm()
    if form.is_submitted:
        new = Animals(
            animalType = form.animalType.data,
            earingId = form.earingId.data,
            building = form.building.data,
            birthDate = form.birthDate.data,
            acquisitionCost = form.acquisitionCost.data,
            isAlive = form.isAlive.data,
            forMeat = form.forMeat.data
                
        )
        expense = Expenses(
            date = datetime.today(),
            category = f"Nabycie zwierzęcia: {form.animalType.data}",
            subCategory = form.earingId.data,
            sum = form.acquisitionCost.data
        )
        session.add(new)
        session.commit()
        session.add(expense)
        session.commit()
        flash("Zwięrzę dodane do bazy")

    return render_template("page_animals_add.html", form=form, menu=menu, active_item=active_item)




@WebServer.route("/buildings/add", methods=["GET", "POST"])
def buildings_add():

    active_item = {
        "headbar_active" : "Budynki",
        "leftbar_active" : "Dodawanie budynków",
    }

    form = Forms.BuildingsAddForm()
    if form.is_submitted() and request.method == "POST":
        new = Buildings(
            userId = form.userId.data,
            buildingType = form.buildingType.data,
            volume = form.volume.data,
            area = form.area.data,
            field = form.field.data,
            cost = form.cost.data
        )
        expense = Expenses(
            date = datetime.today(),
            category = "Nabycie lub budowa budynku",
            subCategory = form.userId.data,
            sum = form.cost.data
        )
        session.add(new)
        session.commit()
        session.add(expense)
        session.commit()
        flash("Budynek dodany do bazy")
        return render_template("page_buildings_add.html", form=form, menu=menu, active_item=active_item)
    return render_template("page_buildings_add.html", menu=menu, active_item=active_item)




@WebServer.route("/animallist/add", methods=["GET", "POST"])
def animallist_add():

    active_item = {
        "headbar_active" : "Zwierzęta",
        "leftbar_active" : "Dodawanie gatunków",
    }

    form = Forms.AnimalListAddForm()
    if form.is_submitted():
        new = AnimalList(
            animalType = form.animalType.data
    )
        session.add(new)
        session.commit()
        flash("Gatunek dodany do bazy")

    return render_template("page_animallist_add.html", form=form, menu=menu, active_item=active_item)




@WebServer.route("/fields/add", methods=["GET", "POST"])
def fields_add():

    active_item = {
        "headbar_active" : "Pola",
        "leftbar_active" : "Dodawanie pól",
    }

    form = Forms.FieldsAddForm()
    if form.is_submitted():
        new = Fields(
            area = form.area.data,
            bonitation = form.bonitation.data,
            cost = form.cost.data,
            purchaseDate = form.purchaseDate.data,
            possessionRight = form.possessionRight.data,
        )
        expense = Expenses(
            date = datetime.today(),
            category = "Nabycie pola",
            subCategory = form.possessionRight.data,
            sum = form.cost.data
        )

        session.add(new)
        session.commit()
        session.add(expense)
        session.commit()
        flash("Pole dodane do bazy")
    return render_template("page_fields_add.html", form=form, menu=menu, active_item=active_item)




@WebServer.route("/vaccineslist/add", methods=["GET", "POST"])
def vaccineslist_add():

    active_item = {
        "headbar_active" : "Preparaty chemiczne",
        "leftbar_active" : "Dodawanie szczepionek",
    }

    form = Forms.VaccinesListAddForm()
    if form.is_submitted():
        new = VaccinesList(
            vaccineType = form.vaccineType.data,
            unitCost = form.unitCost.data,
        )

        session.add(new)
        session.commit()
        flash("Szczepionka dodana do bazy")

    return render_template("page_vaccineslist_add.html", form=form, menu=menu, active_item=active_item)




@WebServer.route("/fertilizerslist/add", methods=["GET", "POST"])
def fertilizerslist_add():

    active_item = {
        "headbar_active" : "Preparaty chemiczne",
        "leftbar_active" : "Dodawanie nawozów",
    }

    form = Forms.FertilizersListAddForm()
    if form.is_submitted():
        new = FertilizersList(
            fertilizerType = form.fertilizerType.data,
            unitCost = form.unitCost.data,
        )

        session.add(new)
        session.commit()
        flash("Nawóz dodany do bazy")

    return render_template("page_fertilizerslist_add.html", form=form, menu=menu, active_item=active_item)




@WebServer.route("/herbicideslist/add", methods=["GET", "POST"])
def herbicideslist_add():

    active_item = {
        "headbar_active" : "Preparaty chemiczne",
        "leftbar_active" : "Dodawanie herbicydów",
    }

    form = Forms.HerbicidesListAddForm()
    if form.is_submitted():
        new = HerbicidesList(
            herbicideType = form.herbicideType.data,
            unitCost = form.unitCost.data,
            against = form.against.data
        )

        session.add(new)
        session.commit()
        flash("Herbicyd dodany do bazy")

    return render_template("page_herbicideslist_add.html", form=form, menu=menu, active_item=active_item)




@WebServer.route("/pesticideslist/add", methods=["GET", "POST"])
def pesticideslist_add():

    active_item = {
        "headbar_active" : "Preparaty chemiczne",
        "leftbar_active" : "Dodawanie pestycydow",
    }

    form = Forms.PesticidesListAddForm()
    if form.is_submitted():
        new = PesticidesList(
            pesticideType = form.pesticideType.data,
            unitCost = form.unitCost.data,
            against = form.against.data
        )

        session.add(new)
        session.commit()
        flash("Pestycyd dodany do bazy")

    return render_template("page_pesticideslist_add.html", form=form, menu=menu, active_item=active_item)

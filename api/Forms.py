from logging import PlaceHolder
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField, FloatField
from wtforms.fields.simple import BooleanField, SubmitField
from DB_Connector import session
import DB_TableModels
from DB_TableModels import *


# TODO: Validators! 


#done
class BuildingsAddForm(FlaskForm): 
    userId = StringField(
        label = "Identyfikator Budynku"
    )
    buildingType = StringField(
        label = "Typ budynku",
    )
    volume = FloatField(
        label = "Objętość magazynowa (dotyczy plonów)"
    )
    area = FloatField(
        label = "Powierzchnia produkcji (dotyczy chowu zwierząt)"
    )
    field = IntegerField(
        label = "Grunt, na którym znajduje się budynek (opcjonalnie)"
    )
    cost = FloatField(
        label = "Koszt nabycia / wybudowania"
    )
    


#done
class AnimalsAddForm(FlaskForm):
    animalType = SelectField(
        label = "Typ zwierzęcia",
        #choices = [animal.id for animal in session.query(AnimalList).order_by(AnimalList.animalType)] 
        choices = [(animal.id, animal.animalType) for animal in session.query(AnimalList).order_by(AnimalList.animalType)]
    )
    earingId = StringField(
        label = "Identyfikator"
    )
    building = SelectField(
        label = "Budynek chowu",
        #choices = [building.id for building in session.query(Buildings).order_by(Buildings.buildingType)] 
        choices = [(building.id, building.userId) for building in session.query(Buildings).order_by(Buildings.buildingType)]
    )
    birthDate = DateField(
        label = "Data urodzenia",
        format = "%Y-%m-%d"
    )
    acquisitionCost = FloatField(
        label = "Koszt nabycia zwierzęta (zł)"
    )
    isAlive = BooleanField(
        label = "Żywe"
    )
    forMeat = BooleanField(
        label = "Przeznaczenie na mięso"
    )



#done
class AnimalListAddForm(FlaskForm):
    animalType = StringField(
        label = "Gatunk i rasa zwierzęcia [gatunek - rasa]",
    )



#done
class FieldsAddForm(FlaskForm):
    area = FloatField(
        label = "Powierzchnia upraw [ar]"
    )
    bonitation = SelectField(
        label = "Klasa bonitacyjna",
        choices = [(bonitation.id, bonitation.bonitationType) for bonitation in session.query(BonitationsList).order_by(BonitationsList.bonitationType)]
    )
    cost = FloatField(
        label = "Koszt nabycia"
    )
    purchaseDate = DateField(
        label = "Data nabycia prawa",
        format = "%Y-%m-%d"        
    )
    possessionRight = SelectField(
        label = "Prawo do nieruchomości",
        choices = [(right.id, right.right) for right in session.query(PossessionRights).order_by(PossessionRights.right)]
    )
    destination = SelectField(
        label = "Przeznaczenie gruntów",
        choices = [(destination.id, destination.destination) for destination in session.query(LandDevelopment).order_by(LandDevelopment.destination)]
    )
    


#---------------------------------------------------------------------
class VaccinesListAddForm(FlaskForm):
    vaccineType = StringField(
        label = "Rodzaj szczepionki"
    )
    unitCost = FloatField(
        label = "Koszt jednostkowy szczepionki"
    )



class FertilizersListAddForm(FlaskForm):
    fertilizerType = StringField(
        label = "Rodzaj nawozu"
    )
    unitCost = FloatField(
        label = "Koszt jednostkowy nawozu [zł/a]"
    )



class HerbicidesListAddForm(FlaskForm):
    herbicideType = StringField(
        label = "Rodzaj herbicydu"
    )
    against = StringField(
        label = "Skuteczny na:"
    )
    unitCost = FloatField(
        label = "Koszt jednostkowy herbicydu [zł/a]"
    )



class PesticidesListAddForm(FlaskForm):
    pesticideType = StringField(
        label = "Rodzaj pestycydu"
    )
    against = StringField(
        label = "Skuteczny na:"
    )
    unitCost = FloatField(
        label = "Koszt jednostkowy pestycydu [zł/a]"
    )
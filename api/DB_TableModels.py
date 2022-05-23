from datetime import date
from unicodedata import category
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine.base import RootTransaction
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from WebServer import db



#TODO: Fields number of characters limits



class TestTab(db.Model):
    __tablename__ = 'TestTab'
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        task: {self.task}'



class AnimalList(db.Model):
    __tablename__ = 'AnimalList'
    id = db.Column(db.Integer, primary_key = True)
    animalType = db.Column(db.String(60), unique=True, nullable=False)

    
    animals = relationship("Animals")
    
    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        animalType: {self.animalType}'



class CropList(db.Model):
    __tablename__ = 'CropList'
    id = db.Column(db.Integer, primary_key = True)
    cropType = db.Column(db.String(60), unique=True, nullable=False)
    uitCost = db.Column(db.Float(12))

    cropstorage = relationship("CropStorage")

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        cropType: {self.cropType}'



class VaccinesList(db.Model):
    __tablename__ = 'VaccinesList'
    id = db.Column(db.Integer, primary_key = True)
    vaccineType = db.Column(db.String(60), unique=True, nullable=False)
    unitCost = db.Column(db.Float(12))

    vaccinations = relationship("Vaccinations")
    
    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        vaccineType: {self.vaccineType}'



class FertilizersList(db.Model):
    __tablename__ = 'FertilizersList'
    id = db.Column(db.Integer, primary_key = True)
    fertilizerType = db.Column(db.String(60), unique=True, nullable=False)
    unitCost = db.Column(db.Float(12))


    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        fertilizerType: {self.fertilizerType}'



class HerbicidesList(db.Model):
    __tablename__ = 'HerbicidesList'
    id = db.Column(db.Integer, primary_key = True)
    herbicideType = db.Column(db.String(60), unique=True, nullable=False)
    against = db.Column(db.String(60), unique=True, nullable=False)
    unitCost = db.Column(db.Float(12))


    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        herbicideType: {self.herbicideType} against: {self.against}'



class PesticidesList(db.Model):
    __tablename__ = 'PesticidesList'
    id = db.Column(db.Integer, primary_key = True)
    pesticideType = db.Column(db.String(60), unique=True, nullable=False)
    against = db.Column(db.String(60), unique=True, nullable=False)
    unitCost = db.Column(db.Float(12))

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        pesticideType{self.pesticideType} \
        against: {self.against}'



class FieldsUpkeep(db.Model):
    __tablename__ = 'FieldsUpkeep'
    id = db.Column(db.Integer, primary_key = True)
    fieldId = db.Column(db.Integer, ForeignKey("Fields.id"))
    procedureType = db.Column(db.Integer, ForeignKey("ProceduresList.id"))
    procedureDate = db.Column(db.Date)

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        fieldId: {self.fieldId}, \
        procedureType: {self.procedureType}, \
        procedureDate: {self.procedureDate}'


class ProceduresList(db.Model):
    __tablename__ = 'ProceduresList'
    id = db.Column(db.Integer, primary_key = True)
    procedureType = db.Column(db.String(60), unique=True, nullable=False)
    unitCost = db.Column(db.Float(12))

    fieldsupkeep = relationship("FieldsUpkeep")
    
    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        procedureType: {self.procedureType}'



class ChemicalProceduresList(db.Model):
    __tablename__ = 'ChemicalProceduresList'
    id = db.Column(db.Integer, primary_key = True)
    procedureType = db.Column(db.String(60), unique=True, nullable=False)

    fieldsupkeepchemical = relationship("FieldsUpkeepChemical")
    
    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        procedureType: {self.procedureType}  \
        unitCost: {self.unitCost}' 



class BonitationsList(db.Model):
    __tablename__ = 'BonitationsList'
    id = db.Column(db.Integer, primary_key = True)
    bonitationType = db.Column(db.String(60), unique=True, nullable=False)
    
    fields = relationship("Fields")

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
            boniType: {self.bonitationType}'



class Fodder(db.Model):
    __tablename__ = 'Fodder'
    id = db.Column(db.Integer, primary_key = True)
    fodderType = db.Column(db.String(60), unique=True, nullable=False)
    unitCost = db.Column(db.Float(12))

    fodderstorage = relationship("FodderStorage")
    
    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        fodderType: {self.fodderType}'



class Fields(db.Model):
    __tablename__ = 'Fields'
    id = db.Column(db.Integer, primary_key = True)
    area = db.Column(db.Float, nullable=False)
    bonitation = db.Column(db.Integer, ForeignKey("BonitationsList.id"))
    cost = db.Column(db.Float(12))
    purchaseDate = db.Column(db.Date)
    possessionRight = db.Column(db.Integer, ForeignKey("PossessionRights.id"))

    buildings = relationship("Buildings")

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        area: {self.area}, \
        nip: {self.nip}, \
        bonitation: {self.bonitation}'



class Buildings(db.Model):
    __tablename__ = 'Buildings'
    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.String(60))
    buildingType = db.Column(db.String(60), nullable=False)
    volume = db.Column(db.Float, nullable=False)
    area = db.Column(db.Float, nullable=False)
    field = db.Column(db.Integer, ForeignKey("Fields.id"))
    cost = db.Column(db.Float, nullable=False)

    animals = relationship("Animals")
    fodderstorage = relationship("FodderStorage")
    cropstorage = relationship("CropStorage")
    milkstorage = relationship("MilkStorage")
    milkstorage = relationship("MilkStorage")
    woolstorage = relationship("WoolStorage")
    honeystorage = relationship ("HoneyStorage")
    seedstorage = relationship("SeedStorage")
    eggstorage = relationship("EggStorage")
    buildingsupkeep = relationship("BuildingsUpkeep")

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        userId: {self.userId} \
        buildingType: {self.buildingType}, \
        volume: {self.volume}, \
        area: {self.area}, \
        field: {self.field}'



class FieldsUpkeepChemical(db.Model):
    __tablename__ = 'FieldsUpkeepChemical'
    id = db.Column(db.Integer, primary_key = True)
    fieldId = db.Column(db.Integer, ForeignKey("Fields.id"))
    procedureType = db.Column(db.Integer, ForeignKey("ChemicalProceduresList.id"))
    fertilizer = db.Column(db.Integer, ForeignKey("FertilizersList.id"))
    pesticide = db.Column(db.Integer, ForeignKey("PesticidesList.id"))
    herbicide = db.Column(db.Integer, ForeignKey("HerbicidesList.id"))
    procedureDate = db.Column(db.Date)
    totalCost = db.Column(db.Float(12))

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        fieldId: {self.fieldId}, \
        chemicalProcedureType: {self.procedureType}, \
        substane: {self.substance}, \
        procedureDate: {self.procedureDate}'




class Harvesting(db.Model):
    __tablename__ = 'Harvesting'
    id = db.Column(db.Integer, primary_key = True)
    field = db.Column(db.Integer, ForeignKey("Fields.id"))
    quantity = db.Column(db.Float(12))
    harvestDate = db.Column(db.Date)

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        area: {self.area}, \
        quantity: {self.quantity}, \
        harvestDate: {self.harvestDate}'


    

class CropStorage(db.Model):
    __tablename__ = 'CropStorage'
    id = db.Column(db.Integer, primary_key = True)
    quantity = db.Column(db.Float, nullable=False)
    building = db.Column(db.Integer, ForeignKey("Buildings.id"))
    crop = db.Column(db.Integer, ForeignKey("CropList.id"))

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        building: {self.building}, \
        quantity: {self.quantity}, \
        crop: {self.crop}'



class FodderStorage(db.Model):
    __tablename__ = 'FodderStorage'
    id = db.Column(db.Integer, primary_key = True)
    fodderType = db.Column(db.Integer, ForeignKey("Fodder.id"))
    building = db.Column(db.Integer, ForeignKey("Buildings.id"))
    quantity = db.Column(db.Float(12), nullable=False)

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        building: {self.building}, \
        quantity: {self.quantity}, \
        fodderType: {self.fodderType}'
    


class Vaccinations(db.Model):
    __tablename__ = 'Vaccinations'
    id = db.Column(db.Integer, primary_key = True)
    animalId = db.Column(db.Integer, ForeignKey("Animals.id"))
    vaccineId = db.Column(db.Integer, ForeignKey("VaccinesList.id"))
    vaccinationDate = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        animalId: {self.animalId}, \
        vaccineId: {self.vaccineId}, \
        vaccinationDate: {self.vaccinationDate}'



class Animals(db.Model):
    __tablename__ = 'Animals'
    id = db.Column(db.Integer, primary_key = True)
    animalType = db.Column(db.Integer, ForeignKey("AnimalList.id"))
    earingId = db.Column(db.String)
    building = db.Column(db.Integer, ForeignKey("Buildings.id"))
    birthDate = db.Column(db.Date)
    acquisitionCost = db.Column(db.Float(12))
    isAlive = db.Column(db.Boolean)
    forMeat = db.Column(db.Boolean)
    

    vaccinations = relationship("Vaccinations")
    sharing = relationship("Shearing")
    milking = relationship("Milking")
    laying = relationship("Laying")
    honeyacquisition = relationship("HoneyAcquisition")
    butchering = relationship("Butchering")

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        animalType: {self.animalType}, \
        earingId: {self.earingId}, \
        building: {self.building}, \
        birthDate: {self.birthDate}, \
        acquisitionCost: {self.acquisitionCost} \
        isAlive: {self.isAlive}, \
        forMear: {self.forMeat}'
    


class Milking(db.Model):
    __tablename__ = 'Milking'
    id = db.Column(db.Integer, primary_key = True)
    animal = db.Column(db.Integer, ForeignKey("Animals.id"))
    volume = db.Column(db.Float(12))
    milkingDate = db.Column(db.Date)
    stored = db.Column(db.Boolean)

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
            animal: {self.animal},\
            volume: {self.volume},\
            milkingDate: {self.milkingDate}, \
            stored: {self.stored}'



class Shearing(db.Model):
    __tablename__ = 'Shearing'
    id = db.Column(db.Integer, primary_key = True)
    animal = db.Column(db.Integer, ForeignKey("Animals.id"))
    mass = db.Column(db.Float(12))
    shearingDate = db.Column(db.Date)
    stored = db.Column(db.Boolean)

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
            animal: {self.animal},\
            mass: {self.mass},\
            shearingDate: {self.shearingDate}, \
            stored: {self.stored}'



class HoneyAcquisition(db.Model):
    __tablename__ = 'HoneyAcquisition'
    id = db.Column(db.Integer, primary_key = True)
    animal = db.Column(db.Integer, ForeignKey("Animals.id"))
    mass = db.Column(db.Float(12))
    acquisitionDate = db.Column(db.Date)
    stored = db.Column(db.Boolean)

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
            animal: {self.animal},\
            mass: {self.mass},\
            acquisitionDate: {self.acquisitionDate}, \
            stored: {self.stored}'



class Laying(db.Model):
    __tablename__ = 'Laying'
    id = db.Column(db.Integer, primary_key = True)
    animal = db.Column(db.Integer, ForeignKey("Animals.id"))
    quantity = db.Column(db.Float(12))
    layingDate = db.Column(db.Date)
    stored = db.Column(db.Boolean)

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
            animal: {self.animal},\
            quantity: {self.quantity},\
            layingDate: {self.layingDate}, \
            stored: {self.stored}'



class Butchering(db.Model):
    __tablename__ = 'Butchering'
    id = db.Column(db.Integer, primary_key = True)
    animal = db.Column(db.Integer, ForeignKey("Animals.id"))
    mass = db.Column(db.Float(12))
    butcheringDate = db.Column(db.Date)
    stored = db.Column(db.Boolean)

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
            animal: {self.animal},\
            mass: {self.mass},\
            butcheringDate: {self.butcheringDate}, \
            stored: {self.stored}'



class MilkStorage(db.Model):
    __tablename__ = 'MilkStorage'
    id = db.Column(db.Integer, primary_key = True)
    building = db.Column(db.Integer, ForeignKey("Buildings.id"))
    volume = db.Column(db.Float(12))
  
    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
            building: {self.building},\
            volume: {self.volume}'



class MeatStorage(db.Model):
    __tablename__ = 'MeatStorage'
    id = db.Column(db.Integer, primary_key = True)
    building = db.Column(db.Integer, ForeignKey("Buildings.id"))
    animalType = db.Column(db.Integer, ForeignKey("AnimalList.id"))
    mass = db.Column(db.Float(12))
  
    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
            building: {self.building},\
            mass: {self.mass} \
            animalType: {self.animalType}'



class WoolStorage(db.Model):
    __tablename__ = 'WoolStorage'
    id = db.Column(db.Integer, primary_key = True)
    building = db.Column(db.Integer, ForeignKey("Buildings.id"))
    mass = db.Column(db.Float(12))
  
    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
            building: {self.building},\
            mass: {self.mass} '



class HoneyStorage(db.Model):
    __tablename__ = 'HoneyStorage'
    id = db.Column(db.Integer, primary_key = True)
    building = db.Column(db.Integer, ForeignKey("Buildings.id"))
    mass = db.Column(db.Float(12))
  
    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
            building: {self.building},\
            mass: {self.mass} '



class EggStorage(db.Model):
    __tablename__ = 'EggStorage'
    id = db.Column(db.Integer, primary_key = True)
    building = db.Column(db.Integer, ForeignKey("Buildings.id"))
    quantity = db.Column(db.Float(12))
  
    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
            building: {self.building},\
            quantity: {self.quantity} '



class SeedStorage(db.Model):
    __tablename__ = 'SeedStorage'
    id = db.Column(db.Integer, primary_key = True)
    building = db.Column(db.Integer, ForeignKey("Buildings.id"))
    quantity = db.Column(db.Float(12))
  
    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
            building: {self.building},\
            quantity: {self.quantity} '



class Revenue(db.Model):
    __tablename__ = 'Revenue'
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)
    category = db.Column(db.String(60))
    subCategory = db.Column(db.String(60))
    sum = db.Column(db.Float(12))

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
            category: {self.category},\
            subcategory: {self.subCategory}, \
            sum: {self.sum}'



class Expenses(db.Model):
    __tablename__ = 'Expenses'
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)
    category = db.Column(db.String(90))
    subCategory = db.Column(db.String(90))
    sum = db.Column(db.Float(12))

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
            category: {self.category},\
            subcategory: {self.subCategory}, \
            sum: {self.sum}'



class BuildingsUpkeep(db.Model):
    __tablename__ = 'BuildingsUpkeep'
    id = db.Column(db.Integer, primary_key = True)
    building = db.Column(db.Integer, ForeignKey("Buildings.id"))
    term = db.Column(db.String(60))
    cost = db.Column(db.Float(12), nullable=False)

    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        id: {self.id} \
        building: {self.building} \
        cost: {self.cost}'



class PossessionRights(db.Model):
    __tablename__ = 'PossessionRights'
    id = db.Column(db.Integer, primary_key = True)
    right = db.Column(db.String(60))


    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        roght: {self.right}, '



class LandDevelopment(db.Model):
    __tablename__ = 'LandDevelopment'
    id = db.Column(db.Integer, primary_key = True)
    destination = db.Column(db.String(60))


    def __repr__(self):
        return f'<{self.__class__.__name__}>: \
        destination: {self.destination}, '


db.create_all()
from django.db import models

class ProvinceChoices(models.TextChoices):
    PINAR_DEL_RIO = 'Pinar del Rio'
    ARTEMISA = 'Artemisa'
    HABANA = 'Habana'
    MAYABEQUE = 'Mayabeque'
    MATANZAS = 'Matanzas'
    VILLA_CLARA = 'Villa Clara'
    CIENFUEGOS = 'Cienfuegos'
    SANCTISPIRITUS = 'Sanctispíritus'
    CIEGO_DE_AVILA = 'Ciego de Avila'
    CAMAGUEY = 'Camagüey'
    LAS_TUNAS = 'Las Tunas'
    GRANMA = 'Granma'
    SANTIAGO_DE_CUBA = 'Santiago de Cuba'
    HOLGUIN = 'Holguín'
    GUANTANAMO = 'Guantánamo'
    ISLA_DE_LA_JUVENTUD = 'Isla de la Juventud'
    
    
class TypePhoneNumberChoices(models.TextChoices):
    CASA = 'Casa'
    MOVIL_PERSONAL = 'Movil Personal'
    TRABAJO = 'Trabajo'

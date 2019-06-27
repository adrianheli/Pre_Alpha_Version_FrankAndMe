from odoo import api, fields, models#Packages von odoo

class Book(models.Model):#models.Model ist eine Klasse
    _name = 'library.book'# interner identifizierer für das Odoo Model -> verbindlich
    _description = 'Book'# user-freundlicher Titel (UI)für das Records des Moduls-> optional
    _order = 'name, date_published desc'#  default Reihenfolge wird benutzt wenn die Records des Models im Browser angezeigt werden,
                            # oder wenn es in einer List-View angezeigt wird. Text-String wenn es als SQL order-by benutzt werden soll
                           # many-to-one field names

    #advanced
    _rec_name = '' # indiziert das Feld das als record Beschreibung benutzt wird wenn es von verwendeten Fields referenziert wird,
                #z.B. einer many-to-one Beschreibung. Default: name Attribut
    _table = '' #Tabellenname welche das Model unterstützt, default :  defined by the ORM , model name mit Underscores statt
                # anstatt Punkte

    _log_access = False # verhindert die automatische Generierung von der audit tracking Fields: create_uid, create_date,
                        # write_uid, und write_date
    _auto = False    #verhindert die automatische Generierung der zugehörigen Datenbank-Tabelle

    #um Module zu erweitern
    _inherit = ''
    _inherits = ''


    # Odoo models werden in einem zentralen Register aufbewahrt (im env - Umgebungs Objekt)
    #code in einer Methode kann self.env['library.book'] um das Model-Klasse abzurufen
    #Konvention für ein Model Name ist eine List mit mehreren Worten getrennt von Punkten library.book.category

    name = fields.Char(
        string = '',#field 's default label, das im UI benutzt wird
        default = True,    #field's default label (UI)
        help = '', # Hilftext wenn User über Field hovert
        readonly=True, #Macht das Field nicht editable , man kann also nur lesen
        required=True, #  macht das Field verbindlich im UI (default)
        index=True,#fügt einen Datenbase Indexauf dem Field,für schenllere Such-Operation
        copy=False,
        groups = '', #Zugriff und Lesezugriff auf eine bestimmte Gruppe
        states ={'done':[('readonly',True)]}, # erwartet einen dictionary mapping Wert für UI -Attribute abhängig
                    # vom Status des Fields.Das Attribut kann als readonly, required, and invisible benutzt werden
    )

    #many - to - one relationship: reference to a record in another model
    publisher_id = fields.Many2one('res.partner', string='Publisher') #1.Argument: related Model, 2. Argument: Field Label


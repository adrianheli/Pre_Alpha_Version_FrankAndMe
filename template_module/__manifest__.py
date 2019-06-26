{
 'name': '', #Name des Moduls -> addon Modul name
 'description': '',# Beschreibung was das Feature machen soll
 'author': '',# Liste von Autoren
 'depends': [''], #Liste von addon-Modulen von den das Modul abhängt. Installiert alle Module in der Liste wenn das Modul selbst installiert werden soll
                      #Wenn Modul-Liste leer füge das Core-Modul in Liste ein
 'application': True,#Boolean Flag ob das Addon-Modul als App in App Liste stehen soll
 'summary': "",#string Untertitel für Modul.
 'version': '1.0',#default 1.0,  http:/​/​semver. org/​ for details. Odoo version vor der module version, z.B. 12.0.1.0.
 'license': 'LGPL-3', #default considered LGPL-3. website: A URL to get more information about the module.
 'category': '', #string mit der FUnktionalität-Kategorie vom Modul, which defaults to Uncategorized.
 'installable': True,  # default True, falsch wenn man nicht möchte das es nicht installiert werden soll
 'auto_install': True,  # Wenn wahr, wird es automatisch installiert sobald alle anderen Module installiert wurden die in der ABhängigkeitsliste standen
# Für glue Module geeignet, welche zwei Feature verbinden sobald sie beide auf der gleichen Instanz installiert wurden
 'demo': [],#Demonstration data für ein Modul
 'data':[
     'views/template.xml',
 ],#hier kommen die ganzen csv und xml Files rein. Das heisst was das Modul wissen muss
}

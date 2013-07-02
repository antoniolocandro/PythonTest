#_author_ Antonio Locandro
#_ArcGIS Version_ 10.0
#_copyright_ GPL

import os
import arcpy #imports the arcpy module from ARCGIS

#workspace to search for MXD's
Workspace=r"l:\\MXD\01_GEN\\" # Hardcoded right now, needs to be changed to accept user input
arcpy.env.workspace = Workspace
#list map documents in folder
mxdList = arcpy.ListFiles("*.mxd")

#Loops through each file in the directory
for filename in mxdList:
    fullpath = os.path.join(Workspace,filename)
    mxd = arcpy.mapping.MapDocument (fullpath) #sets the name of the mxd
    eff_date = arcpy.mapping.ListLayoutElements (mxd,"TEXT_ELEMENT","eff_date")[0] #gets the text element where the effective AIRAC date is placed
    amdt_num = arcpy.mapping.ListLayoutElements (mxd,"TEXT_ELEMENT","amdt_num")[0] #gets the text element where the effective Publication name is placed
    eff_date.text = "25 JUL 13" # hardcoded date
    amdt_num.text = "SECOND EDITION" # hardcoded text
    mxd.title = filename
    mxd.description = "Updated by: Antonio Locandro" +'\n'+"Reason: Second Edition"
    mxd.author = "AIM GIS COCESNA" #sets the owner of the document
    mxd.credits = "(c) COCESNA" #sets copyright
    arcpy.mapping.ExportToPDF(mxd,r"l:\\MXD\01_GEN\\SECOND_EDITION\\"+filename) #exports to a hardcoded folder, need to be change to accept user input
    mxd.makeThumbnail()
    mxd.saveACopy (r"l:\\MXD\01_GEN\\SECOND_EDITION\\"+filename)
    #mxd.save() #saves the file with the updated information




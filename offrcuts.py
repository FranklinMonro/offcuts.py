ofile = open('Offcuts.invent', 'w')#create a txt file to write to
exitProgram = ""
ofile.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<StoreInventoryDataList xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n')
while exitProgram != "YES":
    exitProgram = input("Do you want to EXIT(YES/NO): ")
    if exitProgram == "NO":
        offcutName = input("Pleae enter offcut name: ")
        materialType = input("Please enter the material: ")
        thickness = input("Please enter the thickness: ")
        matWidth = input("Please enter the width: ")
        matLength = input("Please enter the length: ")
        binNumber = input("Please enter the bin number: ")
        NumPieces = input("Please enter the qty: ")
        ofile.write('\t<StoreMaterial>\n'
                '\n'
                        '\t\t\t<Material Name="ArticleNb" Value="'+offcutName+'"/>\n'
			'\t\t\t<Material Name="DinNb" Value="'+materialType+'"/>\n'
			'\t\t\t<Material Name="MatThickness" Value="'+thickness+'"/>\n'
			'\t\t\t<Material Name="MatWidth" Value="'+matWidth+'"/>\n'
			'\t\t\t<Material Name="MatLength" Value="'+matLength+'"/>\n'
			'\t\t\t<Material Name="ChargeNb" Value="'+binNumber+'"/>\n'
			'\t\t\t<Material Name="Inch" Value="false"/>\n'
			'\t\t\t<Material Name="Pound" Value="false"/>\n'
			'\t\t\t<Material Name="NumPieces" Value="'+NumPieces+'"/>\n'
			'\t\t\t<Material Name="MatNb" Value="X"/>\n'
                '\n'
	'\t</StoreMaterial>\n')#write input to txt file

ofile.write('\n\n</StoreInventoryDataList>')


ofile.close()#close file

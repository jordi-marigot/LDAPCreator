
import os
import getpass

accio = int(input("Indica que vols fer: \n (1)Crear Usuari (2)CrearOrganitzacio "))
if accio == 1:
    numUsers = int(input("Indica el numero de usuaris que volem crear: "))

    file = open ("CrearUser.ldif", "w")

    if numUsers > 0:
        i = 0
        while int(i) < numUsers:
            print("--- "+ str(i) +" ---")
            uidUser = input("Identificatiu del Usuari: ")
            group = input("Grup al que partany: ")
            userName = input("Nom del Usuari: ")
            userSecondName = input("Cognom del Usuari: ")
            pwd = getpass.getpass("Contrasenya: ")
            ubicacio = input("Ubicacio: ")
            telefon = input("Telefon: ")
            mailDefault = userName.lower()+"."+userSecondName.lower()+"@"
            mail = input("E-mail: "+ mailDefault)
            mail = mailDefault+mail

            file.write("cn: "+userName + os.linesep)
            file.write("gidNumber: 20000" + os.linesep)
            file.write("objectClass: top" + os.linesep)
            file.write("objectClass: posixGroup" + os.linesep + os.linesep)
            file.write("dn: uid="+userName+",ou="+group+",dc=joviat,dc=cat" + os.linesep)
            file.write("uid: "+uidUser + os.linesep)
            file.write("uidNumber: 2000"+ str(i) + os.linesep)
            file.write("uidNumber: 20001" + os.linesep)
            file.write("cn: "+userName + os.linesep)
            file.write("sn: "+userSecondName + os.linesep)
            file.write("objectClass: top" + os.linesep)
            file.write("objectClass: person" + os.linesep)
            file.write("objectClass: posixAccount" + os.linesep)
            file.write("loginShell: /bin/bash" + os.linesep)
            file.write("homeDirectory: /home/"+userName + os.linesep)
            file.write("userPassword: {SSHA} "+pwd + os.linesep)
            file.write("roomNumber: "+ubicacio + os.linesep)
            file.write("telephoneNumber: "+telefon + os.linesep)
            file.write("mail: "+mail + os.linesep + os.linesep)
            

            print (".............")
            i += 1
    file.close()
    


    

else:
    org = input("Nom de la Organitzacio: ")

    file = open ("CrearOrg.ldif", "w")
    file.close()




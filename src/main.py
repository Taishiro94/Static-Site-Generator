import os, shutil

def main():
    inhalt= get_files("static/")
    move_files(inhalt)
    

def get_files(pfad):
    results=[]
    inhalt = os.listdir(pfad)
    for element in inhalt: 
        if len(element.split(".")) == 2:
            results.append(pfad + element)
        else:
            x = get_files(pfad + element+"/")
            for i in x:
                results.append(i)
    return results

def move_files(pfadlist):
    workpaths = []
    for pfad in pfadlist:
        pfady=""
        workpfad = pfad.split("/", 1)
        workpfad[0] = "public/"
        for p in workpfad:
            pfady+=p
        workpaths.append(pfady)
    if os.path.exists("public/"):
        shutil.rmtree("public/")
    os.mkdir("public/")

    #Create paths    
    for pfad in workpaths:
        teilpfad = pfad.split("/")
        while len(teilpfad) > 2:
            teil_1 = teilpfad[0]
            teil_2 = "/" + teilpfad[1] + "/"
            os.mkdir(teil_1 + teil_2)
            new_teilpfad = [teil_1 + teil_2]
            for part in teilpfad:
                if part == teilpfad[0] or part == teilpfad[1]:
                    continue
                else:
                    new_teilpfad.append(part)
            teilpfad = new_teilpfad
    i=0
    for pfad in pfadlist:
        shutil.copy(pfad, workpaths[i])
        i+=1

        

        
        
            
        

def copy_static():
    pass

main()
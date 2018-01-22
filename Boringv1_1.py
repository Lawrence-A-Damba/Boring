import os, fnmatch
boringFileNames = []
OutPut=open('OutPut.txt','w')
listOfFiles = os.listdir('.')
pattern = input("Enter boring file pattern or hit enter for *.TXT ") or "*.TXT"
horizScaleFactor = input("Enter horizontal scale factor: ")
horizScaleFactor = float(horizScaleFactor)
vertScaleFactor = input("Enter vertical scale factor: ")
vertScaleFactor = float(vertScaleFactor)
counter=1
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        boringFileNames.append(entry)
print('#',boringFileNames, file=OutPut)
for boringName in boringFileNames:
    open_file=open(boringName,'r')
    file=open_file.readlines()
    open_file.close()
    elevLine=file[7]
    gndElev=float(elevLine[10:17])
    boringName=boringName.replace('.TXT','')
    print('LV=', boringName, '\n#Ground Elev. = ',gndElev, file=OutPut)
    print('ac= UCT'+str(counter), file=OutPut)
    counter+=1
    counter2=1
    counter3=1
    for item in range(0,len(file)-1):
        line=file[item]
        try:
            if line[59].isdigit():
                depth=float(line[5:11])
                cohesion=int(line[55:59])/2000
                #wetDensity=int(line[59:62])
                #print('Depth = ',depth, 'Depth elev. = ', round(gndElev-depth,2), 'Cohesion = ',
                #cohesion, 'Wet Density = ', wetDensity)
                print('xy= ' + str(round(cohesion*horizScaleFactor,2)) + ',' + str(round(vertScaleFactor*(gndElev-depth),2))
                      , file=OutPut)
                
        except IndexError:
                pass
        if line[0]=='D' and line[1]=='e':
            if line[16]=='/':
                elev2=float(line[17:25])
            else:
                elev2=float(line[18:26])
        else:
            pass
        if line[0]=='C' and line[1]=='o':
            cohesion2=float(line[10:17])
            if counter2>0:
                print('ac= QTST'+str(counter3), file=OutPut)
                counter2-=1
                counter3+=1
            else:
                pass
            print('xy=',str(round(cohesion2*horizScaleFactor,2)) + ',' + str(round(elev2*vertScaleFactor,2)), file=OutPut)
        else:
            pass
OutPut.close()




import os, fnmatch
boringFileNames = []
listOfFiles = os.listdir('.')
pattern = "*.TXT"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        boringFileNames.append(entry)
print('#',boringFileNames)
for boringName in boringFileNames:
    open_file=open(boringName,'r')
    file=open_file.readlines()
    open_file.close()
    elevLine=file[7]
    gndElev=float(elevLine[10:17])
    boringName=boringName.replace('.TXT','')
    print('LV', boringName, '\n#Ground Elev. = ',gndElev)
    for item in range(0,len(file)-1):
        line=file[item]
        try:
            if line[59].isdigit():
                depth=float(line[5:11])
                cohesion=int(line[55:59])/2000
                #wetDensity=int(line[59:62])
                #print('Depth = ',depth, 'Depth elev. = ', round(gndElev-depth,2), 'Cohesion = ',
                #cohesion, 'Wet Density = ', wetDensity)
                print('xy= ' + str(round(cohesion,2)) +',', round(gndElev-depth,2))
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
            print('xy=',str(round(cohesion2,2)) + ', ' + str(elev2))
        else:
            pass




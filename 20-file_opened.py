with open('/tmp/a.txt', 'r') as file:
    x = True
    print("Abriendo el archivo para buscar ip6-allnodes")
    for line in file:
        if x:    #
            if "Server ASR Disabled" in line:
                print(line)
                x = False
        else:
            print(line)
            if "SODA session starting " in line:
                x = True
file.close()

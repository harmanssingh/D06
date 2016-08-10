with open("roster.txt", "r") as f:
    txt=f.readlines()
    listofnames=''
    count=0
    for names in txt:
        name=names.split()
        if 'e' in name[0] or 'E' in name[0]:
            listofnames=listofnames+name[0]+'\n'
            count=count+1
    print("The number of names that contain the letter e is : "+str(count)+"\nThe names that contain the letter e are :"+listofnames)

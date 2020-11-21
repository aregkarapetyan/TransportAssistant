'''
Created by Areg Karapetyan
'''

#Extra file not needed for the Main.py
#Converts old data with strings to instances for class Streets

#old data of streets and routes
bus_str_0 = []
bus_str_1 = ["Khaghagh Don","Titogradyan","Ayvazovskiy","Erebuni","Artsakh","Tigran Mets","Republic Square","Amiryan","Mashtots","Baghramyan","Kasyan","Komitas","Azatutyuan","Sevak","Dro","Lepsius"]
bus_str_2 = []
bus_str_3 = ["Arno Babajanyan","Raffi","Sebastia","Leningradyan","Kievyan","Kasyan","Komitas","Davit Anhaght","Rubinyants","Gai","Badal Mouradian","Davit Bek","Hunan Avetisyan"]
bus_str_4 = []
bus_str_5 = ["Kochinyan","Tevosyan","Hovhannisyan","Bakunts","Gyulikevkhyan","Gai","Myasnikyan","Abovyan","Moskovyan","Mashtots","Victory Bridge","Admiral Isakov","Kilikia"]
bus_str_6 = []
bus_str_7 = ["Khaghagh Don","Titogradyan","Ayvazovskiy","Erebuni","Atoyan","Belinsku","Sasuntsi Davit","Tigran Mets","Khanjyan","Tumanyan","Mashtots","Koryun","Abovyan","Myasnikyan","Saralanj","Avetisyan","Vagharshyan","Sasna Tzrer","Tigran Petrosyan","Yeghvard"]
bus_str_8 = ["Tigran Petrosyan","Iosifyan","Halabyan","Kievyan","Baghramyan","Moskovyan","Abovyan","Myasnikyan","Gai","Badal Muradian","Davit Bek","Avetisyan","Vilnius"]
bus_str_9 = []
bus_str_10 = []
bus_str_11 = []
bus_str_12 = ["Aeracia","Shiraki","Artashisyan","Bagratunyats","Sebastia","Hasratyan","Janibekyan","Bshinjaghyan","Margaryan","Halabyan","Iosifyan","Tigran Petrosyan"]
bus_str_13 = ["Gazprom","Tbilisyan","Qanaqercu","Azatutyan","Komitas","Kasyan","Baghramyan","Sayat-Nova","Charents","Radiotun"]
bus_str_14 = ["Lepsius","Dro","Sevak","Ulnetsi","Nersisyan","Azatutyan","Saralanj","Abovyan","Moskovyan","Khanjyan","Tigran Mets","Artshakh","Nzhdehi","Arshakunyats","Shiraki","Araratyan","Nerqin Charbakh"]
bus_str_15 = ["Badal Mouradian","Shopron","Gyurjyan","Jughai","Nanseni","Samvel Safaryani","Gai","Myasnikyan","Abovyan","Moskovyan","Khanjyan","Agatangeghos","Arshakunyats","Nzhdehi","Bagratunyats","Artashisyan","Shiraki"]

bus_str = [bus_str_0,bus_str_1,bus_str_2,bus_str_3,bus_str_4,bus_str_5,bus_str_6,bus_str_7,bus_str_8,bus_str_9,bus_str_10,bus_str_11,bus_str_12,bus_str_13,bus_str_14,bus_str_15]

#convert to creation of instance for class Streets
streets = []
for i in range(len(bus_str)):
    for j in range(len(bus_str[i])):
        modified_name = bus_str[i][j].replace(" ", "_")
        streets.append(modified_name + ' = Streets("' + bus_str[i][j] + '")')

#Sorts streets in alphabetical order
sorted_streets = sorted(streets)

#Deletes duplicates of already sorted streets
no_duplicate_streets = list(dict.fromkeys(sorted_streets))

#prints all streets in a comfy way to create instance of class
for i in range(len(no_duplicate_streets)):
    print (no_duplicate_streets[i])

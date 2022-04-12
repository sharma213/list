# import random
# import random
# girl_name=["shivangi-:303,bed,no.5","anshika-:304,bed.no.2","neha-:103,bed,no.4"]
# random.shuffle(girl_name)
# i=0
# while i<len(girl_name):
#     print(girl_name[i])
#     i=i+1

import random
girl_name=["neha","kajal","komal","pooja","anshika","moni"]
Rooms_number=[101,102,103,104,201,403]
Rooms_beds=[1,2,3,4,5,6]
random.shuffle(Rooms_beds)
random.shuffle(girl_name)
random.shuffle(Rooms_number)
i=0
while i<len(girl_name):
    print(girl_name[i],"room no",Rooms_number[i],"bed no",Rooms_beds[i])
    # i=i+1
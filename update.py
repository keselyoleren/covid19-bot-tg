import requests
import json

res = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()

for a in res:
    for key, val in a.items():
        if val['Provinsi'] == "Jawa Timur":
            message = " \033 Update covid19 \033 \n \n \n Wilayah " , val['Provinsi']  , "\n positif" , val['Kasus_Posi'] , "\n Sembuh" , val['Kasus_Semb'] , "\n Meninggal" , val['Kasus_Meni'] 
            print(message)
            # print("probinsi" + val['Provinsi'])
            # print("positif" , val['Kasus_Posi'])
            # print("Sembuh" , val['Kasus_Semb'])
            # print("Meninggal", val['Kasus_Meni'])
        # else:
        #     print('kosong')
    # print(a['attributes'])
    # data = a['attributes']
    # for key,val in data.value():
    #     print(key,val)

# c = {'FID': 32, 'Kode_Provi': 82, 'Provinsi': 'Maluku Utara', 'Kasus_Posi': 1, 'Kasus_Semb': 0, 'Kasus_Meni': 0}

# for key, value in c.items():
#     print(key, value)
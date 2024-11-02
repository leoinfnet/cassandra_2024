input_file = open('../dados/streaming_viewership_data.csv', 'r')
output_file = open("../dados/generos_por_pais.csv", 'w')

for line in input_file.readlines():
    splited_line = line.split(",")
    user_id = splited_line[0]
    genero = splited_line[5]
    pais = str.lower(splited_line[6])
    new_line = f"{pais},{genero},{user_id}\n"
    #print(new_line)
    output_file.write(new_line)

#eb4f9229-74df-45f6-baac-cf19241b8b30,cb2142a7-0750-49ed-b8ac-a975fe1ff69a,232,11,90.04452533,Sci-Fi,Sudan,56,Female,Premium,3,Spanish,Smartphone,Reedshire,4K,73

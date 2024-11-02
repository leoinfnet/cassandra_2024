input_file = open('../dados/streaming_viewership_data.csv', 'r')
output_file = open("../dados/generos_por_idade.csv", 'w')

for line in input_file.readlines():
    splited_line = line.split(",")
    user_id = splited_line[0]
    genero = splited_line[5]
    idade = splited_line[7]
    new_line = f"{idade},{genero},{user_id}\n"
    #print(new_line)
    output_file.write(new_line)

#eb4f9229-74df-45f6-baac-cf19241b8b30,cb2142a7-0750-49ed-b8ac-a975fe1ff69a,232,11,90.04452533,Sci-Fi,Sudan,56,Female,Premium,3,Spanish,Smartphone,Reedshire,4K,73

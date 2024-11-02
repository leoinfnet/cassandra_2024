input_file = open('../dados/streaming_viewership_data.csv', 'r')
output_file = open("../dados/qualidade_por_pais.csv", 'w')

for line in input_file.readlines():
    splited_line = line.split(",")
    user_id = splited_line[0]
    pais = str.lower(splited_line[6])
    qualidade = splited_line[14]
    new_line = f"{pais},{qualidade},{user_id}\n"
    #print(new_line)
    output_file.write(new_line)
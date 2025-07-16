import json

def transform_macadava_list_(pairs_file, colour_file, file_write_name):
    with open(pairs_file) as file:  
        data_pair = json.load(file)
    with open(colour_file) as file:
        data_colour = json.load(file)
    
    result = {
        "colour_1": [],
        "colour_2": [],
        "dist": []
    }

    for i in range(len(data_pair)):
        pair = data_pair[i]
        
        color1 = data_colour.get(str(pair[1]), [0, 0, 0])[:3]
        color2 = data_colour.get(str(pair[2]), [0, 0, 0])[:3]
        diff = pair[3]

        result["colour_1"].append({
            "x": color1[0],
            "y": color1[1],
            "Y": color1[2]
        })
        
        result["colour_2"].append({
            "x": color2[0],
            "y": color2[1],
            "Y": color2[2]
        })
        
        result["dist"].append(diff)

    with open(file_write_name, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

# Example call
pairs_file = 'table1.json'
colour_file = 'table2.json'
file_write_name = 'macadam_1974.json'
transform_macadava_list_(pairs_file, colour_file, file_write_name)
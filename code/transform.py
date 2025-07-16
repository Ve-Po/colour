import json
import colour
import numpy as np  # Добавляем импорт numpy

def xyz_to_dict_xyY(colour_xyz):
    colour_xyY = colour.XYZ_to_xyY(colour_xyz)
    colour_res = dict()
    colour_res["x"] = colour_xyY[0]
    colour_res["y"] = colour_xyY[1]
    colour_res["Y"] = colour_xyY[2]
    return colour_res


def transform_dv_pair_xyz(file_read_name, file_write_name):
    with open(file_read_name) as file:  
        data = json.load(file)
    
    d = dict()
    colours_1 = []
    colours_2 = []
    
    for pair in data["pairs"]:
        colour_1 = xyz_to_dict_xyY(data["xyz"][pair[0]])
        colour_2 = xyz_to_dict_xyY(data["xyz"][pair[1]])
        
        colours_1.append(colour_1)
        colours_2.append(colour_2)
    
    d["colour_1"] = colours_1
    d["colour_2"] = colours_2
    d["dist"] = data["dv"]
    
    with open(file_write_name, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4)

def transform_ebner_fairchild(file_read_name, file_write_name):
    with open(file_read_name) as file:  
        data = json.load(file)
    d = dict()
    colours_1 = []
    colours_2 = []
    dist = []
    for elem in data["data"]:
        colour_1 = xyz_to_dict_xyY(elem["reference xyz"])
        for colour_2_xyz in elem["same"]:
            colour_2 = xyz_to_dict_xyY(colour_2_xyz)
            colours_1.append(colour_1)
            colours_2.append(colour_2)
            dist.append(0)
    d["colour_1"] = colours_1
    d["colour_2"] = colours_2
    d["dist"] = dist

    with open(file_write_name, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4)



file_read_name = 'Data/ebner_fairchild.json'
file_write_name = 'Transformed_Data/ebner_fairchild.json'
transform_ebner_fairchild(file_read_name, file_write_name)

from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map,delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

#def import_folder(path):
#    surface_list = []
#
#    for _,__,img_files in walk(path):
#        for image in img_files:
#            full_path = path + '/' + image
#            image_surf = pygame.image.load(full_path).convert_alpha()
#            surface_list.append(image_surf)
#
#    return surface_list


#Mac fix for how files are loaded
def import_folder(path):
    image_list = []
    surface_list = []
    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path +  '/' + image
            image_list.append(full_path)
    for image in sorted(image_list):
        image_surf = pygame.image.load(image).convert_alpha()
        surface_list.append(image_surf)

    return surface_list

x = {}
coords = []
name = []
no_w = int(input("Enter the Number of Warehouse:"))
for i in range(no_w):
    temp_name = input(f"Enter the Name of Warehouse {i + 1}:")
    name.append(temp_name)
    temp_lat = float(input("Enter Latitude:"))
    temp_long = float(input("Enter Longitude:"))
    temp_coords = (temp_lat,temp_long)
    coords.append(temp_coords)
for i in range(no_w):
    x[name[i]] = coords[i]

def get_loc(place):
    for i in x.keys():
        if i == place:
            return x[place]

if __name__ == "__main__":
    place = input("Enter place name:")
    y = get_loc(place)
    if y :
        print(f"{place} is in {x[place]} ")
"""
Module make a map
"""
import folium
import geopy


def map_making(places):
    """
    Function makes a map
    """
    my_map = folium.Map(location=[places[0][1][0], places[0][1][1]])

    fg_loc = folium.FeatureGroup(name="Closest location")

    for (name, [lat, lon]) in places:
        fg_loc.add_child(folium.Marker(location=[lat, lon],
                                       popup=folium.Popup(name),
                                       icon=folium.Icon(color="black")))
    my_map.fit_bounds(fg_loc.get_bounds())
    my_map.add_child(fg_loc)
    my_map.add_child(folium.LayerControl())
    return my_map.get_root().render()


def find_coordinates(place):
    """
    The function find the distance
    """
    try:
        geolocator = geopy.geocoders.Nominatim(user_agent="syla_liuby")
        location = geolocator.geocode(place)
        lat, long = location.latitude, location.longitude
    except Exception:
        place_ls = place.split(", ")
        if len(place_ls) == 1:
            return -1
        shorter_place = ", ".join(place_ls[1:])
        return find_coordinates(shorter_place)
    return [lat, long]


def iter_places(places):
    """
    Function iter friends' location
    """
    incorrect_places = []
    for place_inf in places:
        location = place_inf[1]
        new_location = find_coordinates(location)
        if new_location == -1:
            incorrect_places.append(place_inf)
        else:
            place_inf[1] = new_location
    for place in incorrect_places:
        places.remove(place)
    return map_making(places)

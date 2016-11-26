routes = []

def nearest_neighbor(cities, start):
    path = [start]
    currentCity = start
    i = 0
    while len(cities) > len(path): 
        i+=1
        #List that is left

        #filter list out of dict values for current city
        print(path)
        #min_dist_key = currentCity
        dist = 9999
        for i, value in enumerate(cities[currentCity]):
            if((value not in path) & (dist > cities[currentCity][value])):
                dist = (cities[currentCity][value])
                min_dist_key = value
        
        currentCity = min_dist_key
        path.append(currentCity)
        
    return path

if __name__ == '__main__':
    cities = {
        'RV': {'S': 195, 'UL': 86, 'M': 178},
        'S': {'RV': 195, 'UL': 107, 'M': 230},
        'UL': {'RV': 86, 'S': 107, 'M': 123},
        'M': {'RV': 178, 'S': 230, 'UL': 123}
    }

    #print("Start: River City")
    shortRout = nearest_neighbor(cities, 'RV')
    print(shortRout)
    #routes.sort()
    #if len(routes) != 0:
        #print("Shortest route: %s" % routes[0])
     #   print('k')
import random

routes = []

def sim_annealing(cities, start):
    # This function uses sim_annealing which creates random paths and checks if the previous path is shorter than the old path.
   
    # Link to source which I used as explanation of simulated annealing: http://katrinaeg.com/simulated-annealing.html
    for i in range(5000):
        print(i)
        best_tot_dist = None
        best_path = None
        path, tot_dist = gen_rand_path(cities, start)

        # If first run then var is None and first value is equal to best value
        if(best_tot_dist == None):
            best_tot_dist = tot_dist
            best_path = path
        
        # Else check if current best distane is higher than total distance of function.
        elif(best_tot_dist > tot_dist):
            best_path = path
            best_tot_dist = tot_dist

    return best_path, best_tot_dist

def gen_rand_path(cities, start):
     # Generate random solution
    current_city = start 
    path = [start]
    tot_dist = 0
    
    while len(cities) > (len(path)):
        # Set previous city to determine total distance from previous city to new city.        
        prev_city = current_city
        
        # Get random pick for city that is not already in path
        current_city = random.choice([a for a in cities[current_city].keys() if a not in path])

        # Calculate total distance       
        tot_dist += cities[prev_city][current_city]

        # Append current city to path
        path.append(current_city)

    return path, tot_dist

def nearest_neighbor(cities, start):
    path = [start]
    current_city = start
    total_distance = 0
    
    while len(cities) > (len(path)): 
        # Set dist equal to max value of current city (init)
        dist = max(cities[current_city].values())
        for value in cities[current_city]:
            # If value is not in path already AND the value is smaller or equal than distance, 
            # set distance and key equal to current value.
            if((value not in path) & (dist >= cities[current_city][value])):
                dist = cities[current_city][value]
                min_dist_key = value
        
        total_distance += cities[current_city][min_dist_key]
        current_city = min_dist_key
        path.append(current_city)
        
    return path, total_distance

if __name__ == '__main__':
    # Created new dataset so that the nearest_neighbor function is more realistic and more simplistic to calculate.
    cities = {
        'RV': {'S': 195, 'UL': 86, 'M': 178},
        'S': {'RV': 195, 'UL': 107, 'M': 230},
        'UL': {'RV': 86, 'S': 107, 'M': 123},
        'M': {'RV': 178, 'S': 230, 'UL': 123}
    }

    short_route_sa, tot_dist_sa = sim_annealing(cities, 'RV')
    short_route_nn, tot_dist_nn = nearest_neighbor(cities, 'RV')

    if(tot_dist_sa > tot_dist_nn):
        short_route = short_route_nn
        tot_dist = tot_dist_nn
        best_func = nearest_neighbor.__name__

    else:
        short_route = short_route_sa
        tot_dist = tot_dist_sa
        best_func = sim_annealing.__name__


    print('Shortest route: ' + str(short_route) + '. Total distance: ' + str(tot_dist) 
        + '. Best function : ' + best_func)

    # Note: I think my dataset should be larger to see the full potential of sim_annealing. I notice that sometimes
    # the function returns the smallest value possible (which is awesome), but most of the time (even if I iterate 500k times)
    # it still does not find the best solution or a solution better than nearest_neighbor. Having more data would
    # result in nearest_neighbor being larger, since picking the nearest neighbor won't be any good when we have values
    # that have a great distance between eachother. Thanks Sirajology, I really liked this challenge :))!

    # Last note: The best/shortest output the functions can generate is the following output:
    # Shortest route: ['RV', 'M', 'UL', 'S']. Total distance: 408. Best function : sim_annealing
    # I've decided to add this since it can take a few times before sim_annealing actually gets to this output.
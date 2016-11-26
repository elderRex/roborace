'''
Grow obstacle by cart using reflection
Input: Coord of cart vertices relative to world coordinate
Output: Grown points set of each obstacle in the form of
[[(x1,y1),(x2,y2)...],[(),()...],...]
 obs 1                  obs2    etc
'''
half_cart = 11.5
cart_grow = [(0,0)]

def get_R(cart_x,cart_y,cart_ori):
    global cart_grow
    cart_vertex = []
    cart_vertex.append((cart_x + half_cart, cart_y + half_cart))
    cart_vertex.append((cart_x - half_cart, cart_y + half_cart))
    cart_vertex.append((cart_x + half_cart, cart_y - half_cart))
    cart_vertex.append((cart_x - half_cart, cart_y - half_cart))
    print cart_vertex
    for i in range(1,4):
        cart_grow = cart_grow + [(cart_vertex[i][0]-cart_vertex[0][0],cart_vertex[i][1]-cart_vertex[0][1])]


def my_grow_obs(cart_x,cart_y,cart_ori,init_obs):
    global half_cart
    print "in my grow"
    get_R(cart_x,cart_y,cart_ori)

    init_obs = grow_stuff(init_obs)

    return init_obs

def grow_stuff(init_obstacles):
    global cart_grow
    for i in range(0,len(init_obstacles)):
        update_obs = []
        for j in range(0,len(init_obstacles[i])):
            for k in range(0,4):
                update_obs += [(init_obstacles[i][j][0]+cart_grow[k][0],init_obstacles[i][j][1]+cart_grow[k][1])]
        init_obstacles[i] = update_obs
        print init_obstacles[i]

    return init_obstacles

from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 0, 255 ]
matrix = new_matrix()


m2 = new_matrix(0, 0)

print("\nTesting add_edge (which implements add_point): Adding (1, 2, 3), (4, 5, 6)  m2 = ")
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)

print("Creating matrix m1 = " + "\n")
m1 = new_matrix(0,0)
add_edge(m1,1,2,3,4,5,6)
add_edge(m1,7,8,9,1,2,3)
print_matrix(m1)

print("Testing ident. m1 = " + "\n")
ident(m1)
print_matrix(m1)

print("Testing Matrix mult. m1 * m2 = " + "\n")
matrix_mult(m2, m1)
print_matrix(m2)


helo = new_matrix(0,0)
add_edge(helo,90,10,0,90,90,0)
add_edge(helo,90,90,0,120,120,0)
add_edge(helo,120,120,0,150,90,0)
add_edge(helo,150,90,0,150,10,0)
add_edge(helo,90,90,0,150,90,0)
add_edge(helo,90,10,0,150,10,0)

draw_lines( helo, screen, color )

house2 = new_matrix(0,0)
color = [255, 0, 0]
add_edge(house2,190,100,0,190,190,0)
add_edge(house2,190,190,0,220,220,0)
add_edge(house2,220,220,0,250,190,0)
add_edge(house2,250,190,0,250,100,0)
add_edge(house2,190,190,0,250,190,0)
add_edge(house2,190,100,0,250,100,0)

draw_lines( house2, screen, color )

street1 = new_matrix(0,0)
color = [0,160,160]
add_edge(street1,0,200,0,300,500,0)
add_edge(street1,0,150,0,350,500,0)

draw_lines( street1, screen, color )

house3 = new_matrix(0,0)
color = [0,255,0]
add_edge(house3,290,200,0,290,290,0)
add_edge(house3,290,290,0,320,320,0)
add_edge(house3,320,320,0,350,290,0)
add_edge(house3,350,290,0,350,200,0)
add_edge(house3,290,290,0,350,290,0)
add_edge(house3,290,200,0,350,200,0)

draw_lines( house3, screen, color )

house4 = new_matrix(0,0)
color = [255,0,255]
add_edge(house4,390,300,0,390,390,0)
add_edge(house4,390,390,0,420,420,0)
add_edge(house4,420,420,0,450,390,0)
add_edge(house4,450,390,0,450,300,0)
add_edge(house4,390,390,0,450,390,0)
add_edge(house4,390,300,0,450,300,0)

draw_lines( house4, screen, color )

color = [245,180,247]
coolstuff = new_matrix(0,0)
for i in range(200):
    if (i % 2 == 0 and i % 3 == 0):
        add_edge(coolstuff,i,i*2,0,i*3,i,0)

draw_lines( coolstuff, screen, color )
    

display(screen)
save_ppm(screen, 'matrix.ppm')
save_extension(screen, 'matrix.png')

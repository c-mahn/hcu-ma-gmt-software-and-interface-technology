# PGG1011: Final Python exercise
# #############################################################################

# Import the math module

# Compute the volume and surface area of cylinder with math.pi


# Autoren:
# Christopher Mahn

# #############################################################################

# Import von Bibliotheken
# -----------------------------------------------------------------------------

import math as m

# Funktionen
# -----------------------------------------------------------------------------

def cylinder_volume(r, h):
    return(m.pi*(r**2)*h)

def cylinder_surface(r, h):
    return(2*m.pi*(r**2)+2*m.pi*r*h)

# Klassen
# -----------------------------------------------------------------------------

# Beginn des Programms
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    print(cylinder_volume(2, 5))
    print(cylinder_surface(2, 5))

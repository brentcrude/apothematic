#KNERD2026
'''
4/2026 to 5/2026
Keshav Nishanth <knerd2026>
Geometry Honors (P5)
Apothematic

UPDATES:
when using getter functions with same name as var, it breaks
 - rename actual attributes to "<varname>attr"
also add an Ankylosaurus - Caden Cai <mangocartaguys>
'''

#Helper Functions for Apothematic
import math
def sin(angle):
    return math.sin(math.radians(angle))
def cos(angle):
    return math.cos(math.radians(angle))
def tan(angle):
    return math.tan(math.radians(angle))
def sqrt(num):
    return math.sqrt(num)
pi = math.pi
def indent(text):
    return ''.join('  '+line for line in text.splitlines(True))
# Apothematic

class regularpolygon(object):
    def __init__(self, sides, sidelength):
        self.sidesattr = sides
        self.sidelengthattr = sidelength
        #calculate radius, apothem
        self.angleattr = 180*(self.sidesattr - 2)/self.sidesattr #interior angle formula - verify
        self.apothemattr = tan(self.angleattr/2)*self.sidelengthattr/2 #sohcahtoa: opposite/adjacent * adjacent
        self.radiusattr = 1/(cos(self.angleattr/2)/(self.sidelengthattr/2))
        #sohcahtoa: 1/([adjacent/hypotenuse] / adjacent)
        self.perimeterattr = self.sidesattr * self.sidelengthattr #It's a regular polygon
        self.areaattr = (1/2) * self.perimeterattr * self.apothemattr #A = 1/2 pa
    def sides(self):
        return self.sidesattr
    def sidelength(self):
        return self.sidelengthattr
    def apothem(self):
        return self.apothemattr
    def radius(self):
        return self.radiusattr
    def perimeter(self):
        return self.perimeterattr
    def angle(self):
        return self.angleattr
    def area(self):
        return self.areaattr
    def __repr__(self):
        return f'''REGULAR POLYGON:
Sides: {self.sides()}
Sidelength: {self.sidelength()}
Apothem: {self.apothem()}
Radius (Circumcircle Radius): {self.radius()}
Interior Angle Measure: {self.angle()}
Perimeter: {self.perimeter()}
Area: {self.area()}
'''

#ALERT: Functionality not confirmed beyond this point
#****************************************************

class square(regularpolygon):
    def __init__(self, sidelength):
        regularpolygon.__init__(4, sidelength)
        self.diagonalattr = sqrt(2)*self.sidelength
    def diagonal(self):
        return self.diagonalattr
    def __repr__(self):
        return f'''SQUARE:
Sides: {self.sides()}
Sidelength: {self.sidelength()}
Apothem: {self.apothem()}
Radius (Circumcircle Radius): {self.radius()}
Interior Angle Measure: {self.angle()}
Diagonal Length: {self.diagonal()}
Perimeter: {self.perimeter()}
Area: {self.area()}
'''
class pentagon(regularpolygon):
    def __init__(self, sidelength):
        regularpolygon.__init__(5, sidelength)
    def __repr__(self):
        return f'''PENTAGON:
Sides: {self.sides()}
Sidelength: {self.sidelength()}
Apothem: {self.apothem()}
Radius (Circumcircle Radius): {self.radius()}
Interior Angle Measure: {self.angle()}
Perimeter: {self.perimeter()}
Area: {self.area()}
'''
class hexagon(regularpolygon):
    def __init__(self, sidelength):
        regularpolygon.__init__(6, sidelength)
    def __repr__(self):
        return f'''HEXAGON:
Sides: {self.sides()}
Sidelength: {self.sidelength()}
Apothem: {self.apothem()}
Radius (Circumcircle Radius): {self.radius()}
Interior Angle Measure: {self.angle()}
Perimeter: {self.perimeter()}
Area: {self.area()}
'''

class rectangle(object):
    def __init__(self, length, width):
        self.lengthattr = length
        self.widthattr = width
        self.areaattr = self.lengthattr * self.widthattr
        self.diagonalattr = sqrt((self.lengthattr**2) + (self.widthattr**2))
        self.perimeterattr = 2*(self.lengthattr + self.widthattr)
    def length(self):
        return self.lengthattr
    def width(self):
        return self.widthattr
    def area(self):
        return self.areaattr
    def perimeter(self):
        return self.perimeterattr
    def diagonal(self):
        return self.diagonalattr
    def __repr__(self):
        return f'''RECTANGLE:
Length: {self.length()}
Width: {self.width()}
Diagonal Length: {self.diagonal()}
Perimeter: {self.perimeter()}
Area: {self.area()}
'''

#create something to return height of trapezoid given all sides
class trapezoid(object):
    def __init__(self, base1, base2, height, perimeter=None):
        self.b1attr=base1
        self.b2attr=base2
        self.medianattr=(self.b1attr+self.b2attr)/2
        self.heightattr=height
        self.areaattr=(1/2)*(self.b1attr+self.b2attr)*self.heightattr
        self.perimeterattr=perimeter
    def bases(self):
        return (self.b1attr, self.b2attr)
    def height(self):
        return self.heightattr
    def median(self):
        return self.medianattr
    def perimeter(self):
        if self.perimeterattr==None:
            print("ALERT: Perimeter for trapezoid is currently undefined.")
            return None
        return self.perimeterattr
    def area(self):
        return self.areaattr
    def __repr__(self):
        return f'''TRAPEZOID:
Bases: {self.bases()}
Height: {self.height()}
Median: {self.median()}
Perimeter: {self.perimeter()}
Area: {self.area()}
'''

class circle(object):
    def __init__(self, radius):
        self.radiusattr = radius
        self.diameterattr = 2*self.radiusattr
        self.perimeterattr = pi*self.diameterattr
        self.areaattr = pi*(self.radiusattr**2)
    def radius(self):
        return self.radiusattr
    def diameter(self):
        return self.diameterattr
    def perimeter(self):
        return self.perimeterattr
    def circumference(self):
        return self.perimeterattr
    def area(self):
        return self.areaattr
    def __repr__(self):
        return f'''CIRCLE:
Radius: {self.radius()}
Diameter: {self.diameter()}
Circumference/Perimeter: {self.perimeter()}
Area: {self.area()}
'''

class prism(object):
    '''
    This code is only applicable in its present form for right prisms.
    '''
    def __init__(self, base, height):
        self.baseattr=base
        self.heightattr=height
        try:
            self.lateralareaattr=self.baseattr.perimeter()*self.heightattr
            self.totalareaattr=self.lateralareaattr+(2*self.baseattr.area())
        except AttributeError:
            pass #self.lateralarea/totalarea calls will now raise an error b/c undefined
        self.volumeattr=self.baseattr.area()*self.heightattr
    def base(self):
        return self.baseattr
    def height(self):
        return self.heightattr
    def lateralarea(self):
        return self.lateralareaattr
    def totalarea(self):
        return self.totalareaattr
    def surfacearea(self):
        return self.totalareaattr
    def volume(self):
        return self.volumeattr
    def __repr__(self):
        return f'''RIGHT PRISM:
Base:
{indent(self.base().__repr__())}  END BASE
Height: {self.height()}
Lateral Area: {self.lateralarea()}
Total Area/Surface Area: {self.totalarea()}
Volume: {self.volume()}
'''
    
class cylinder(prism):
    def __init__(self, base, height):
        prism.__init__(base, height)
    def __repr__(self):
        return f'''CYLINDER:
Base:
{indent(self.base().__repr__())}  END BASE
Height: {self.height()}
Lateral Area: {self.lateralarea()}
Total Area/Surface Area: {self.totalarea()}
Volume: {self.volume()}
'''

#need slantheight to altitude calculator
class pyramid(object):
    def __init__(self, base, altitude):
        self.baseattr=base
        self.altitudeattr=altitude
        if isinstance(self.baseattr, regularpolygon):
            self.slantheightattr=sqrt((self.baseattr.apothem()**2)+(self.altitudeattr**2))
            self.lateralareaattr=(1/2)*self.baseattr.perimeter()*self.slantheightattr
            self.totalareaattr=self.lateralareaattr+self.baseattr.area()
        elif isinstance(self.baseattr, rectangle):
            l = sqrt((self.baseattr.length()**2)+(self.altitudeattr**2))
            w = sqrt((self.baseattr.width()**2)+(self.altitudeattr**2))
            self.slantheightattr = [l, w, l, w]
            self.lateralareaattr=(self.baseattr.width()*l)+(self.baseattr.length()*w)
            self.totalareaattr=self.lateralareaattr+self.baseattr.area()
        elif isinstance(self.baseattr, circle):
            self.slantheightattr = sqrt((self.baseattr.radius()**2)+(self.altitudeattr**2))
            self.lateralareaattr = pi*self.baseattr.radius()*self.slantheightattr
        else:
            pass #Why on Earth do you have a trapezoidal base, dude?
        self.volumeattr=self.baseattr.area()*self.altitudeattr/3
    def base(self):
        return self.baseattr
    def altitude(self):
        return self.altitudeattr
    def slantheight(self):
        return self.slantheightattr
    def lateralarea(self):
        return self.lateralareaattr
    def totalarea(self):
        return self.totalareaattr
    def surfacearea(self):
        return self.totalareaattr
    def volume(self):
        return self.volumeattr
    def __repr__(self):
        return f'''PYRAMID:
Base:
{indent(self.base().__repr__())}  END BASE
Height (Altitude): {self.altitude()}
Slant Height: {self.slantheight()}
Lateral Area: {self.lateralarea()}
Total Area/Surface Area: {self.totalarea()}
Volume: {self.volume()}
'''

class cone(pyramid):
    def __init__(self, base, altitude):
        pyramid.__init__(base, altitude)
    def __repr__(self):
        return f'''CONE:
Base:
{indent(self.base().__repr__())}  END BASE
Height (Altitude): {self.altitude()}
Slant Height: {self.slantheight()}
Lateral Area: {self.lateralarea()}
Total Area/Surface Area: {self.totalarea()}
Volume: {self.volume()}
'''

validshape=False
while not validshape:
    shape = input("shape: input 'square', 'pentagon', 'hexagon', 'regularpolygon', 'rectangle', " \
    "'trapezoid','circle', 'prism', 'cylinder', 'pyramid', 'cone':")
    if shape in ['square', 'pentagon', 'hexagon', 'regularpolygon', 'rectangle', 
                 'trapezoid','circle', 'prism', 'cylinder', 'pyramid', 'cone']:
        validshape=True
if shape == 'regularpolygon':
    sides = input('Sides:')
    sidelength = input('Sidelength:')
    print(regularpolygon(float(sides), float(sidelength)))
elif shape == 'square':
    sidelength = input('Sidelength:')
    print(square(float(sidelength)))
elif shape == 'pentagon':
    sidelength = input('Sidelength:')
    print(pentagon(float(sidelength)))
elif shape == 'hexagon':
    sidelength = input('Sidelength:')
    print(hexagon(float(sidelength)))
elif shape == 'rectangle':
    length = input('Length:')
    width = input('Width:')
    print(regularpolygon(float(length), float(width)))
elif shape == 'trapezoid':
    b1 = input('Base 1:')
    b2 = input('Base 2:')
    height = input('Height:')
    perimeter = input("Perimeter if provided, else type '0':")
    if perimeter == '0':
        perimeter = None
    else:
        perimeter = float(perimeter)
    print(trapezoid(float(b1), float(b2), float(height), perimeter))
elif shape == 'circle':
    radius = input('Radius:')
    print(circle(float(radius)))
elif shape in ['prism', 'cylinder', 'pyramid', 'cone']:
    validbase=False
    while not validbase:
        base = input("base: input 'square', 'pentagon', 'hexagon', 'regularpolygon'," \
        " 'rectangle', 'trapezoid', 'circle':")
        if base in ['square', 'pentagon', 'hexagon', 'regularpolygon', 'rectangle', 'trapezoid','circle']:
            validbase=True
    if base == 'regularpolygon':
        sides = input('Sides:')
        sidelength = input('Sidelength:')
        b=regularpolygon(float(sides), float(sidelength))
    elif base == 'square':
        sidelength = input('Sidelength:')
        b=square(float(sidelength))
    elif base == 'pentagon':
        sidelength = input('Sidelength:')
        b=pentagon(float(sidelength))
    elif base == 'hexagon':
        sidelength = input('Sidelength:')
        b=hexagon(float(sidelength))
    elif base == 'rectangle':
        length = input('Length:')
        width = input('Width:')
        b=regularpolygon(float(length), float(width))
    elif base == 'trapezoid':
        b1 = input('Base 1:')
        b2 = input('Base 2:')
        height = input('Height:')
        perimeter = input("Perimeter if provided, else type '0':")
        if perimeter == '0':
            perimeter = None
        else:
            perimeter = float(perimeter)
        b=trapezoid(float(b1), float(b2), float(height), perimeter)
    elif base == 'circle':
        radius = input('Radius:')
        b=circle(float(radius))
    if shape == 'prism':
        height = input('Height:')
        print(prism(b, float(height)))
    elif shape == 'cylinder':
        height = input('Height:')
        print(cylinder(b, float(height)))
    elif shape == 'pyramid':
        height = input('Height (Altitude):')
        print(pyramid(b, float(height)))
    elif shape == 'cone':
        height = input('Height (Altitude):')
        print(cone(b, float(height)))

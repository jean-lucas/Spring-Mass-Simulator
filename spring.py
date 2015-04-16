from graphics import *
import math,time


''' Simulation of a mass hanging on a vertical spring '''

class Block():
    ''' object block is given 5 values, a mass, the springs constant K,
        the inital force applied to make it oscillate, gravity it experiences,
        and damping force.'''
    
    def __init__(self,mass,k,force,gravity,damp):
        self.mass = float(mass)
        self.k = float(k)
        self.gravity = float(gravity)
        self.damp = float(damp)
        self.force = float(force)
        
        self.initPos = (self.mass*self.gravity)/self.k          # Hooke's Law F = k*x
        self.amp = ((self.mass*self.gravity) + self.force) / self.k  # calculating max amplitude
        self.omega = math.sqrt(self.k/self.mass)                # speed of mass

    def getMass(self):
        return self.mass
    def getForce(self):
        return self.force
    def getK(self):
        return self.k
    def getGravity(self):
        return self.gravity
    def getDamp(self):
        return self.damp

    def update(self,t):
        ''' Calculating the new postion of the block at a certain time,t,
            using oscillation equation and damping'''
        
        pos = self.initPos + self.amp*(math.cos(self.omega*t))*math.exp(-self.damp*t)
        self.initPos = pos                                      #setting the inital postion to current position
        return pos


def main():

    b = Block(3.0,2.0,10.0,9.8,0.05)
    win = GraphWin("oscillation",400,400)
    win.setCoords(0,-80,400,400)
    win.setBackground(color_rgb(244,250,159))

    windowGraphics(win)
    simulation(b,win)
    
def windowGraphics(win):
    '''Drawing all the shapes/items onto the screen via graphics module'''
    
    #base
    base = Rectangle(Point(90,250),Point(320,270))
    base.setFill(color_rgb(81,94,98))
    base.setWidth(2)
    base.setOutline(color_rgb(52,61,64))
    base.draw(win)

    #Texts
    massText = TextFun(26,380,"Mass: ",8,"black",'italic',win)
    gravityText = TextFun(28,360,"Gravity: ",8,"black",'italic',win)
    springKText = TextFun(31,340,"Spring K: ",8,"black",'italic',win)
    forceText= TextFun(43,320,"Force Applied: ",8,"black",'italic',win)
    dampedText= TextFun(39,300,"Damp Value: ",8,"black",'italic',win)

    #Apply Button
    button = Rectangle(Point(200,350),Point(270,380))
    button.setFill(color_rgb(165,203,122))
    button.setOutline(color_rgb(116,137,95))
    button.setWidth(2)
    button.draw(win)
    point = button.getCenter()
    applyT = TextFun(point.getX(),point.getY(),'APPLY',10,'black','bold',win)


    #Simulate Button
    button = Rectangle(Point(200,310),Point(270,340))
    button.setFill(color_rgb(165,203,122))
    button.setOutline(color_rgb(116,137,95))
    button.setWidth(2)
    button.draw(win)
    point = button.getCenter()
    simT = TextFun(point.getX(),point.getY(),'RESET',8,'black','bold',win)    

def simulation(b,win):
    '''Apply a simulation based on entry from user'''

    #graph plotter
    plot = GraphWin("plot", 300,300)
    plot.setCoords(0,-300,300,300)

    
    #entry information
    mass = b.getMass()
    springK = b.getK()
    force = b.getForce()
    gravity = b.getGravity()
    damp = b.getDamp()

    massE = Entry(Point(100,380),7)
    massE.setText(mass)
    EntryFun(massE,8,'white',win)

    springE = Entry(Point(100,340),7)
    springE.setText(springK)
    EntryFun(springE,8,'white',win)
    
    gravityE = Entry(Point(100,360),7)
    gravityE.setText(gravity)  
    EntryFun(gravityE,8,'white',win)

    forceE = Entry(Point(100,320),7)
    forceE.setText(force)
    EntryFun(forceE,8,'white',win)

    dampE = Entry(Point(100,300),7)
    dampE.setText(damp)
    EntryFun(dampE,8,'white',win)

    click = win.getMouse()
    x = click.getX()
    y = click.getY()


    #apply button
    if 200<x<270 and 350<y<380:
        b = Block(massE.getText(),springE.getText(),forceE.getText(),gravityE.getText(),dampE.getText())



    done = False
    t = 0
    while not done:


        xaxis = Line(Point(10,0),Point(260,0)).draw(plot)
        yaxis = Line(Point(30,-290),Point(30,290)).draw(plot)

        t+=0.5
        y = int(b.update(t))  #postion of block at a given time

        reset= win.checkMouse()
        if reset!=None:
            x1=reset.getX()
            y1 = reset.getY()
            if 200<x1<270 and 310<y1<340:
                done=True
        
        block = Rectangle(Point(170,y),Point(200, y+30))
        block.setFill("red")
        block.setOutline("black")
        block.draw(win)

        line = Line(Point(185,250),Point(185,y+30))
        line.draw(win)
        
        time.sleep(0.1)
        block.undraw()
        line.undraw()

        plotz(plot,y,t)
    plot.close()
    simulation(b,win)

        

'''These methods below just simplify the code above'''    
    
def EntryFun(e,size,color,win):
    e.setSize(size)
    e.setFill(color)
    e.draw(win)
    
def TextFun(x,y,string,size,color,style,win):
    ''' quick and efficent way to draw text on screen'''

    t = Text(Point(x,y),string)
    t.setSize(size)
    t.setFill(str(color))
    t.setStyle(str(style))
    t.draw(win)

def plotz(plot,y,t):

    point = Point(t*2+30,y).draw(plot)

    

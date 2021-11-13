from graphics import *
from time import sleep

win = GraphWin('Picobot',600,660)
CoPage =  [[ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 ],
	   [ 1,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,1 ],
	   [ 1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1 ],
	   [ 1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1 ],
	   [ 1,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1 ],
	   [ 1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,1 ],
	   [ 1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1 ],
	   [ 1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1 ],
	   [ 1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,1,1,1 ],
	   [ 1,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1 ],
	   [ 1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1 ],
	   [ 1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,1,1,0,1 ],
	   [ 1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,1 ],
	   [ 1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,1,0,1,1,1,0,1,0,1 ],
	   [ 1,0,1,1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,0,0,1,0,1,0,1 ],
	   [ 1,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,1,0,1,0,1,0,1 ],
	   [ 1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1 ],
	   [ 1,0,0,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1 ],
	   [ 1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,1 ],
	   [ 1,0,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1 ],
	   [ 1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1 ],
	   [ 1,0,1,0,0,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1 ],
	   [ 1,0,1,1,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,1 ],
	   [ 1,0,0,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,1,1 ],
	   [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 ]]

def saveRules(inFileName):
    ' a = state and b = surroundings and c = direction and d = new state '
    inFile = open(inFileName,'r')
    DicOfRules = {}
    n = 1
    for line in inFile:
        xs = line.split()
        a = xs[0]
        b = xs[1]
        c = xs[3]
        d = xs[4]
        DicOfRules[n] = a,b,c,d
        n += 1
    return DicOfRules
    inFile.close()
	
def makemove(rule):
	
    fstate = 0
    x = 5
    y = 1
    CoOfBot = (x,y)
    drawSquare(x, y, 'green')
    def check_1(t):
        dic = {'N' : 1,'E' : 1,'W' : 1,'S' : 1,'x' :0, 'X' : 0}
        if int(t[0]) == fstate: 
            if t[1][0] == '*' or dic[t[1][0]] == CoPage[x][y+1]:
                if t[1][1] == '*' or dic[t[1][1]] == CoPage[x+1][y]:
                    if t[1][2] == '*' or dic[t[1][2]] == CoPage[x-1][y]:
                        if t[1][3] == '*' or dic[t[1][3]] == CoPage[x][y-1]:
                            return True
                        return False
                    return False
                return False
            return False
        return False
    drule = rule.keys()
    e = 1
    lst = []
    while e in drule:
        if check_1(rule[e]):
            nx, ny = x, y
            if rule[e][2] == 'N':
                ny = y+1
            if rule[e][2] == 'E':
                nx = x+1
            if rule[e][2] == 'W':
                nx = x-1
            if rule[e][2] == 'S':
                ny = y-1
            fstate = int(rule[e][3])
            if (x,y) not in lst:
                lst.append((x,y))
            
				
            drawSquare(x, y, 'gray')
            drawSquare(nx, ny, 'green')
			
            sleep(0.04)

            x, y = nx, ny
        e += 1
        if e > len(drule):
            e = 1
        if len(lst) >= 279:
            break
            
    return CoOfBot
	
def drawSquare(x, y, color):
	p1 = Point(y * 24, (x + 1) * 24)
	p2 = Point((y + 1) * 24, x * 24)
	q = Rectangle(p1, p2)
	q.setOutline(color)
	q.setFill(color)
	q.draw(win)

def draw():	
    for i in range(25):
        for j in range (25):
            if CoPage[j][i] == 1:
                p1 = Point(i * 24,(j + 1) * 24)
                p2 = Point((i + 1) * 24,j * 24)
                q = Rectangle(p1,p2)
                q.setOutline('blue')
                q.setFill('blue')
                q.draw(win)
		
def drawStart():
    square = Rectangle(Point(250,620),Point(350,640))
    square.setFill('light blue')
    square.setOutline('light blue')
    message = Text(Point(300,630),'START')
    message.setTextColor('black')
    square.draw(win)
    message.draw(win)
    
def check(x,y):
    if x <= 350 and x >= 250:
        if y >= 620 and y <= 640:
            return True
        return False
    return False
    	
dic = saveRules('rules.txt')
draw()
drawStart()
drawSquare(5, 1, 'green')
Picobot = Text(Point(475,630),'" Picobot "')
Picobot.setTextColor('orange')
Picobot.setStyle('italic')
Picobot.setSize(15)
Picobot.draw(win)

message = Text(Point(125,630),'Click on START')
message.setTextColor('orange')
message.setStyle('italic')
message.setSize(15)
message.draw(win)

p1 = win.getMouse()
if check(p1.getX(),p1.getY()):
    makemove(dic)
message.setText('Click anywhere to quit')
win.getMouse()
win.close()
    
        
            
            
    
    

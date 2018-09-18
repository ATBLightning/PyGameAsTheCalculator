#6001012630047
#Tummanoon Kitcharas-anan
#For more information ==> http://myblogmysoftware.blogspot.com/

import pygame

pygame.init()
#scene adjust
width = 385
height = 525

#colors in RGB
black = (0,0,0)
white = (255,255,255)

blue = (120,120,255)

LB = (180,180,255) #Light blue

VLB = (210,210,255) #Very light blue
D_VLB = (210,210,230)  #When click very light blue button

VVLB = (240,240,255) #Very very light blue
D_VVLB = (226,219,226) #When click very very light blue button

#ButtonShape (1:rectangle, 2:ellipse, 3:circle)
BCP = 1

#str for display
EQ = ''

#-------------------------------------------- 


Display = pygame.display.set_mode((width,height))
pygame.display.set_caption('Calculator')     #Display caption
clock = pygame.time.Clock()

#--------------------------------------------
#Text in the Button
def text_objects(text,font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message(text,xpos,ypos):                
    smtext = pygame.font.Font('freesansbold.ttf',24)
    textsurf, textrect = text_objects(text, smtext)
    textrect.center = ((xpos+(90/2)),(ypos+(60/2)))
    Display.blit(textsurf, textrect)
#--------------------------------------------
#Text in the Display
def text_objects2(text,font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message2(text,xpos,ypos):
    smtext = pygame.font.Font('freesansbold.ttf',32)
    textsurf, textrect = text_objects2(text, smtext)
    textrect = (xpos,ypos)
    Display.blit(textsurf, textrect)
#--------------------------------------------      
    
class button():
    def __init__(self,nameButton,ButColor,xPos,yPos,shapeOfButton): 
        self.nameButton = nameButton
        self.ButColor = ButColor
        self.xPos = xPos
        self.yPos = yPos
        self.shapeOfButton = shapeOfButton
    
    def ShapeColorPos(self):
        if self.shapeOfButton == 1:
            return self.rect()
        elif self.shapeOfButton == 2:
            return self.ellipse()
        elif self.shapeOfButton == 3:
            return self.circle()
        
    def rect(self): #fuction for rectangle
        global mouse,EQ,IO
        if self.xPos+90 > mouse[0] > self.xPos and self.yPos+60 > mouse[1] > self.yPos:
            if event.type == pygame.MOUSEBUTTONDOWN:
                IO = 0
                return pygame.draw.rect(Display, white, (self.xPos+2,self.yPos+2,86,56)),message(self.nameButton,self.xPos,self.yPos)
            elif event.type == pygame.MOUSEBUTTONUP:
                while IO <1:
                    if self.nameButton == 'C':
                        EQ = ''
                        IO += 1  
                    elif self.nameButton == '<<':
                        EQ = EQ[:-1]
                        IO += 1
                    elif self.nameButton == '=':
                        if len(EQ) == 0:
                            IO += 1
                        elif len(EQ) != 0:
                            answer = str(eval(EQ))
                            EQ = answer
                            IO += 1
                    elif self.nameButton == '+' or self.nameButton == '*' or self.nameButton == '/':
                        if len(EQ) == 0:
                            IO += 1
                        else:
                            EQ += self.nameButton 
                            IO += 1
                    else:
                        EQ += self.nameButton
                        IO += 1
            else:
                return pygame.draw.rect(Display, D_VLB, (self.xPos,self.yPos,90,60)),message(self.nameButton,self.xPos,self.yPos)
        else:
            return pygame.draw.rect(Display, self.ButColor, (self.xPos,self.yPos,90,60)),message(self.nameButton,self.xPos,self.yPos)
        
    
    def ellipse(self): #fuction for ellipse
        global mouse,EQ,IO
        if self.xPos+90 > mouse[0] > self.xPos and self.yPos+60 > mouse[1] > self.yPos:
            if event.type == pygame.MOUSEBUTTONDOWN:
                IO = 0
                return pygame.draw.ellipse(Display, white, (self.xPos+2,self.yPos+2,86,56)),message(self.nameButton,self.xPos,self.yPos)
            elif event.type == pygame.MOUSEBUTTONUP:
                while IO <1:
                    if self.nameButton == 'C':
                        EQ = ''
                        IO += 1  
                    elif self.nameButton == '<<':
                        EQ = EQ[:-1]
                        IO += 1
                    elif self.nameButton == '=':
                        if len(EQ) == 0:
                            IO += 1
                        elif len(EQ) != 0:
                            answer = str(eval(EQ))
                            EQ = answer
                            IO += 1
                    elif self.nameButton == '+' or self.nameButton == '*' or self.nameButton == '/':
                        if len(EQ) == 0:
                            IO += 1
                        else:
                            EQ += self.nameButton 
                            IO += 1
                    else:
                        EQ += self.nameButton
                        IO += 1
            else:
                return pygame.draw.ellipse(Display, D_VLB, (self.xPos,self.yPos,90,60)),message(self.nameButton,self.xPos,self.yPos)
        else:
            return pygame.draw.ellipse(Display, self.ButColor, (self.xPos,self.yPos,90,60)),message(self.nameButton,self.xPos,self.yPos)
    
    def circle(self): #fuction for circle
        global mouse,EQ,IO
        if self.xPos+90 > mouse[0] > self.xPos and self.yPos+60 > mouse[1] > self.yPos:
            if event.type == pygame.MOUSEBUTTONDOWN:
                IO = 0
                return pygame.draw.circle(Display, white, (self.xPos+45,self.yPos+30),30),message(self.nameButton,self.xPos,self.yPos)
            elif event.type == pygame.MOUSEBUTTONUP:
                while IO <1:
                    if self.nameButton == 'C':
                        EQ = ''
                        IO += 1  
                    elif self.nameButton == '<<':
                        EQ = EQ[:-1]
                        IO += 1
                    elif self.nameButton == '=':
                        if len(EQ) == 0:
                            IO += 1
                        elif len(EQ) >= 1:
                            answer = str(eval(EQ))
                            EQ = answer
                            IO += 1
                    elif self.nameButton == '+' or self.nameButton == '*' or self.nameButton == '/':
                        if len(EQ) == 0:
                            IO += 1
                        else:
                            EQ += self.nameButton 
                            IO += 1
                    else:
                        EQ += self.nameButton
                        IO += 1
            else:
                return pygame.draw.circle(Display, D_VLB, (self.xPos+45,self.yPos+30),32),message(self.nameButton,self.xPos,self.yPos)
        
        else:
            return pygame.draw.circle(Display, self.ButColor, (self.xPos+45,self.yPos+30),32),message(self.nameButton,self.xPos,self.yPos)

                        
#--------------------------------------------
def loop1():
    calExit = False

    while not calExit:
        global mouse,event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                calExit = True
                
        Display.fill(LB)        
        
        mouse = pygame.mouse.get_pos()
#--------------------------------------------
#Button in first row
        B1 = button('(',VLB,5,200,BCP)
        B1.ShapeColorPos()
        
        B2 = button(')',VLB,100,200,BCP)
        B2.ShapeColorPos()
        
        B3 = button('C',VLB,195,200,BCP)
        B3.ShapeColorPos()
        
        B4 = button('<<',VLB,290,200,BCP)
        B4.ShapeColorPos()
#--------------------------------------------
#Button in second row
        B5 = button('7',VVLB,5,265,BCP)
        B5.ShapeColorPos()
        
        B6 = button('8',VVLB,100,265,BCP)
        B6.ShapeColorPos()
        
        B7 = button('9',VVLB,195,265,BCP)
        B7.ShapeColorPos()
        
        B8 = button('/',VLB,290,265,BCP)
        B8.ShapeColorPos()
#--------------------------------------------
#Button in third row
        B9 = button('4',VVLB,5,330,BCP)
        B9.ShapeColorPos()
        
        B10 = button('5',VVLB,100,330,BCP)
        B10.ShapeColorPos()
        
        B11 = button('6',VVLB,195,330,BCP)
        B11.ShapeColorPos()
        
        B12 = button('*',VLB,290,330,BCP)
        B12.ShapeColorPos()
#--------------------------------------------
#Button in fouth row
        B13 = button('1',VVLB,5,395,BCP)
        B13.ShapeColorPos()
        
        B14 = button('2',VVLB,100,395,BCP)
        B14.ShapeColorPos()
        
        B15 = button('3',VVLB,195,395,BCP)
        B15.ShapeColorPos()
        
        B16 = button('-',VLB,290,395,BCP)
        B16.ShapeColorPos()
#--------------------------------------------
#Button in fifth row
        B17 = button('.',VLB,5,460,BCP)
        B17.ShapeColorPos()
        
        B18 = button('0',VVLB,100,460,BCP)
        B18.ShapeColorPos()
        
        B19 = button('=',VLB,195,460,BCP)
        B19.ShapeColorPos()
        
        B20 = button('+',VLB,290,460,BCP)
        B20.ShapeColorPos()
#--------------------------------------------
        message2(EQ,25,25)   #for the number display 
                
        pygame.display.update()
        clock.tick(30)
        
loop1()

pygame.quit()
quit()
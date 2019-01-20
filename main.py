import pygame, sys
import random


class Runner():
    __customes=('turtle', 'fish', 'prawn', 'moray', 'octopus')
    
    def __init__(self,x=0,y=0):
        ixCostume = random.randint(0,4)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCostume]))
        self.position = [x, y]
        self.name = ''
        
    def avanzar(self):
        self.position[0]+= random.randint(1,6) #self.__position[0] es el valor de l primer elemento x

class Game():
    runners=[]
    __posY = (160,200,240,280)
    __names=("Speedy", "Lucera", "Alonso", "Torcuata")
    __startline=-15
    __finishline=620
    
    def __init__(self):
        self.__screen= pygame.display.set_mode((640,480))
        
        self.__background=pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range(4):
            
        #cota de salida
            theRunner= Runner(self.__startline,self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
        #equivalente a las dos lineas
        #self.runners.append(Runner(self.__startline, self.__posY[i]))
        
    def close(self):
        pygame.quit()
        sys.exit()
        
    def competir(self):
        #comprobacion de eventos
        gameOver = False
        while not gameOver:
            for  event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver=True
            
            for runner in self.runners:
                runner.avanzar()
                if runner.position[0]>=self.__finishline:
                    print("{} ha ganado".format(runner.name))
                    gameOver=True
                    
            #actualizar la pantalla
            self.__screen.blit(self.__background, (0, 0))
            #coloco el corredor en la cota
             
            
                      #for i in range(4):
                #self.__screen.blit(self.runners[1].custome, (self.runners[1].position))
            #Esto si fueran cuatro, sería equivalente a lo de abajo, pero en vez de i
            #utilizo runner y no tengo que poner array[pos]
            for runner in self.runners:
                self.__screen.blit(runner.custome, (runner.position))#no pongo coordenada y porque ya la incluye position
                
            #refrescar pantalla
            pygame.display.flip()
            
        while True:
    #cerrar programa al darle en la x
            for event in pygame.event.get():
                if event.type==pygame.QUIT():
                    self.close()
        
        
    
    
if __name__=='__main__':
    game=Game()
    pygame.init()
    game.competir()
    
    
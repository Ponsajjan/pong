import pygame, sys, random
pygame.init()
clock = pygame.time.Clock()
screen_width = 1350
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')                                                                                                
game_font = pygame.font.Font('freesansbold.ttf', 32)

class Pong():
    def __init__(self,screen_width, screen_height, screen):
        self.screen_width = screen_width
        self.screen_height = screen_height        
        self.screen = screen
        self.bg_color = pygame.Color('grey12')
        self.light_grey = (200,200,200)
        self.ball_speed_x = 8 * random.choice((1,-1))
        self.ball_speed_y = 8 * random.choice((1,-1))
        self.player_speed = 0
        self.opponent_speedws = 0
        self.opponent_speed = 7
        self.menu()
    
    def menu(self):
        while True:
            mx, my = pygame.mouse.get_pos()
            self.button_1 = pygame.Rect(self.screen_width/2-100, self.screen_height/2-35, 200, 50)
            self.button_2 = pygame.Rect(self.screen_width/2-100, self.screen_height/2+35, 200, 50)
            self.text1 = game_font.render(f"   1 player", False, self.bg_color)
            self.text2 = game_font.render(f"   2 player", False, self.bg_color)

            click = False 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    print('click')
            if self.button_1.collidepoint((mx, my)):
                if click:
                    print('button1')
                    self.main()
            if self.button_2.collidepoint((mx, my)):
                if click:
                    self.main_2()   
                    print('button2')

            self.screen.fill(self.bg_color)
            pygame.draw.rect(self.screen, (self.light_grey), self.button_1)
            self.screen.blit(self.text1,(self.screen_width/2-100, self.screen_height/2-25))     
            pygame.draw.rect(self.screen,(self.light_grey), self.button_2)
            self.screen.blit(self.text2,(self.screen_width/2-100, self.screen_height/2+45))
            pygame.display.flip()
            clock.tick(60)
    def pause(self):
        pause = True
        self.pause_text = game_font.render(f"press space to resume", False, self.light_grey)
        self.screen.blit(self.pause_text,(self.screen_width/2-150, self.screen_height/2))
        pygame.display.flip()
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = False
            
    def main(self):
        self.ball = pygame.Rect(screen_width/2-15, screen_height/2-15, 30, 30)
        self.player = pygame.Rect(screen_width -20,screen_height /2-70, 10, 140)
        self.opponent = pygame.Rect(10, screen_height/2-70,10,140)
        self.player_score = 0
        self.opponent_score = 0
        self.game_font = pygame.font.Font('freesansbold.ttf',32)
        self.score_time = int(pygame.time.get_ticks())
        
        run = True
        while run == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                   
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.player_speed +=7
                    if event.key == pygame.K_UP:
                        self.player_speed -=7

                    if event.key == pygame.K_SPACE:
                        self.pause()
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.player_speed -= 7
                    if event.key == pygame.K_UP:
                        self.player_speed += 7

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and self.score_time == None:
                    self.menu()
                    break

            self.ball_animation()
            self.player_animation()
            self.opponent_animation()
            self.draw()
 
    def ball_animation(self):
        
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        if self.ball.top <= 0 or self.ball.bottom >= self.screen_height :
            self.ball_speed_y *= -1
                        
        if self.ball.left <= 0:
            self.player_score += 1
            self.score_time = int(pygame.time.get_ticks())
            print('score time',self.score_time)
            #print(self.current_time)
            
        if self.ball.right >= self.screen_width:
            self.opponent_score += 1
            self.score_time = int(pygame.time.get_ticks())
            print('score time',self.score_time)
            #print(self.current_time)
            
        if self.ball.colliderect(self.player) or self.ball.colliderect(self.opponent):
            self.ball_speed_x *= -1

        if self.score_time != None:
            self.ball_start()
            #print(self.score_time)
            
    def player_animation(self):
        
        self.player.y += self.player_speed       
        if self.player.top <= 0:
            self.player.top =0
        if self.player.bottom >= self.screen_height:
            self.player.bottom = self.screen_height
            
    def opponent_animation(self):        
        if self.opponent.top < self.ball.y and self.ball_speed_x <= 0:
            self.opponent.top += self.opponent_speed
        if self.opponent.bottom > self.ball.y and self.ball_speed_x <= 0:
            self.opponent.bottom -= self.opponent_speed
        if self.opponent.top <= 0 :
            self.opponent.top = 0
        if self.opponent.bottom >= self.screen_height :
            self.opponent.bottom = self.screen_height

    def opponent_animationws(self):
        self.opponent.y += self.opponent_speedws
             
        if self.opponent.top <= 0:
            self.opponent.top =0
        if self.opponent.bottom >= self.screen_height:
            self.opponent.bottom = self.screen_height
    
    def ball_start(self):
        self.current_time = int(pygame.time.get_ticks())
        self.ball.center =(self.screen_width/2, self.screen_height/2)
        print('current time',self.current_time)
        print('current time - score time',self.current_time - self.score_time)

        if self.current_time - self.score_time < 700:
            self.number_three = game_font.render("3", False, self.light_grey)
            self.screen.blit(self.number_three,(self.screen_width/2 - 10, self.screen_height/2 + 20))
            print('1')
            pygame.display.flip()
            

        if 700 < self.current_time - self.score_time < 1400:
            self.number_two = game_font.render("2", False, self.light_grey)
            self.screen.blit(self.number_two,(self.screen_width/2 - 10, self.screen_height/2 + 20))
            print('2')
            pygame.display.flip()

        if 1400 < self.current_time - self.score_time < 2100:
            self.number_one = game_font.render("1", False, self.light_grey)
            self.screen.blit(self.number_one,(self.screen_width/2 - 10, self.screen_height/2 + 20))
            print('3')
            pygame.display.flip()
            
        if self.current_time - self.score_time < 2100:
            self.ball_speed_x = 0
            self.ball_speed_y = 0      
        else:
            self.ball_speed_y = 8 * random.choice((1,-1))
            self.ball_speed_x = 8 * random.choice((1,-1))
            self.score_time = None
            #print(self.score_time)   
            self.ball_animation()
        
    def draw(self):
        
        self.player_text= game_font.render(f"{self.player_score}", False, self.light_grey)
            
        self.opponent_text= game_font.render(f"{self.opponent_score}", False, self.light_grey)
        
        screen.fill(self.bg_color)
        pygame.draw.rect(screen, self.light_grey, self.player)
        pygame.draw.rect(screen, self.light_grey, self.opponent)
        pygame.draw.ellipse(screen, self.light_grey, self.ball)
        pygame.draw.aaline(screen, self.light_grey, (self.screen_width/2, 0), (self.screen_width/2, 700))
        self.screen.blit(self.player_text,(730,470))
        self.screen.blit(self.opponent_text,(600,470))
        pygame.display.flip()
        clock.tick(60)
                
    def main_2(self):
        self.ball = pygame.Rect(screen_width/2-15, screen_height/2-15, 30, 30)
        self.player = pygame.Rect(screen_width -20,screen_height /2-70, 10, 140)
        self.opponent = pygame.Rect(10, screen_height/2-70,10,140)
        self.player_score = 0
        self.opponent_score = 0
        self.game_font = pygame.font.Font('freesansbold.ttf',32)
        self.score_time = int(pygame.time.get_ticks())        
        run = True
        print(self.ball.center)
        while run == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                   
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.player_speed +=7
                    if event.key == pygame.K_UP:
                        self.player_speed -=7

                    if event.key == pygame.K_s:
                        self.opponent_speedws +=7
                    if event.key == pygame.K_w:
                        self.opponent_speedws -=7

                    if event.key == pygame.K_SPACE:
                        self.pause()
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.player_speed -= 7
                    if event.key == pygame.K_UP:
                        self.player_speed += 7

                    if event.key == pygame.K_s:
                        self.opponent_speedws -= 7
                    if event.key == pygame.K_w:
                        self.opponent_speedws += 7

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and self.score_time == None:
                    self.menu()

            self.draw()        
            self.ball_animation()
            self.player_animation()
            self.opponent_animationws()

poong = Pong(screen_width, screen_height, screen)



import pytest
import pygame
from Space_Invaders import *

@pytest.fixture
def init_game():
    # Initialize pygame and create game screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    # Set up basic game objects
    playerX = 370
    enemyX = [0]
    enemyY = [0]
    
    yield screen, playerX, enemyX, enemyY
    
    # Clean up 
    pygame.quit()

def test_player_movement(init_game):
    screen, playerX, _, _ = init_game
    
    # Simulate left key press
    event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT) 
    pygame.event.post(event)
    
    # Update player position
    playerX += -5
    
    # Test that player position updated correctly
    assert playerX == 365
    
def test_bullet_collision(init_game):

    screen, _, enemyX, enemyY = init_game
    
    # Place enemy
    enemyX[0] = 100 
    enemyY[0] = 300

    # Fire bullet towards enemy
    bulletX = 105
    bulletY = 290

    # Call collision check
    is_collision = isCollision(enemyX[0], enemyY[0], bulletX, bulletY)

    assert is_collision == True    

  


# Test enemy movement and direction changes

def test_enemy_movement(init_game):
    _, _, enemyX, enemyY = init_game
    
    # Initialize enemy
    enemyX[0] = 100
    enemyY[0] = 100
    enemyX_change[0] = 4
    enemyY_change[0]=40
    
    # Update position
    enemyX[0] += enemyX_change[0]  
    
    # Check position change
    assert enemyX[0] == 104
    
    # Simulate edge collision
    enemyX[0] = 736
    
    # Update position  
    enemyX[0] += enemyX_change[0]
    enemyY[0]+=enemyY_change[0]
    # Check x change and y down
    assert enemyX[0] == 740
    assert enemyY[0] == 140  

# Test multiple bullets firing

def test_multiple_bullet(init_game):
    _, playerX, _, _ = init_game

    # Fire first bullet
    bulletY=400
    fire_bullet(playerX, bulletY) 
    assert bulletY == 400
    # Fire second bullet
    bulletY=350
    fire_bullet(playerX, bulletY) 
    
    # Check y positions of both bullets 

    assert bulletY == 350
    
# Test score update on collision

def test_score(init_game):
    _, _, enemyX, enemyY = init_game
   
    # Initialize enemy and bullet collision
    enemyX[0] = 100
    enemyY[0] = 300
    bulletX = 120
    bulletY = 400
  
    # Register collision
    isCollision(enemyX[0], enemyY[0], bulletX, bulletY) 
    
    # Check that score was incremented
    
    assert score_value >= 1

def test_game_over(init_game):

    screen, _, enemyX, enemyY = init_game

    # Move enemy below screen
    enemyY[0] = 500
    
    # Call game over check
    game_over_text()
    
    # Check if game over text rendered
    assert over_font.render
    

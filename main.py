import pygame

# Initialize Pygame
pygame.init()

# Set window size and title
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hello World!")

# Define colors
blue = (0, 0, 255)
light_blue = (135, 206, 250)

# Load resources
font = pygame.font.Font('resources/font.ttf', 18)
button_image = pygame.image.load('resources/button.png')

# Set initial values
text_size = 18
text_color = blue
background_color = light_blue

def display_text(text, size, color, x, y):
    font = pygame.font.Font('resources/font.ttf', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def reset_cycle():
    # Reset values for the next cycle
    global text_size, text_color, background_color
    text_size = 18
    text_color = blue
    background_color = light_blue

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                reset_cycle()

    # Update text size, color, and background color
    if text_size < 80:
        text_size += 1
    else:
        text_size = 18

    if text_color == blue:
        text_color = (255, 0, 0)
    else:
        text_color = blue

    if background_color == light_blue:
        background_color = (0, 0, 128)
    else:
        background_color = light_blue

    # Fill the background with a gradient
    pygame.draw.rect(screen, background_color, (0, 0, width, height))
    pygame.draw.rect(screen, light_blue, (0, height // 2, width, height // 2))

    # Display "Hello World" in the center of the screen
    display_text("Hello World!", text_size, text_color, width // 2, height // 2)

    # Display the button on the top right corner of the screen
    screen.blit(button_image, (width - button_image.get_width(), 0))

    # Display "BMC1 copyright 2023" at the bottom of the screen
    display_text("BMC1 copyright 2023", 14, (0, 0, 0), width // 2, height - 14)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    # Initialize variables
    radius = 15
    mode = 'blue'
    points = []
    erasing = False  # Flag to indicate whether erasing mode is active
    drawing_rect = False
    rect_start = None
    rect_end = None
    
    while True:
        pressed = pygame.key.get_pressed()
        
        # Check for key combinations
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # Check for quit event or key presses
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_e:
                    erasing = not erasing
                if event.key == pygame.K_d:
                    drawing_rect = not drawing_rect
                    rect_start = None
                    rect_end = None
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if drawing_rect and event.button == 1:
                    rect_start = event.pos
            if event.type == pygame.MOUSEMOTION:
                if drawing_rect:
                    rect_end = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                if drawing_rect and event.button == 1 and rect_start is not None:
                    rect_end = event.pos
                    drawing_rect = False
                
                # Toggle erasing mode when left-clicking or right-clicking
                if event.button == 1: # left click grows radius
                    if not erasing:
                        radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    if not erasing:
                        radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                if erasing:
                    position = event.pos
                    points = [p for p in points if pygame.math.Vector2(p).distance_to(pygame.math.Vector2(position)) > radius]
                else:
                    # if mouse moved, add point to list
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]
                
        screen.fill((0, 0, 0))

        # Draw rectangle
        if rect_start is not None and rect_end is not None:
            # Draw a rectangle with a semi-transparent cyan color
            pygame.draw.rect(screen, (0, 255, 255), (rect_start, (rect_end[0] - rect_start[0], rect_end[1] - rect_start[1])), 100)
        
        # Draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

# Function to draw a line between two points
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()

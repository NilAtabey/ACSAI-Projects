import images
def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
    img = images.load(start_img)
    comdict = {'E':(1,0),'W':(-1,0),'S':(0,1),'N':(0,-1),'SW':(-1,1),'SE':(1,1),'NW':(-1,-1),'NE':(1,-1)}
    pos = position
    snake = []
    snake.append(pos)
    for com in commands.split():
        pos = [(pos[0] + comdict[com][0]) % len(img[0]), (pos[1] + comdict[com][1]) % len(img)]
        posx, posy = pos
        imgpos = img[posy][posx]
        
        if com in {'NE','NW','SW','SE'} and img[(posy - comdict[com][1]) % len(img)][posx] == (0, 255, 0) and img[posy][(posx - comdict[com][0]) % len(img[0])] == (0, 255, 0):
            break
            
        if imgpos == (255, 128, 0): # orange → food
            snake.append(pos)
            img[posy][posx] = (0, 255, 0)

        elif imgpos == (255, 0, 0) or pos in snake: # red → block or green → hits itself
            break

        else: # black or gray → new space
            snake.append(pos)
            tg1, tg2 = snake.pop(0)
            img[tg2][tg1] = (128, 128, 128)
            img[posy][posx] = (0, 255, 0)

    images.save(img, out_img)
    return len(snake)

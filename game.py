import turtle
import random
import sys


def setup_screen():
    wn = turtle.Screen()
    wn.title("Turtle Food Collection Game with Obstacles")
    wn.bgcolor("lightblue")
    wn.setup(width=600, height=600)
    wn.tracer(0)  
    return wn

def create_player():
    player = turtle.Turtle()
    player.shape("turtle")
    player.color("green")
    player.penup()
    player.speed(2)  
    player.shapesize(stretch_wid=2, stretch_len=2)  
    return player


def create_food(num_food):
    food_items = []
    for _ in range(num_food):
        food = turtle.Turtle()
        food.shape("circle")
        food.color("red")
        food.penup()
        food.speed(0)
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        food_items.append(food)
    return food_items

def create_enemies(num_enemies):
    enemies = []
    for _ in range(num_enemies):
        enemy = turtle.Turtle()
        enemy.shape("turtle")
        enemy.color("black")
        enemy.penup()
        enemy.speed(1)
        enemy.goto(random.randint(-290, 290), random.randint(-290, 290))
        enemies.append(enemy)
    return enemies

def create_obstacles(num_obstacles):
    obstacles = []
    for _ in range(num_obstacles):
        obstacle = turtle.Turtle()
        obstacle.shape("square")
        obstacle.color("gray")
        obstacle.penup()
        obstacle.speed(0)
        obstacle.goto(random.randint(-290, 290), random.randint(-290, 290))
        obstacles.append(obstacle)
    return obstacles


def create_score_display():
    score_display = turtle.Turtle()
    score_display.hideturtle()
    score_display.penup()
    score_display.goto(0, 260)
    score_display.color("black")
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
    return score_display


def restart_game():
    global score
    global food_items
    global enemies
    global obstacles
    global player
    global score_display
    

    score = 0
    

    player.hideturtle()
    for food in food_items:
        food.hideturtle()
    for enemy in enemies:
        enemy.hideturtle()
    for obstacle in obstacles:
        obstacle.hideturtle()
    

    wn.clear()
    wn.setup(width=600, height=600)
    wn.tracer(0)
    
    player = create_player()
    food_items = create_food(5)
    enemies = create_enemies(5)
    obstacles = create_obstacles(5)
    score_display = create_score_display()
    

    score_display.clear()
    score_display.goto(0, 0)
    score_display.write("Game Over! Press 'r' to Restart or 'q' to Quit", align="center", font=("Courier", 24, "normal"))


def end_game():
    player.hideturtle()
    for food in food_items:
        food.hideturtle()
    for enemy in enemies:
        enemy.hideturtle()
    for obstacle in obstacles:
        obstacle.hideturtle()
    score_display.clear()
    score_display.goto(0, 0)
    score_display.write("Game Over! Press 'r' to Restart or 'q' to Quit", align="center", font=("Courier", 24, "normal"))
    wn.onkey(restart_game, "r")
    wn.onkey(sys.exit, "q")
    wn.listen()

def go_up():
    y = player.ycor()
    player.sety(y + 20)

def go_down():
    y = player.ycor()
    player.sety(y - 20)

def go_left():
    x = player.xcor()
    player.setx(x - 20)

def go_right():
    x = player.xcor()
    player.setx(x + 20)


def grow_player():
    global score
    current_wid = player.shapesize()[0]
    current_len = player.shapesize()[1]
    player.shapesize(stretch_wid=current_wid + 0.5, stretch_len=current_len + 0.5)
    score += 10
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))


def setup_controls():
    wn.listen()
    wn.onkey(go_up, "Up")
    wn.onkey(go_down, "Down")
    wn.onkey(go_left, "Left")
    wn.onkey(go_right, "Right")


def main_game_loop():
    while True:
        wn.update()
        
       
        for enemy in enemies:
            if random.randint(1, 100) < 5: 
                x = enemy.xcor() + random.randint(-20, 20)
                y = enemy.ycor() + random.randint(-20, 20)
                enemy.goto(x, y)

    
        for food in food_items:
            if player.distance(food) < 20:
                food.hideturtle()
                food_items.remove(food)
                grow_player()
        
        for enemy in enemies:
            if player.distance(enemy) < 20:
                end_game()


        for obstacle in obstacles:
            if player.distance(obstacle) < 20:
                end_game()
        
       
        if not food_items:
            score_display.clear()
            score_display.goto(0, 0)
            score_display.write("You Win! All Food Collected", align="center", font=("Courier", 36, "normal"))
            turtle.done()
            sys.exit()


wn = setup_screen()
player = create_player()
food_items = create_food(5)
enemies = create_enemies(5)
obstacles = create_obstacles(5)
score_display = create_score_display()


setup_controls()


main_game_loop()

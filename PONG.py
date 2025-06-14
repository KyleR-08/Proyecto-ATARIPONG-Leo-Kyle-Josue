import turtle


ventana = turtle.Screen()
ventana.title("Grupo Leo, Josue y Kyle PONG")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)

inicio = turtle.Turtle()
inicio.speed(0)
inicio.color("white")
inicio.penup()
inicio.hideturtle()
inicio.goto(0, 0)
inicio.write("Presiona ESPACIO para comenzar", align="center", font=("Courier", 24, "normal"))


juego_iniciado = False
def iniciar_juego():
    global juego_iniciado
    juego_iniciado = True
    inicio.clear()

ventana.listen()
ventana.onkeypress(iniciar_juego, "space")


while not juego_iniciado:
    ventana.update()


score_a = 0
score_b = 0


raqueta_a = turtle.Turtle()
raqueta_a.speed(0)
raqueta_a.shape("square")
raqueta_a.color("white")
raqueta_a.shapesize(stretch_wid=5, stretch_len=1)
raqueta_a.penup()
raqueta_a.goto(-350, 0)

raqueta_b = turtle.Turtle()
raqueta_b.speed(0)
raqueta_b.shape("square")
raqueta_b.color("white")
raqueta_b.shapesize(stretch_wid=5, stretch_len=1)
raqueta_b.penup()
raqueta_b.goto(350, 0)

pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 2.0
pelota.dy = 2.0


marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("Jugador A: 0  Jugador B: 0", align="center", font=("Courier", 20, "normal"))


def raqueta_a_arriba():
    if raqueta_a.ycor() < 250:
        raqueta_a.sety(raqueta_a.ycor() + 20)

def raqueta_a_abajo():
    if raqueta_a.ycor() > -250:
        raqueta_a.sety(raqueta_a.ycor() - 20)

def raqueta_b_arriba():
    if raqueta_b.ycor() < 250:
        raqueta_b.sety(raqueta_b.ycor() + 20)

def raqueta_b_abajo():
    if raqueta_b.ycor() > -250:
        raqueta_b.sety(raqueta_b.ycor() - 20)


ventana.listen()
ventana.onkeypress(raqueta_a_arriba, "w")
ventana.onkeypress(raqueta_a_abajo, "s")
ventana.onkeypress(raqueta_b_arriba, "Up")
ventana.onkeypress(raqueta_b_abajo, "Down")


juego_activo = True
while juego_activo:
    ventana.update()


    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

   
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        score_a += 1
        marcador.clear()
        marcador.write(f"Jugador A: {score_a}  Jugador B: {score_b}", align="center", font=("Courier", 20, "normal"))

    
    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        score_b += 1
        marcador.clear()
        marcador.write(f"Jugador A: {score_a}  Jugador B: {score_b}", align="center", font=("Courier", 20, "normal"))

    
    if (340 < pelota.xcor() < 350) and (raqueta_b.ycor() - 50 < pelota.ycor() < raqueta_b.ycor() + 50):
        pelota.setx(340)
        pelota.dx *= -1

    if (-350 < pelota.xcor() < -340) and (raqueta_a.ycor() - 50 < pelota.ycor() < raqueta_a.ycor() + 50):
        pelota.setx(-340)
        pelota.dx *= -1

    
    if score_a == 4 or score_b == 4:
        ganador = "Jugador A" if score_a == 4 else "Jugador B"
        juego_activo = False


ganador_turtle = turtle.Turtle()
ganador_turtle.speed(0)
ganador_turtle.color("yellow")
ganador_turtle.penup()
ganador_turtle.hideturtle()
ganador_turtle.goto(0, 0)
ganador_turtle.write(f"¡{ganador} gana el juego!", align="center", font=("Courier", 28, "bold"))


ventana.mainloop()

import turtle
import winsound
import time

class Ventana():
    def __init__(self):
        winsound.PlaySound("musica", winsound.SND_ASYNC | winsound.SND_LOOP)
        self.puntos1=0
        self.puntos2=0

        self.window=turtle.Screen()
        self.window.setup(height=600, width=1000)
        self.window.bgpic("fondo.png")
        self.window.title("Juego PONG")
        self.window.tracer(0)

        self.division=turtle.Turtle()
        self.division.speed(0)
        self.division.shape("square")
        self.division.pencolor("white")
        self.division.shapesize(30,1)

        self.score = turtle.Turtle()
        self.score.hideturtle()

    def marcador(self, coordenadaX):
        if (coordenadaX > 520):
            self.puntos1+=1
            winsound.Beep(2000, 900)
            self.score.speed(0)
            self.score.pencolor("#F0F005")
            self.score.penup()
            self.score.goto(0.0,0.0)
            self.score.write("Jugardor 1 Anotó! ", align="center", font=("castellar", 40, "bold"))
            self.score.hideturtle()
            time.sleep(2)

        elif (coordenadaX <- 520):
            self.puntos2 += 1
            winsound.Beep(2000, 900)
            self.score.speed(0)
            self.score.pencolor("#DA1A63")
            self.score.penup()
            self.score.goto(0.0, 0.0)
            self.score.write("Jugardor 2 Anotó! ", align="center", font=("castellar", 40, "bold"))
            self.score.hideturtle()
            time.sleep(2)


        self.score.clear()
        self.score.pencolor("black")
        self.score.penup()
        self.score.goto(0.0, 250)
        self.score.write(f"Jugardor 1: {self.puntos1} |     | Jugador 2: {self.puntos2} ", align="center", font=("courier", 30, "bold"))

    def actualizar(self):
        self.window.update()
        self.window.listen()

class Jugador():
    def __init__(self, numero):
        self.player=turtle.Turtle()
        self.player.color("#A03DED")
        self.player.pencolor("white")
        self.player.shape("square")
        self.player.speed(0)
        self.player.penup()
        self.player.shapesize(6,1)
        if(numero==1):
            self.player.goto(-450, 0)
        else:
            self.player.goto(450, 0)

    def subir(self):
        if self.player.ycor() < 230:
            self.player.sety(self.player.ycor()+40)
    def bajar(self):
        if self.player.ycor() > -230:
            self.player.sety(self.player.ycor()-40)
    def getCordenadaY(self):
        return self.player.ycor()


class Pelota():
    def __init__(self):

        self.esfera=turtle.Turtle()
        self.esfera.color("#E8733C")
        self.esfera.pencolor("#3498DB")
        self.esfera.shape("circle")
        self.esfera.speed(0)
        self.esfera.penup()
        self.esfera.shapesize(2)
        self.esfera.dx=1
        self.esfera.dy=1

    def getCoordenadaX(self):
        return self.esfera.xcor()

    def movimiento(self,coordenada1,coordenada2):

        if self.esfera.ycor() > 270:
            self.esfera.dy *= -1
            winsound.Beep(1000, 50)
        if self.esfera.ycor() < -280:
            self.esfera.dy *= -1
            winsound.Beep(1000, 50)

        if (self.esfera.xcor()==415 and self.esfera.ycor()>coordenada2-95 and self.esfera.ycor()<coordenada2+95):
            self.esfera.dx *= -1
            winsound.Beep(1000, 50)

        if (self.esfera.xcor()==-415 and self.esfera.ycor()>coordenada1-95 and self.esfera.ycor()<coordenada1+95):
            self.esfera.dx *= -1
            winsound.Beep(1000, 50)

        if (self.esfera.xcor() > 520):
            self.esfera.dx *= -1
            self.esfera.goto(0, 0)

        if (self.esfera.xcor() < -520):
            self.esfera.dx *= -1
            self.esfera.goto(0, 0)

        self.esfera.setx(self.esfera.xcor() + self.esfera.dx)
        self.esfera.sety(self.esfera.ycor() + self.esfera.dy)





ventana=Ventana()
jugador1=Jugador(1)
jugador2=Jugador(2)
pelota=Pelota()



while True:
    ventana.actualizar()
    ventana.window.onkeypress(jugador1.subir, "w")
    ventana.window.onkeypress(jugador1.bajar, "s")
    ventana.window.onkeypress(jugador2.subir, "Up")
    ventana.window.onkeypress(jugador2.bajar, "Down")
    pelota.movimiento(jugador1.getCordenadaY(), jugador2.getCordenadaY())
    ventana.marcador(pelota.getCoordenadaX())




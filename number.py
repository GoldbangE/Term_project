from turtle import  *
import time
shape()
speed(0)    
pensize(2)
penup()

st()

l=100
    
def rectangle(i) :
    pencolor('black')
    penup()
    goto(-850+i*120,200)
    
    setheading(90)
    pendown()
    rt(180)
    
    fd(50),lt(90) # 1

    fd(100),lt(90) # 2

    fd(50),lt(90) #3
    fd(100),rt(90) #4

    
    
    fd(50),rt(90) #5

    fd(100),rt(90) #6

    fd(50),lt(90) # 7
 
    
ht()
def plus(i):
    pencolor('black')
    penup()
    goto(-800+i*120,250)
    setheading(90)
    pendown()
    rt(180)

    fd(50)
    fd(50),lt(90)
    penup()
    fd(50),lt(90)
    fd(50),lt(90)
    pendown()
    fd(100)
    penup()

def minus(i):
    pencolor('black')
    penup()
    goto(-850+i*120,200)
    setheading(90)
    pendown()
    rt(180)

    penup()
    fd(50),lt(90) # 1

    fd(100),lt(90) # 2
    
    fd(50),lt(90) #3
    pendown()
    fd(100)
    
def multiplication(i):
    pencolor('black')
    penup()
    goto(-850+i*120,250)
    setheading(90)
    pendown()
    rt(180)

    lt(45)
    fd(140)
    penup()
    
    goto(-750+i*120,250)
    setheading(90)
    pendown()
    rt(180)
    rt(45)
    fd(140)
    penup()
    
def division(i):
    pencolor('black')
    penup()
    goto(-750+i*120,250)
    setheading(90)
    pendown()
    rt(180)

    rt(45)
    fd(140)
    penup()

def square(i):
    pencolor('black')
    penup()
    goto(-850+i*120,200)
    setheading(90)
    pendown()
    rt(180)

    lt(135)
    fd(60),rt(90)
    fd(60)
    penup()

def equal(i):
    pencolor('black')
    penup()
    goto(-850+i*120,220)
    setheading(90)
    pendown()
    rt(180)
    
    lt(90)
    fd(100),rt(90)
    penup()
    fd(40),rt(90)
    pendown()
    fd(100)
    penup()

    
def zero(i) :
    pencolor('white')
    penup()
    goto(-850+i*120,200)
    setheading(90)
    pendown()
    rt(180)
    
    penup()
    fd(50),lt(90) # 1

    fd(100),lt(90) # 2
    
    fd(50),lt(90) #3
    pendown()
    fd(100),rt(90) #4

    penup()
    fd(50),rt(90) #5

    fd(100),rt(90) #6

    fd(50),lt(90) # 7
    

def one(i) :
    pencolor('white')
    penup()
    goto(-850+i*120,200)
    setheading(90)
    pendown()
    rt(180)
    
    fd(50),lt(90) # 1

    fd(100),lt(90) # 2
    penup() 
    fd(50),lt(90) #3
    pendown()
    fd(100),rt(90) #4

    fd(50),rt(90) #5

    fd(100),rt(90) #6
    penup()
    fd(50),lt(90) # 7

def two(i) :
    pencolor('white')
    penup()
    goto(-850+i*120,200)
    setheading(90)
    pendown()
    rt(180)
    
    penup()
    fd(50),lt(90) # 1

    fd(100),lt(90) # 2
    pd() 
    fd(50),lt(90) #3
    penup()
    fd(100),rt(90) #4

    pd() 
    fd(50),rt(90) #5
    penup()
    fd(100),rt(90) #6
    penup()
    fd(50),lt(90) # 7

def three(i) :
    pencolor('white')
    penup()
    goto(-850+i*120,200)
    setheading(90)
    pendown()
    rt(180)
    
    fd(50),lt(90) # 1
    penup() 
    fd(100),lt(90) # 2
    fd(50),lt(90) #3
    fd(100),rt(90) #4

    pd() 
    fd(50),rt(90) #5
    penup()
    fd(100),rt(90) #6
    fd(50),lt(90) # 7

def four(i) :
    pencolor('white')
    penup()
    goto(-850+i*120,200)
    setheading(90)
    pendown()
    rt(180)
     
    fd(50),lt(90) # 1
    fd(100),lt(90) # 2
    penup()
    fd(50),lt(90) #3
    fd(100),rt(90) #4
    
    fd(50),rt(90) #5
    pd()
    fd(100),rt(90) #6
    penup()
    fd(50),lt(90) # 7

def five(i) :
    pencolor('white')
    penup()
    goto(-850+i*120,200)
    setheading(90)
    pendown()
    rt(180)
    
    fd(50),lt(90) # 1
    penup()
    fd(100),lt(90) # 2
    fd(50),lt(90) #3
    fd(100),rt(90) #4
    penup() 
    
    fd(50),rt(90) #5
    fd(100),rt(90) #6
    pd()
    fd(50),lt(90) # 7

def six(i) :
    pencolor('white')
    penup()
    goto(-850+i*120,200)
    setheading(90)
    pendown()
    rt(180)
    
    penup()   
    fd(50),lt(90) # 1

    fd(100),lt(90) # 2
    fd(50),lt(90) #3
    fd(100),rt(90) #4
    
    fd(50),rt(90) #5
    fd(100),rt(90) #6
    pd()
    fd(50),lt(90) # 7

def seven(i) :
    pencolor('white')
    penup()
    goto(-850+i*120,200)
    setheading(90)
    pendown()
    rt(180)
    
    fd(50),lt(90) # 1

    fd(100),lt(90) # 2
    penup() 
    fd(50),lt(90) #3
    pendown()
    fd(100),rt(90) #4

    penup()
    fd(50),rt(90) #5

    fd(100),rt(90) #6
    
    fd(50),lt(90) # 7

def eight(i) :
    pencolor('white')
    penup()
    goto(-850+i*120,200)
    setheading(90)
    pendown()
    rt(180)

    penup()
    fd(50),lt(90) # 1

    fd(100),lt(90) # 2
    
    fd(50),lt(90) #3
    
    fd(100),rt(90) #4
    
    fd(50),rt(90) #5

    fd(100),rt(90) #6
    
    fd(50),lt(90) # 7

def nine(i) :
    pencolor('white')
    penup()
    goto(-850+i*120,200)
    setheading(90)
    pendown()
    rt(180)
    
    fd(50),lt(90) # 1
    penup()
    fd(100),lt(90) # 2
     
    fd(50),lt(90) #3
    
    fd(100),rt(90) #4
    
    fd(50),rt(90) #5

    fd(100),rt(90) #6
    
    fd(50),lt(90) # 7


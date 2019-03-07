#!/usr/bin/env python3
import turtle
import json
# for command line args
import sys

def rewrite(axiom, rules, iterations):
    current_gen = str(axiom)
    for i in range(iterations):
        next_gen = "" 
        for char in current_gen:
            if char in rules:
                next_gen += rules[char]
            else:
                next_gen += char
        current_gen = next_gen
    return current_gen

def read_params(filename):
    file = open(filename, "r")
    params = json.loads(file.read())
    file.close()
    return params

def main():
    if len(sys.argv) < 2:
        print("Please enter a filename")
        return

    params = read_params(sys.argv[1])
    rules = {"F": "F+F--F+F"}
    axiom = "F--F--F"
    print(type(params))
    instructions = rewrite(params["axiom"], params["rules"], params["iterations"])

    heading = params["heading"]
    ANGLE = params["angle"]
    UNIT = params["unit"]
    x = params["x"]
    y = params["y"]

    t = turtle.Turtle()
    t.setheading(heading)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.speed(0)

    draw(instructions, t, ANGLE, UNIT)
    t.hideturtle()

def draw(instructions, t, ANGLE, UNIT):

    positions = []
    angles = []
    for i in instructions:
        if i == "F" or i == "G":
            t.forward(UNIT)
        if i == "+":
            t.left(ANGLE)
        if i == "-":
            t.right(ANGLE)
        if i == "[":
            positions.append(t.position())
            angles.append(t.heading())
        if i == "]":
            t.penup()
            t.setposition(positions.pop())
            t.pendown()
            t.setheading(angles.pop())



if __name__=="__main__":
    main()
    input()

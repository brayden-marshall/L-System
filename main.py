#!/usr/bin/env python3

import turtle
import json
import re
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

def draw(instructions, t, ANGLE, UNIT):
    # stacks used for '[' and ']' commands
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
        if i == "|":
            # turning as close to 180 degrees as ANGLE will allow
            for i in range(round(180 / ANGLE)):
                t.right(ANGLE)

def main():
    if len(sys.argv) < 2:
        print("Please enter a filename")
        return

    params = read_params(sys.argv[1])
    instructions = rewrite(params["axiom"], params["rules"], params["iterations"])

    t = turtle.Turtle()
    color_regex = re.compile("#[0-9a-fA-F]{6}")
    if "color" in params and color_regex.match(params["color"]):
        t.color(params["color"])
    t.setheading(params["heading"])
    t.penup()
    t.setposition(params["x"], params["y"])
    t.pendown()
    t.speed(0)

    draw(instructions, t, params["angle"], params["unit"])
    t.hideturtle()


if __name__=="__main__":
    main()
    input()

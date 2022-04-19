#!/usr/bin/env python
import re


def favorite_food():
    print('Admittedly, Emile has a horrendous sweet tooth, so chocolatey, sugary things are definitely his favorite. Either blonde brownies or double chocolate crinkle cookies being the top choice.')


def favorite_hobby():
    print('Well, that might be quite a laundry list... Would you like to know about his more active hobbies or passive ones?')
    res = re.search('(active|passive)', input())
    if res is None:
        print("I'm sorry, I didn't understand the input. Please respond with \"active\" or \"passive\".")
        res = re.search('(.*)', input())
    group = res.group()
    print({'active': 'Emile likes being in the outdoors as much as possible; hiking, climbing, mountain biking, kayaking, skiing, etc.',
           'passive': 'Emile likes reading, learning languages, playing piano, and occasionally gaming with friends.'}.get(group, "I'm sorry, maybe I can help you with something else instead."))


def end():
    print("Thank you for your time!")
    exit()


def check_input(val):
    parsed_val = re.search(
        '(hobbies|food[s]?|show[s]?|peeve[s]?|nothing|^no$)', val)
    if parsed_val is None:
        handle_error()
    else:
        looper({
            'hobby': favorite_hobby,
            'hobbies': favorite_hobby,
            'food': favorite_food,
            'nothing': end,
            'no': end

        }.get(parsed_val.group(), handle_error))


def handle_error():
    print("I'm sorry, I am only a lowly answer bot. I can tell you about Emile's hobbies, favorite foods, favorite shows, and pet peeves. What would you like to know more about?")
    check_input(input())


def introduction():
    print("Hello, my name is Emile! What would you like to know about me?")
    check_input(input())


def looper(val):
    val()
    print("Is there anything else you would like to know?")
    check_input(input())


if __name__ == '__main__':
    introduction()

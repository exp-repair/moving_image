import os
import time

# 计算终端宽度
terminal_width = 30

# 小人的初始位置
position = 0


def print_running_man1(position):
    print(" " * position + "   O")
    print(" " * position + "  /|\\")
    print(" " * position + "  / \\")
    print("孤独的旅人")


def print_running_man2(position):
    print(" " * position + "   O")
    print(" " * position + "  /|\\")
    print(" " * position + "   | ")
    print("孤独的旅人")


def print_running_man_with_another1(position):
    print(" " * position + "   O " + "   O ")
    print(" " * position + "  /|\\" + "  /|\\")
    print(" " * position + "  / \\ " + "  / \\")
    print("抱得美人归")


def print_running_man_with_another2(position):
    print(" " * position + "   O " + "   O ")
    print(" " * position + "  /|\\" + "  /|\\")
    print(" " * position + "   | " + "   | ")
    print("抱得美人归")


def print_running_man_wait_for_you1(position):
    print(" " * position + "   O " + " " * (terminal_width - position) + "   O ")
    print(" " * position + "  /|\\" + " " * (terminal_width - position) + "  /|\\")
    print(" " * position + "  / \\ " + " " * (terminal_width - position) + "   | ")
    print("抱得美人归")


def print_running_man_wait_for_you2(position):
    print(" " * position + "   O " +  " " * (terminal_width - position) + "   O ")
    print(" " * position + "  /|\\" + " " * (terminal_width - position) + "  /|\\")
    print(" " * position + "   | " +  " " * (terminal_width - position) + "   | ")
    print("抱得美人归")


def print_running_play_with_go_cat1(position):
    print(" " * position + "     " +   " " * (terminal_width - position) + "   /\\_/\\    ")
    print(" " * position + "   O " +   " " * (terminal_width - position) + " ( o   o ) ")
    print(" " * position + "  /|\\" +  " " * (terminal_width - position) + "==(     )==")
    print(" " * position + "  / \\ " + " " * (terminal_width - position) + "  `--'--'  ")
    print("捉住一只猫")


def print_running_play_with_go_cat2(position):
    print(" " * position + "     " + " " * (terminal_width - position)  + "   /\\_/\\    ")
    print(" " * position + "   O " + " " * (terminal_width - position)  + " ( o   o ) ")
    print(" " * position + "  /|\\" + " " * (terminal_width - position) + "==(     )==")
    print(" " * position + "   | " + " " * (terminal_width - position)  + "  `--'--'  ")
    print("捉住一只猫")


def print_running_play_with_cat1(position):
    print(" " * position + "     "  + "  /\\_/\\    ")
    print(" " * position + "   O "  + " ( o   o ) ")
    print(" " * position + "  /|\\" + "==(     )==")
    print(" " * position + "  / \\" + "  `--'--'  ")
    print("捉住一只猫")


def print_running_play_with_cat2(position):
    print(" " * position + "     " + "  /\\_/\\    ")
    print(" " * position + "   O " + " ( o   o ) ")
    print(" " * position + "  /|\\" + "==(     )==")
    print(" " * position + "   | " + "   `--'    ")
    print("捉住一只猫")


def clear_screen():
    os.system("clear")


walk_sequence = [print_running_man1, print_running_man2, print_running_man1]

walk_sequence_with_another = [print_running_man_with_another1, print_running_man_with_another2, print_running_man_with_another1]
walk_sequence_wait_for_you = [print_running_man_wait_for_you1, print_running_man_wait_for_you2, print_running_man_wait_for_you1]

catch_a_cat = [print_running_play_with_go_cat1, print_running_play_with_go_cat2, print_running_play_with_go_cat1]
catch_a_cat_back = [print_running_play_with_cat1, print_running_play_with_cat2, print_running_play_with_cat1]



def walkToRight():
    global position
    while position < terminal_width:
        for j in range(3):
            clear_screen()
            walk_sequence[j](position)
            if j == 1:
                position += 1
            time.sleep(0.03)
        time.sleep(0.1)


def walkToLeft():
    global position
    while position > 0:
        for j in range(3):
            clear_screen()
            walk_sequence[j](position)
            if j == 1:
                position -= 1
            time.sleep(0.03)
        time.sleep(0.1)

def walkToRight_with_another():
    global position
    while position < terminal_width:
        for j in range(3):
            clear_screen()
            walk_sequence_with_another[j](position)
            if j == 1:
                position += 1
            time.sleep(0.03)
        time.sleep(0.1)


def walkToLeft_with_another():
    global position
    while position > 0:
        for j in range(3):
            clear_screen()
            walk_sequence_with_another[j](position)
            if j == 1:
                position -= 1
            time.sleep(0.03)
        time.sleep(0.1)


def walkToRight_wait_for_you():
    global position
    while position < terminal_width:
        for j in range(3):
            clear_screen()
            walk_sequence_wait_for_you[j](position)
            if j == 1:
                position += 1
            time.sleep(0.01)
        time.sleep(0.01)


def walkToLeft_wait_for_you():
    global position
    while position > 0:
        for j in range(3):
            clear_screen()
            walk_sequence_wait_for_you[j](position)
            if j == 1:
                position -= 1
            time.sleep(0.03)
        time.sleep(0.1)


def cat_a_cat_for_you():
    global position
    while position < terminal_width:
        for j in range(3):
            clear_screen()
            catch_a_cat[j](position)
            if j == 1:
                position += 1
            time.sleep(0.01)
        time.sleep(0.01)


def cat_a_cat_for_you_back():
    global position
    while position > 0:
        for j in range(3):
            clear_screen()
            catch_a_cat_back[j](position)
            if j == 1:
                position -= 1
            time.sleep(0.03)
        time.sleep(0.1)


while position < terminal_width:
    # walkToRight()
    # walkToLeft()

    cat_a_cat_for_you()
    cat_a_cat_for_you_back()

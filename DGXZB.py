import os
import numpy as np
import random
from PIL import Image, ImageTk # 导入图像处理函数库
import tkinter as tk           # 导入GUI界面函数库
import tkinter.messagebox


# 红绿蓝黄 0000
im1 = None
image_file1 = None
im2 = None
image_file2 = None
im3 = None
image_file3 = None
im4 = None
image_file4 = None


def special_card():
    global cardlist
    global RING
    for i in range(4):
        if not present_surface_card[i]:
            continue
        a = cardlist[present_surface_card[i][0]]
        if a.split("-")[1] == "A":
            RING = "A"
            break
        elif a.split("-")[1] == "B":
            RING = "B"
            break
        elif a.split("-")[1] == "G":
            RING = "G"
            break
        elif a.split("-")[1] == "Y":
            RING = "Y"
            break
        else:
            RING = 0
    # QIANG = True


def lose():
    global player1_hand, player2_hand, player3_hand, player4_hand
    if not player1_hand:
        # print("player1 lose...")
        tk.messagebox.showinfo(title='uhahaha', message="player1 lose...")
    if not player2_hand:
        tk.messagebox.showinfo(title='uhahaha', message="player2 lose...")
    if not player3_hand:
        tk.messagebox.showinfo(title='uhahaha', message="player3 lose...")
    if not player4_hand:
        tk.messagebox.showinfo(title='uhahaha', message="player4 lose...")


def clean_cards():
    global im1, im2, im3, im4, image_file4, image_file3, image_file2, image_file1, QIANG
    im1, im2, im3, im4, image_file4, image_file3, image_file2, image_file1 = None, None, None, None, None, None, None, None
    # im1 = ImageTk.PhotoImage(image_file1)
    canvas.create_image(200, 200, anchor='s', image=im1)
    # im2 = ImageTk.PhotoImage(image_file2)
    canvas.create_image(400, 200, anchor='s', image=im2)
    # im3 = ImageTk.PhotoImage(image_file3)
    canvas.create_image(600, 200, anchor='s', image=im3)
    # im4 = ImageTk.PhotoImage(image_file4)
    canvas.create_image(800, 200, anchor='s', image=im4)
    # QIANG = False


def check_cards():
    global present_sum, TAKE
    # 检查在场牌数
    if 5 in present_sum:
        TAKE = 1  # 可拍铃
    else:
        TAKE = 0
    print(present_sum,present_surface_card,RING,TAKE)

def update_label_remaining():
    global label_remain, player1_hand, player2_hand, player3_hand, player4_hand
    label_remain["text"] = ('剩余手牌：player1：{}，player2：{}，player3：{}，player4：{}'.format(
        len(player1_hand), len(player2_hand), len(player3_hand), len(player4_hand)))


TAKE = 0  # 可以拍铃与否
# QIANG = False  # 桌上没牌不能抢
RING = 0  # 铃响与否
STOCK = []  # 牌库
present_total_card = []  # 场上所有牌
card1 = None  # 1号用户面前的卡牌
card2 = None
card3 = None
card4 = None

cardlist = os.listdir("./img/")
# 打乱
random_card = random.sample(range(0, len(cardlist)), len(cardlist))
# print(random_card)
# print(cardlist)
# print(len(cardlist))
# 分牌
present_sum = np.asarray([0, 0, 0, 0])
present_surface_card = [[], [], [], []]  # 场上4players最顶上的牌
player1_hand = random_card[0:24]
player2_hand = random_card[24:48]
player3_hand = random_card[48:72]
player4_hand = random_card[72:]

# 创建窗口 设定大小并命名
window = tk.Tk()
window.title('德国心脏病')
window.geometry('1280x768')
# var = tk.StringVar()
tempstring = "剩余手牌：player1：{}，player2：{}，player3：{}，player4：{}".format(
    len(player1_hand), len(player2_hand), len(player3_hand), len(player4_hand))
# var.set(tempstring)
label_remain = tk.Label(window, text="", bg='white', font=('Arial', 20),
                        width=300, height=2)
label_remain["text"] = tempstring
label_remain.pack()
canvas = tk.Canvas(window, bg='white', width=1260, height=688)
canvas.pack()


def keyboard(event):
    global image_file1, image_file2, image_file3, image_file4, im1, im2, im3, im4, QIANG
    global TAKE, RING, STOCK, present_total_card, card1, card2, card3, card4, cardlist, random_card
    global present_surface_card, present_sum, present_total_card
    global player1_hand, player2_hand, player3_hand, player4_hand
    if event.char == "1":
        if not player1_hand:
            lose()
        else:
            if card1 is not None:
                present_surface_card[0] = []
                for i in range(4):
                    present_sum[i] = present_sum[i]-int(cardlist[card1].split("-")[0][i])
            card1 = player1_hand.pop()
            present_surface_card[0] = [card1]
            present_total_card = present_total_card+[card1]
            for i in range(4):
                present_sum[i] = present_sum[i]+int(cardlist[card1].split("-")[0][i])
            special_card()
            image_file1 = Image.open('./img/{}'.format(cardlist[card1]))
            im1 = ImageTk.PhotoImage(image_file1)
            canvas.create_image(200, 200, anchor='s', image=im1)

        check_cards()
        update_label_remaining()

    elif event.char == "-":
        if not player2_hand:
            lose()
        else:
            if card2 is not None:
                present_surface_card[1] = []
                for i in range(4):
                    present_sum[i] = present_sum[i]-int(cardlist[card2].split("-")[0][i])

            card2 = player2_hand.pop()
            present_surface_card[1] = [card2]
            present_total_card = present_total_card+[card2]
            for i in range(4):
                present_sum[i] = present_sum[i]+int(cardlist[card2].split("-")[0][i])
            special_card()
            image_file2 = Image.open('./img/{}'.format(cardlist[card2]))
            im2 = ImageTk.PhotoImage(image_file2)
            canvas.create_image(400, 200, anchor='s', image=im2)
        check_cards()
        update_label_remaining()

    elif event.char == "z":
        if not player3_hand:
            lose()
        else:
            if card3 is not None:
                present_surface_card[2] = []
                for i in range(4):
                    present_sum[i] = present_sum[i] - int(cardlist[card3].split("-")[0][i])
            card3 = player3_hand.pop()
            present_surface_card[2] = [card3]
            present_total_card = present_total_card + [card3]
            for i in range(4):
                present_sum[i] = present_sum[i] + int(cardlist[card3].split("-")[0][i])
            special_card()
            image_file3 = Image.open('./img/{}'.format(cardlist[card3]))
            im3 = ImageTk.PhotoImage(image_file3)
            canvas.create_image(600, 200, anchor='s', image=im3)
        check_cards()
        update_label_remaining()

    elif event.char == ".":
        if not player4_hand:
            lose()
        else:
            if card4 is not None:
                present_surface_card[3] = []
                for i in range(4):
                    present_sum[i] = present_sum[i] - int(cardlist[card4].split("-")[0][i])
            card4 = player4_hand.pop()
            present_surface_card[3] = [card4]
            present_total_card = present_total_card + [card4]
            for i in range(4):
                present_sum[i] = present_sum[i] + int(cardlist[card4].split("-")[0][i])
            special_card()
            image_file4 = Image.open('./img/{}'.format(cardlist[card4]))
            im4 = ImageTk.PhotoImage(image_file4)
            canvas.create_image(800, 200, anchor='s', image=im4)
        check_cards()
        update_label_remaining()

    if present_surface_card != [[], [], [], []] or (present_surface_card == [[], [], [], []] and RING == 1):
        if event.char == "2":

            if (TAKE == 1 and RING == 0) or RING == "A" or (RING == "B" and present_sum[2] == 0) or (
                                RING == "Y" and present_sum[3] == 0) or (RING == "G" and present_sum[1] == 0):
                player1_hand = present_total_card + player1_hand
                present_total_card = []
                present_surface_card = [[], [], [], []]
                present_sum = np.asarray([0, 0, 0, 0])
                card1, card2, card3, card4, RING, TAKE = None, None, None, None, 0, 0
                clean_cards()
            elif TAKE == 0:
                if len(player1_hand) > 3:
                    player2_hand.insert(0, player1_hand.pop())
                    player3_hand.insert(0, player1_hand.pop())
                    player4_hand.insert(0, player1_hand.pop())
                else:
                    player1_hand = []
                    lose()
            check_cards()
            update_label_remaining()

        elif event.char == "=":

            if (TAKE == 1 and RING == 0) or RING == "A" or (RING == "B" and present_sum[2] == 0) or (
                                RING == "Y" and present_sum[3] == 0) or (RING == "G" and present_sum[1] == 0):
                player2_hand = present_total_card + player2_hand
                present_total_card = []
                present_surface_card = [[], [], [], []]
                present_sum = np.asarray([0, 0, 0, 0])
                card1, card2, card3, card4, RING, TAKE = None, None, None, None, 0, 0
                clean_cards()
            elif TAKE == 0:
                if len(player2_hand) > 3:
                    player1_hand.insert(0, player2_hand.pop())
                    player3_hand.insert(0, player2_hand.pop())
                    player4_hand.insert(0, player2_hand.pop())
                else:
                    player2_hand = []
                    lose()
            check_cards()
            update_label_remaining()

        elif event.char == "x":

            if (TAKE == 1 and RING == 0) or RING == "A" or (RING == "B" and present_sum[2] == 0) or (
                                RING == "Y" and present_sum[3] == 0) or (RING == "G" and present_sum[1] == 0):
                player3_hand = present_total_card + player3_hand
                present_total_card = []
                present_surface_card = [[], [], [], []]
                present_sum = np.asarray([0, 0, 0, 0])
                card1, card2, card3, card4, RING, TAKE = None, None, None, None, 0, 0
                clean_cards()
            elif TAKE == 0:
                if len(player3_hand) > 3:
                    player1_hand.insert(0, player3_hand.pop())
                    player2_hand.insert(0, player3_hand.pop())
                    player4_hand.insert(0, player3_hand.pop())
                else:
                    player3_hand = []
                    lose()
            check_cards()
            update_label_remaining()

        elif event.char == "/":

            if (TAKE == 1 and RING == 0) or RING == "A" or (RING == "B" and present_sum[2] == 0) or (
                                RING == "Y" and present_sum[3] == 0) or (RING == "G" and present_sum[1] == 0):
                player4_hand = present_total_card + player4_hand
                present_total_card = []
                present_surface_card = [[], [], [], []]
                present_sum = np.asarray([0, 0, 0, 0])
                card1, card2, card3, card4, RING, TAKE = None, None, None, None, 0, 0
                clean_cards()
            elif TAKE == 0:
                if len(player4_hand) > 3:
                    player1_hand.insert(0, player4_hand.pop())
                    player2_hand.insert(0, player4_hand.pop())
                    player3_hand.insert(0, player4_hand.pop())
                else:
                    player4_hand = []
                    lose()
            check_cards()
            update_label_remaining()

    canvas.pack()


frame = tk.Frame(window, width=200, height=200)
frame.bind("<Key>", keyboard)
frame.focus_set()
frame.pack()

window.mainloop()

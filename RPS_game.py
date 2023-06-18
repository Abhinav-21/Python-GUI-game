import tkinter as tk
import tkinter.font as tkf
import random as r

count_system = 0
count_player = 0


def start():

    list_item = ["Rock", "Paper", "Scissors"]

    # algorithm for selecting rock.
    def rock():
        global count_player
        global count_system
        computer_choice = r.choices(list_item)[0]

        if computer_choice == "Rock":
            label_point["text"] = "Draw"

        elif computer_choice == "Paper":
            count_system += 1
            label_point["text"] = "System's Point"

        else:
            count_player += 1
            label_point["text"] = f"{player}'s point"

        label_update[
            "text"
        ] = f'You chose {choice_1["text"]} and system chose {computer_choice}'
        game_lab2["text"] = f"{player}: {count_player}"
        game_lab3["text"] = f"Computer: {count_system}"

        if (count_player > 2) or (count_system > 2):
            choice_1.destroy()
            choice_2.destroy()
            choice_3.destroy()

            gap = tk.Label(game, text="       ")
            gap.grid(column=2, row=2)

            result = tk.Label(game, text="", font=font_)
            result.grid(column=1, row=3, columnspan=3, padx=15)

            if count_player == 3:
                game_lab.destroy()
                result["text"] = "YOU WON CONGRATULATIONS!!!🎉"
                game.geometry("370x200")

            else:
                game_lab.destroy()
                result["text"] = "      YOU LOSE 👎      "
                game.geometry("300x200")

    # algorithm for selecting paper.
    def paper():
        global count_player
        global count_system
        computer_choice = r.choices(list_item)[0]

        if computer_choice == "Paper":
            label_point["text"] = "Draw"

        elif computer_choice == "Rock":
            count_player += 1
            label_point["text"] = f"{player}'s point"

        else:
            count_system += 1
            label_point["text"] = "System's Point"

        label_update[
            "text"
        ] = f'You chose {choice_2["text"]} and system chose {computer_choice}'
        game_lab2["text"] = f"{player}: {count_player}"
        game_lab3["text"] = f"Computer: {count_system}"

        if (count_player > 2) or (count_system > 2):
            choice_1.destroy()
            choice_2.destroy()
            choice_3.destroy()

            gap = tk.Label(game, text="       ")
            gap.grid(column=2, row=2)

            result = tk.Label(game, text="", font=font_)
            result.grid(column=1, row=3, columnspan=3, padx=15)

            if count_player == 3:
                game_lab.destroy()
                result["text"] = "YOU WON CONGRATULATIONS!!!🎉"
                game.geometry("370x200")

            else:
                game_lab.destroy()
                result["text"] = "      YOU LOSE 👎     "
                game.geometry("300x200")

    # algorithm for selecting scissors.
    def scissors():
        global count_player
        global count_system
        computer_choice = r.choices(list_item)[0]

        if computer_choice == "Scissors":
            label_point["text"] = "Draw"

        elif computer_choice == "Rock":
            count_system += 1
            label_point["text"] = "System's Point"

        else:
            count_player += 1
            label_point["text"] = f"{player}'s point"

        label_update[
            "text"
        ] = f'You chose {choice_3["text"]} and system chose {computer_choice}'
        game_lab2["text"] = f"{player}: {count_player}"
        game_lab3["text"] = f"Computer: {count_system}"

        if (count_player > 2) or (count_system > 2):
            choice_1.destroy()
            choice_2.destroy()
            choice_3.destroy()

            gap = tk.Label(game, text="       ")
            gap.grid(column=2, row=2)

            result = tk.Label(game, text="", font=font_)
            result.grid(column=1, row=3, columnspan=3, padx=15)

            if count_player == 3:
                game_lab.destroy()
                result["text"] = "YOU WON CONGRATULATIONS!!!🎉"
                game.geometry("370x200")

            else:
                game_lab.destroy()
                result["text"] = "      YOU LOSE 👎      "
                game.geometry("300x200")

    #   Main Game Window

    player = entry_1.get()
    game = tk.Tk()
    game.title("Game")
    game.geometry("450x250")

    count_player = 0
    count_system = 0

    game_lab = tk.Label(game, text="Select your choice:")
    game_lab.grid(column=1, row=2, padx=15, pady=10)

    font_ = tkf.Font(size=20)

    game_lab2 = tk.Label(game, text=f"{player}: {count_player}", font=font_)
    game_lab2.grid(column=1, row=1, pady=15, padx=10)

    game_lab3 = tk.Label(game, text=f"Computer: {count_system}", font=font_)
    game_lab3.grid(column=3, row=1, pady=15, padx=10)

    choice_1 = tk.Button(game, text="Rock", width=10, command=rock)
    choice_1.grid(column=1, row=3, padx=10, pady=10)

    choice_2 = tk.Button(game, text="Paper", width=10, command=paper)
    choice_2.grid(column=2, row=3, padx=10, pady=10)

    choice_3 = tk.Button(game, text="Scissors", width=10, command=scissors)
    choice_3.grid(column=3, row=3, padx=10, pady=10)

    label_update = tk.Label(game, text="")
    label_update.grid(column=1, row=4, columnspan=3)

    label_point = tk.Label(game, text="")
    label_point.grid(column=1, row=5, columnspan=3)

    tk.mainloop()


# Help Window


def guide():
    main2 = tk.Tk()
    main2.geometry("600x200")
    main2.title("help")
    game_help = tk.Label(
        main2,
        text="""
       ___________________________
         ROCK-PAPER-SCISSORS
      ---------------------------
            In this game you will have five choices, stone, paper or scissors,
            you will choose one of them and your opponent(computer) will also choose one of them.
            The result is decided as follows:
              1. Paper beats rock but is beaten by scissors.
              2. Scissors beats paper but is beaten by rock.
              3. Rock beats scissors but is beaten by paper.
              4. Here we go...!     
            -----X-----X-----X-----X-----X-----
             """,
    )
    game_help.pack()

    tk.mainloop()


# Welcome Window


def welcome():
    player = entry_1.get()
    label_2 = tk.Label(
        frame,
        text=f"""Hello! {player}, Welcome to this game of rock paper and scissors,
        The game will be of 5 round, GOOD LUCK!
            """,
        bg="#6888DF",
    )
    label_2.grid(column=3, row=3, pady=15, columnspan=4)

    button_2 = tk.Button(frame, text="Start", width=10, command=start)
    button_2.grid(column=3, row=5, padx=20, pady=10)

    button_3 = tk.Button(frame, text="Help", command=guide)
    button_3.grid(column=4, row=5, padx=10)


# Entry Window

main = tk.Tk()
main.geometry("550x350")
main.title("Rock Paper and Scissors")

frame = tk.Frame(main, bg="#6888DF", relief="sunken")
frame.place(relwidth=0.85, relheight=0.85, relx=0.08, rely=0.08)

label_1 = tk.Label(frame, text="Enter your name here:", bg="#6888DF")
label_1.grid(column=3, row=1, columnspan=3, pady=15)

entry_1 = tk.Entry(frame, width=30)
entry_1.grid(column=3, row=2, padx=30, pady=10)

button_1 = tk.Button(frame, text="OK", command=welcome)
button_1.grid(column=4, row=2)

tk.mainloop()

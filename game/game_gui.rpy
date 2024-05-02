screen money_info:
    frame:
        padding(10,10)
        xalign 0.99
        yalign 0.02
        background Frame("images/frameback.png", 10, 10, corners=(15, 15), alpha=True)
        hbox:
            xalign 1.0
            yalign 0.0
            text "Гроші: ":
                color "#000000"
            text str(gg_money):
                color "#000000"
define vlad = Character('Влад', color="#800000")
define brain = Character('Думки', color="#67b3c3")
define voice = Character('Голос', color="#db12bd")
define mama_vlada = Character('Мама Влада', color="#ffc0cb")
define street_girl = Character('Дівчина', color="#4bdf70")
define alina = Character('Аліна', color="#4bdf70")
define bodya = Character('Бодя', color="#cfff4bff")
define currator = Character("Куратор", color="#553D67")

define gui.interface_text_color = "#c505a2ff"
define config.mouse ={}
define config.mouse["default"] = [("gui/penis.png", 0,0)]
#Влад--------------------------
define gg_money = 29
define inventory = []

#Влад2-------------------------
define love = 0

#Мама Влада--------------------
default love_mama = 50
define take_mom_money = None


#Аліна-------------------------
default love_alina = 10
define Alina_num = None
define go_to_home_alina = None

#Бодя--------------------------
define check_bodya_in_club = None
define Bodya_num = None
default love_bodya = 0
#Куратор-----------------------
define love_currator = 0

#Nvl-setup---------------------
default maxlove = 100
default minlove = 0
define a_s_nvl = Character("Аліна", kind=nvl, image="nighten", callback=Phone_SendSound)
define a_r_nvl = Character("Аліна", kind=nvl, image="nighten", callback=Phone_ReceiveSound)
define b_s_nvl = Character("Бодя", kind=nvl, image="nighten", callback=Phone_SendSound)
define b_s_nvl = Character("Бодя", kind=nvl, image="nighten", callback=Phone_ReceiveSound)
define v_r_nvl = Character("Влад", kind=nvl, callback=Phone_ReceiveSound)

#Other------------------------
style scream_style:
    color "#aa0000"
    size 40
    font "TurretRoad-Medium.ttf"


image menu_slideshow:
    "gui/main_menu/bg menu.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu2.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu3.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu4.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu5.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu6.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu7.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu8.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu9.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu10.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu11.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu12.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu13.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu14.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu15.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu16.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu17.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu18.png" with dissolve
    pause 5.0
    "gui/main_menu/bg menu19.png" with dissolve
    pause 5.0
    repeat

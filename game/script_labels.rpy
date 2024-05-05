label bus_with_alina:
    voice "{cps=20}Я знову почув своє ім'я{/cps}{cps=10}, але тепер його високим голосом промовила дівчина{/cps}"
    scene bg busstop_day_summer
    show alina happy_uniform with dissolve
    show screen lovemetr_alina
    alina "{cps=20}Влад!{/cps}"
    vlad "О, привіт Аліно"
    alina "Ти теж не встиг на автобус?"
    vlad "Ага{w=0.5}.{w=0.5}.{w=0.5}."
    brain "Ми трішки перекинулися думками та продовжили чекати"
    vlad "{cps=15}Оо{/cps} от і мій автобус, бувай!"
    show alina shocked_uniform
    $ flash = Fade(.25, 0, .75, color="#fff")
    alina "{cps=20}Стій...{/cps}так мені теж на нього" with flash
    vlad "{cps=25}Ти теж в аграрному коледжі на 122 вчишся?"
    alina {cps=25}"Так!!!"
    show alina smile_uniform with dissolve
    vlad "{cps=25}Добре потім обговоримо, швидше сідай"
    $ love_alina += 10
    hide screen lovemetr_alina
    scene black with dissolve
    stop music
    play music "audio/bus_sound.mp3"
    vlad "{cps=25}Який ж все таки гарний Стрий!"
    alina "{cps=25}Особливо вночі!"
    alina "{cps=25}А ти би не хотів сьогодні поїхати до дому разом?"
    brain "{cps=25}Я не очікував цих слів від неї"
    menu:
        "Піти з Аліною":
            $ go_to_home_alina = True
            vlad "{cps=25}Можна, тоді зустрінемось після пар біля входу"

        "Відмовити та піти до Боді" if check_bodya_in_club:
            vlad "{cps=25}Я сьогодні зайнятий, можливо наступним разом"
        
        "Відмовитися" if check_bodya_in_club == False or check_bodya_in_club == None:
            vlad "{cps=25}Сьогодні не зможу, втомився через переїзд"
    
    brain "Автобус під'їхав до коледжу"
    if go_to_home_alina:
        alina "{cps=25}До вечора!"
    else:
        alina "{cps=25}Побачимось!"
    vlad "{cps=25}Бувай"
    return


label bus_without_alina:
    voice "{cps=15}Пройшло близько 15 хвилин і він приїхав"
    vlad "{cps=10}Оо фух{/cps}{cps=25} от і мій автобус"
    stop music
    play music "audio/bus_sound.mp3"
    vlad "{cps=25}Який ж все таки гарний Стрий!"
    brain "{cps=25}Автобус під'їхав до коледжу"
    return

label titles:
    $ renpy.pause(1.0)
    scene black with dissolve
    voice "{explode=1}Кінець гри v[config.version]{/explode}"
    $ renpy.pause(5.0)
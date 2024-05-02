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
    vlad "Ти теж в аграрному коледжі на 122 вчишся?"
    alina "Так!!!"
    show alina smile_uniform with dissolve
    vlad "Добре потім обговоримо, швидше сідай"
    $ love_alina += 10
    hide screen lovemetr_alina
    scene black with dissolve
    stop music
    play music "audio/bus_sound.mp3"
    vlad "Який ж все таки гарний Стрий!"
    alina "Особливо вночі!"
    alina "А ти би не хотів сьогодні поїхати до дому разом?"
    brain "Я не очікував цих слів від неї"
    menu:
        "Піти з Аліною":
            $ go_to_home_alina = True
            vlad "Можна, тоді зустрінемось після пар біля входу"

        "Відмовити та піти до Боді" if check_bodya_in_club:
            vlad "Я сьогодні зайнятий, можливо наступним разом"
        
        "Відмовитися" if check_bodya_in_club == False or check_bodya_in_club == None:
            vlad "Сьогодні не зможу, втомився через переїзд"
    
    brain "Автобус під'їхав до коледжу"
    if go_to_home_alina:
        alina "До вечора!"
    vlad "Бувай"
    return


label bus_without_alina:
    scene bg busstop_day_summer
    vlad "{cps=15}Оо{/cps} от і мій автобус"
    stop music
    play music "audio/bus_sound.mp3"
    vlad "Який ж все таки гарний Стрий!"
    brain "Автобус під'їхав до коледжу"
    return

label titles:
    $ renpy.pause(1.0)
    scene black with dissolve
    voice "{explode=1}Кінець гри v[config.version]{/explode}"
    $ renpy.pause(5.0)
label start :
    play music "audio/mus.mp3" fadein 1.0 volume 0.5
    'Назва візуальної новели: "Лінії Долі"'
    voice "Головний герой, Влад, переїжджає в місто Стрий і вступає в колледж"
    with fade
    show screen money_info
    show bg room_day
    show vlad nuded
    vlad "Охх щось я заморився з цим переїздом, вже не можу дочекатися зустрічі з моїми новими одногрупниками!"
    hide vlad nuded
    show vlad sad
    voice "Щойно промовивши у Влада забурчало в животі"
    vlad "Треба сходити в магазин, мама ще не встигла нічого приготувати"
    hide bg room_day
    hide vlad nuded
    hide vlad sad
    show bg hata_day
    with fade
    brain "Мама замітала на подвір'ї"
    show vlad_mama speak
    show screen lovemetr_mama
    with dissolve
    mama_vlada "Куди ти зібрався так пізно?"
    hide vlad_mama speak
    show vlad sweat_mayka
    vlad "Піду куплю протеїна похавать бо ти нічого не готуєш"
    voice "Промовив злісно Влад та пішов геть"
    hide screen lovemetr_mama
    scene bg street_day
    with fade
    show vlad sweat_mayka
    with dissolve
    brain "Я знову думав про те як завтра побачу одногрупників, {w=1}та раптом..."
    hide vlad sweat_mayka
    with dissolve
    show alina default
    with dissolve
    show screen lovemetr_alina
    street_girl "Привіт, ти ж Влад наче?"
    hide alina default
    show vlad sweat_mayka
    with dissolve
    vlad "Ну так, а ти хто така?"
    hide vlad sweat_mayka
    show alina default
    with dissolve
    street_girl "Я твоя сусідка, живу навпроти тебе"
    menu:
        "Що мені зробити ?"

        "Поговорити з дівчиною та дізнатись про неї більше":
            $ Alina_num = True
            $ inventory.append(Alina_num)
            $ love_alina +=10
            show alina default
            with dissolve
            brain "Дівчина мені дуже сподобалась, врешті-решт я дістав її номер телефону"

        "Залишити дівчину":
            show alina default_sad
            $ love_alina -=10
            $ Alina_num = False
            brain "Мене не цікавлять дівчата, тому я проігнорував її спроби поговорити та вже скоро наблизився до Стрийського ларька"
    hide alina default
    hide screen lovemetr_alina
    $ renpy.notify("Вона запам'ятає це")
    show bg larek_day
    with fade
    show vlad sweat_mayka
    with dissolve
    vlad "Оцей будь ласка"
    voice "Він як завжди вибрав свій улюблений китайський протеїн та колу і пішов додому..."
    play sound "audio/cola.mp3"
    hide vlad sweat_mayka
    hide bg larek_day
    show bg street2_dusk
    with fade
    brain "Поки я ходив вже стемніло, треба скоріше повертатися додому, бо мама поб'є"
    hide bg street2_dusk
    show bg hata_night
    with fade
    show vlad_mama angry
    with dissolve
    mama_vlada "Чому ти так піздно прийшов? Їжа вже охолола"
    hide bg hata_night
    hide vlad_mama angry
    show bg room_night
    with fade
    vlad "Я вже наївся тому пішов до себе в кімнату"
    show vlad default_sleep
    with dissolve
    vlad "Я вирубився дуже швидко"
    voice "От так і завершився перший день Влада в новому місті"
    stop music
    jump day_2
    return

label day_2:
    scene bg room_morning with fade
    play sound "audio/alarm_clock.mp3"
    vlad "{cps=20}Чорт вже ранок... {w=1}наче взагалі не спав, {w=3}треба прокидатися, {w=2}сьогодні все ж таки {b}перший{/b} день в колледжі і не хотілось би запізнитись{/cps}"
    scene bg kitchen_day with fade
    brain "На столі лежав мамин гаманець"
    menu:
        "Що мені зробити?"

        "Відмовитися від спокуси":
            $ take_mom_money = False
            brain "Ми і так зводимо кінці з кінцями, {w=1}після того як мій тато пішов за хлібом {w=1}і не повернувся"
        
        "Взяти невеличку купюру":
            $ take_mom_money = True
            $ gg_money += 100
            brain "Нічого страшного якщо я візьму трішки"
            $ renpy.notify("Вона запам'ятає це")
    
    "{b}06:21{/b}"
    brain "Треба вже збиратися"
    scene bg bathroom with fade
    show vlad default_sleep
    play sound "audio/bathroom_water_sounds.mp3"
    vlad "{cps=20}Хм {w=1}цікаво чи знайду я собі там друзів{/cps}"
    vlad "Гарна водичка"
    scene bg hata_day
    show vlad uniform_normal at left with dissolve
    show vlad_mama speak at right with dissolve
    mama_vlada "Ти вже йдеш?"
    vlad "Так, хочу ще в ларьок заскочить, тому пораніше вийшов"
    "{i}*Мама поцілувала сина*{/i}"
    show vlad uniform_angry
    vlad "Та ну мам шо ти робиш я  вже дорослий"
    mama_vlada "Ой ну вибач, {w=1}йди вже"
    play music "audio/mus.mp3" fadein 1.0 volume 0.5
    scene bg larek_day with fade
    "{b}Влад!{/b}"
    brain "Хтось голосно викрикнув моє ім'я"
    show bodya default with moveinright
    vlad "{cps=20}Єбать Бодя то шо ти? {w=1}Господи в тебе все волосся випало, ось до чого доводять наркотики, {w=1}добре шо я за ЗОЖ{/cps}"
    show bodya speak
    hide body default
    bodya "Кароче хочеш хапнуть в мене крек новий з тайланду"
    vlad "Та я тебе знаю, шо ти вже там нахімічив"
    bodya "Я не пиздю ріл з тайланду, давай я тобі пробу дам і знижку"
    vlad "Ладно вірю, скіки пакетик?"
    bodya "Для тебе як завжди {w=1}за {b}сотку{/b}"
    show screen lovemetr_bodya
    menu:
        "Розважитися перед коледжем?"

        "Звичайно ж!" if int(gg_money) >=100:
            $ gg_money -=100
            vlad "Давай його сюди!"
            $ inventory.append("Drugs")
        "Відмовитися":
            vlad "Фу, ти думаєш я наркоман? {w=1}Тимпаче мені сьогодні до коледжу"
    bodya """
    Добре, може зайдеш до мене сьогодні увечері?
    
    Згадаємо дитинство
    """
    menu:
        "Зайти після коледжу до Боді?"
        
        "Як я можу таке пропустити?":
            $ love_bodya += 10
            $ check_bodya_in_club = True
            vlad "Добре, заскочу на годинку"
            vlad "Ти все ще в підвалі з мамою живеш?"
            bodya "Грошей майже немає, тому все ще планую з'їхати. {w=1}Ти приходь сьогодні в новий клуб \"Зоряна Галявина\" я там барменом працюю"
        "Я сьогодні в зал, тому не зможу":
            $ check_bodya_in_club = False

    bodya "А, і ось тобі мій новий номер, мусора чуть не зловили, тому сімку прийшлось змінити"
    $ Bodya_num = True
    $ inventory.append(Bodya_num)
    show bodya speak at right with move
    nvl_narrator "Нове повідомлення"
    b_s_nvl "."
    if check_bodya_in_club:
        b_s_nvl '32°40\'34.5"N 117°09\'27.6"W'
        bodya "Кинув корди клубу"
    vlad "Добре, мені треба спішити"
    hide screen lovemetr_bodya with dissolve
    stop music
    voice "Влад дивиться на час і бачить що може cпізнитись{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}."
    scene bg busstop_day_summer with dissolve
    play music "audio/cikadi.mp3" fadein 5 volume 0.1
    brain "{sc}{b}{i}{font=FOT-PopJoyStd-B.otf}{=scream_style}ЧОРТ{/b}{/font}{/i}{/=scream_style}{/sc}"
    vlad "{atl=fade_in_text}Я не встиг на автобус...{/atl=fade_in_text}"
    vlad "Чекати{w=1}{cps=20}, або викликати таксі?"
    scene black with dissolve
    menu:
        "Що мені зробити?"

        "Викликати таксі на мамині гроші(-100)" if gg_money>=100:
            #доробити
            pass

        "Почекаю на новий автобус":
            if Alina_num:
                call bus_with_alina from _call_bus_with_alina
            else:
                call bus_without_alina from _call_bus_without_alina
        "Прогуляти пари":
            pass

    stop music
    scene bg bus_school_afternoon with dissolve
    play audio "audio/school_bell.mp3" volume 0.5
    vlad "{cps=20}Схоже вже пара, треба бігти{/cps}"
    scene bg school_building_day with dissolve
    voice "{cps=25}До цього моменту Влад ще не бачив будівлю коледжу. Вона вразила його, залишаючи приємні враження та атмосферу"
    scene bg school_corridor with dissolve
    play sound "audio/background_sound_peoples.mp3" fadein 1.0 volume 0.5
    brain "{cps=25}У коридорах все ще товпиться багато людей, і здається, що ніхто не поспішає на пару так, як це роблю я"
    vlad "{cps=25}Наче цей кабінет"
    play sound "audio/wood-door-opeining-and-creaking.mp3"
    scene bg classroom_day with dissolve
    brain "В класі вже була вся група та наша кураторка...через це мені було ніяково"
    vlad "{cps=8}В-вибачте{/cps} {cps=20}за запізнення{/cps}"
    show currator_default with dissolve
    show screen lovemetr_currator
    currator "{fi=0-0.5}Ще один запізнився, сідайте поряд з Кухтіним в кінці{/fi}"
    $ love_currator+=5
    currator "Кхм, про що я там говорила?"
    #додати відповідь
    hide currator_default
    hide screen lovemetr_currator
    brain "Куратор розповідала як буде влаштовано наше студентське життя.{w} Але мене цікавило дещо інше{w=0.5}.{w=0.5}.{w=0.5}."
    show vlad2_uniform_normal with fade
    brain "Біловолосий хлопець, що сидів за одною партою зі мною біля вікна"
    brain "Раптом ми пересіклися поглядами"
    show vlad2_uniform_smile with fade
    show screen lovemetr_kyn
    brain "Я {atl=bounce}збентежився{/atl}"
    brain "{cps=15}Завдяки сонечку я зміг повністю розглянути його вираз обличчя.{/cps} {w=1}{cps=20}Його посмішка осліпила мене.{/cps} {w=1}{cps=20}Веселий блиск його очей нагадував мені розквітаючі пелюстки квітки,{w=1} відкриваючі переді мною всесвіт радості та невичерпного оптимізму.{/cps}"
    $ love_kyn +=5
    call titles from _call_titles
    return
print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
 ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print("You're at a crossroad. Where do you want to go?")
direction = input("Type 'left' or 'right': ")
if direction == "left" or direction == "LEFT" or direction == "Left":
  print("\nYou've come to a beautiful beach. \nThere is an island a little bit far at the sea.")
  print('''
  ************************************************************
        ___ __ 
       (_  ( . ) )__                  '.    \   :   /    .'
         '(___(_____)      __           '.   \  :  /   .'
                         /. _\            '.  \ : /  .'
                    .--.|/_/__      -----____   _  _____-----
    _______________''.--o/___  \_______________(_)___________
           ~        /.'o|_o  '.|  ~                   ~   ~
      ~            |/    |_|  ~'         ~
                   '  ~  |_|        ~       ~     ~     ~
          ~    ~          |_|O  ~                       ~
                 ~     ___|_||_____     ~       ~    ~
       ~    ~      .'':. .|_|A:. ..::''.
                 /:.  .:::|_|.\ .:.  :.:\   ~
      ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
                 \.: .:  :. .: ..:: .lcf/
        ~      ~      ~    ~    ~         ~
                   ~           ~    ~   ~             ~
            ~         ~            ~   ~                 ~
       ~                  ~    ~ ~                 ~
  ************************************************************
  ''')
  wait_or_swim = input("Type 'wait' to wait for a boat. Type 'swim' to swim across: ")
  if wait_or_swim == "wait" or wait_or_swim == "Wait" or wait_or_swim == "WAIT":
    print("\nYou arrive at the island unharmed. \nThere is a hidden shelter and the password to the entrance has 3 color buttons. \nOne red, one yellow and one blue.")
    color = input("Which color do you choose? ")
    if color == "red" or color == "Red" or color == "RED":
      print("\nRed....\nis....\nthe....\ncolor...\nof...\nfire!!!!!!!!\nYou are burned by fire. \nGame Over.")
      print('''


                      --=[GAME OVER]=--
           (  .      )
                 )           (              )
                       .  '   .   '  .  '  .
              (    , )       (.   )  (   ',    )
               .' ) ( . )    ,  ( ,     )   ( .
            ). , ( .   (  ) ( , ')  .' (  ,    )
           (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
      ***************************************************
      ''')
    elif color == "blue" or color == "Blue" or color == "BLUE":
      print("\nOh no! \nYou've invoked the treasure keeper!!! \nAn aaaaaaaaaaaangry Dragon!\nDo I need to tell you what happens next?\nGame Over.")
      print('''

                             --=[GAME OVER]=--
                                                    ,--,  ,.-.
                      ,                   \,       '-,-`,'-.' | ._
                     /|           \    ,   |\         }  )/  / `-,',
                     [ '          |\  /|   | |        /  \|  |/`  ,`
                     | |       ,.`  `,` `, | |  _,...(   (      _',
                     \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L
                      \  \_\,``,   ` , ,  /  |         )         _,/
                       \  '  `  ,_ _`_,-,<._.<        /         /
                        ', `>.,`  `  `   ,., |_      |         /
                          \/`  `,   `   ,`  | /__,.-`    _,   `<
                      -,-..\  _  \  `  /  ,  / `._) _,-\`       <
                       \_,,.) /\    ` /  / ) (-,, ``    ,        |
                      ,` )  | \_\       '-`  |  `(               <
                     /  /```(   , --, ,' \   |`<`    ,            |
                    /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
              ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
             (-, \           ) \ ('_.-._)/ /,`    /
             | /  `          `/ \\ V   V, /`     /
          ,--\(        ,     <_/`\\     ||      /
         (   ,``-     \/|         \-A.A-`|     /
        ,>,_ )_,..(    )\          -,,_-`  _--`
       (_ \|`   _,/_  /  \_            ,--`
        \( `   <.,../`     `-.._   _,-`
         `                      ```


      ''')
    elif color == "yellow" or color == "Yellow" or color == "YELLOW":
      print("\nYEEEEEES!!!!!\nYou found the treasure! \n\n")
      print('''
                                     --||[You Win!]||--
      *******************************************************************************
                |                   |                  |                     |
       _________|________________.=""_;=.______________|_____________________|_______
      |                   |  ,-"_,=""     `"=.|                  |
      |___________________|__"=._o`"-._        `"=.______________|___________________
                |                `"=._o`"=._      _`"=._                     |
       _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
      |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
      |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
       _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
      |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
      |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
      ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
      /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
      ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
      /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
      ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
      /______/______/______/______/______/______/______/______/______/______/_____ /
      *******************************************************************************
      ''')

  else:
    print("\nOh no!!! \nYou get attacked by a hungry shark! \nGame Over.")
    print('''

                             --=[GAME OVER]=--
                                     ,-
                                   ,'::|
                                  /::::|
                                ,':::::|                                      _..
             ____........-------,..::::|.                                  ,-' /
     _.--"""". . . .      .   .  .  .  ""`-._                           ,-' .;'
    <. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'
     `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
         """_=--       //''::.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
             ""--.__     <(       \               ` ``:`:``:::: .   .;'
                    "\""--.:-.     `.                             .:/
                      \. /    `-._   `.""-----.,-..::(--"".\""`.  `:<
                       `P         `-._ \          `-:\          `. `:<
                                       ""            "            `-._)

    ''')




else:
  print("\nIt's a trap!!! \nYou fell into a hole.\nGame Over.")
  print('''

                          --=[GAME OVER]=--

              ___           _,.---,---.,_
              |         ,;~'             '~;,
              |       ,;                     ;,
     Frontal  |      ;                         ; ,--- Supraorbital Foramen
      Bone    |     ,'                         /'
              |    ,;                        /' ;,
              |    ; ;      .           . <-'  ; |
              |__  | ;   ______       ______   ;<----- Coronal Suture
             ___   |  '/~"     ~" . "~     "~\'  |
             |     |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
   Maxilla,  |      |   |        }:{        | <------ Orbit
  Nasal and  |      |   l       / | \       !   |
  Zygomatic  |      .~  (__,.--" .^. "--.,__)  ~.
    Bones    |      |    ----;' / | \ `;-<--------- Infraorbital Foramen
             |__     \__.       \/^\/       .__/
                ___   V| \                 / |V <--- Mastoid Process
                |      | |T~\___!___!___/~T| |
                |      | |`IIII_I_I_I_IIII'| |
       Mandible |      |  \,III I I I III,/  |
                |       \   `~~~~~~~~~~'    /
                |         \   .       . <-x---- Mental Foramen
                |__         \.    ^    ./
                              ^~~~^~~~^       

  ''')
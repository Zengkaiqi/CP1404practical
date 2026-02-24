CODE_TO_COLOR = {"Absolute Zero":"#0048ba",
                 "Acid Green":"#b0bf1a",
                 "Bone":"#e3dbe2",
                 "Brandeis Blue":"#0070ff",
                 "Cameo Pink":"#efbbcc",
                 "Canary Yellow":"#ffef00",
                 "Dark Sky Blue":"#8cbed6",
                 "Deep Peach":"#ffcba4",
                 "Falu Red":"#801818",
                 "Fire Opal":"#ee95c4b"
}
color_name = input("Enter the  colour: ").title()
while color_name != "":
    try:
        print(CODE_TO_COLOR[color_name])
    except KeyError:
        print("Invalid colour")
    color_name = input("Enter the  colour: ").title()

from enum import Enum

class Rock(Enum):
    """Rock type enums pointing to rock emojis in Discord.\n
    Contains the text emojis, discord icon, icon image, and style bars.\n
    \n
    Contains:\n
    Letters A-Z - Discord emoji pointers to rock letters\n
    ICON - Discord icon\n
    ICON_IMAGE - Icon image link\n
    BAR_END_FILL - End of bar filled\n
    BAR_START_FILL - Start of bar filled\n
    BAR_MIDDLE_FILL_SPLIT - Half filled bar middle\n
    BAR_MIDDLE_FILL - Fully filled bar middle\n
    BAR_START_FILL_SPLIT - Bar start filled a little bit\n
    """
    
    A = "<:R_A:1131678520846852118>"
    B = "<:R_B:1131678529323532449>"
    C = "<:R_C:1131678538077057025>"
    D = "<:R_D:1131678546742476860>"
    E = "<:R_E:1131678554917183568>"
    F = "<:R_F:1131678563515498496>"
    G = "<:R_G:1131678571996381234>"
    H = "<:R_H:1131678581219668038>"
    I = "<:R_I:1131678592921776279>"
    J = "<:R_J:1131678601411055667>"
    K = "<:R_K:1131678609933861036>"
    L = "<:R_L:1131678618314096792>"
    M = "<:R_M:1131678626509754429>"
    N = "<:R_N:1131678634432798812>"
    O = "<:R_O:1131678642896900217>"
    P = "<:R_P:1131678651356827789>"
    Q = "<:R_Q:1131678660047413358>"
    R = "<:R_R:1131678668016603177>"
    S = "<:R_S:1131678676019331223>"
    T = "<:R_T:1131678685523624106>"
    U = "<:R_U:1131678693874479114>"
    V = "<:R_V:1131678701893988432>"
    W = "<:R_W:1131678709917679748>"
    X = "<:R_X:1131678719421976668>"
    Y = "<:R_Y:1131678729941303296>"
    Z = "<:R_Z:1131678738011132004>"
    
    # ICON = '<:RockIC:1133942118235263027>'
    ICON = '<:Rock:1133950917251711126>'
    ICON_IMAGE = 'https://cdn.discordapp.com/attachments/1131643315993976884/1139012800178561135/Rock.png'

    BAR_END_FILL = '<:bar_end_fill_rock:1133845175890890782>'
    BAR_START_FILL = '<:bar_start_fill_rock:1133845241028419598>'
    BAR_MIDDLE_FILL_SPLIT = '<:bar_middle_fill_split_rock:1133845225027141632>'
    BAR_MIDDLE_FILL = '<:bar_middle_fill_rock:1133845197680279614>'
    BAR_START_FILL_SPLIT = '<:bar_start_fill_split_rock:1133845259261071520>'
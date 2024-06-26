from enum import Enum


class Dark(Enum):
    """Dark type enums pointing to dark emojis in Discord.\n
    Contains the text emojis, discord icon, icon image, and style bars.\n
    \n
    Contains:\n
    Letters A-Z - Discord emoji pointers to dark letters\n
    ICON - Discord icon\n
    ICON_IMAGE - Icon image link\n
    BAR_END_FILL - End of bar filled\n
    BAR_START_FILL - Start of bar filled\n
    BAR_MIDDLE_FILL_SPLIT - Half filled bar middle\n
    BAR_MIDDLE_FILL - Fully filled bar middle\n
    BAR_START_FILL_SPLIT - Bar start filled a little bit\n
    
    """
    
    A = "<:D_A:1131687856176365671>"
    B = "<:D_B:1131687864225243216>"
    C = "<:D_C:1131687873305919598>"
    D = "<:D_D:1131687881572880384>"
    E = "<:D_E:1131687890452234451>"
    F = "<:D_F:1131687898119413801>"
    G = "<:D_G:1131687906147311766>"
    H = "<:D_H:1131687915072798840>"
    I = "<:D_I:1131687927160778825>"
    J = "<:D_J:1131687935570366525>"
    K = "<:D_K:1131687944080588962>"
    L = "<:D_L:1131687952439840788>"
    M = "<:D_M:1131687960597774378>"
    N = "<:D_N:1131687968663412787>"
    O = "<:D_O:1131687976561291295>"
    P = "<:D_P:1131687984853422121>"
    Q = "<:D_Q:1131687993325920326>"
    R = "<:D_R:1131688001181860011>"
    S = "<:D_S:1131688009343979550>"
    T = "<:D_T:1131688017581580439>"
    U = "<:D_U:1131688025139720232>"
    V = "<:D_V:1131688032966299669>"
    W = "<:D_W:1131688041279397928>"
    X = "<:D_X:1131688050121003028>"
    Y = "<:D_Y:1131688058106957944>"
    Z = "<:D_Z:1131688065878994994>"
    
    # ICON = '<:DarkIC:1133942823549403248>'
    ICON = '<:Dark:1133950344251064412>'
    ICON_IMAGE = 'https://cdn.discordapp.com/attachments/1131641317349412896/1139011121244815381/Dark.png'

    BAR_END_FILL = '<:bar_end_fill_dark:1133851195497259038>'
    BAR_START_FILL = '<:bar_start_fill_dark:1133851312216350812>'
    BAR_MIDDLE_FILL_SPLIT = '<:bar_middle_fill_split_dark:1133851248643284992>'
    BAR_MIDDLE_FILL = '<:bar_middle_fill_dark:1133851216162590873>'
    BAR_START_FILL_SPLIT = '<:bar_start_fill_split_dark:1133851279089733632>'
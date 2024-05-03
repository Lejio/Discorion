from enum import Enum

class Ground(Enum):
    """Ground type enums pointing to ground emojis in Discord.\n
    Contains the text emojis, discord icon, icon image, and style bars.\n
    \n
    Contains:\n
    Letters A-Z - Discord emoji pointers to ground letters\n
    ICON - Discord icon\n
    ICON_IMAGE - Icon image link\n
    BAR_END_FILL - End of bar filled\n
    BAR_START_FILL - Start of bar filled\n
    BAR_MIDDLE_FILL_SPLIT - Half filled bar middle\n
    BAR_MIDDLE_FILL - Fully filled bar middle\n
    BAR_START_FILL_SPLIT - Bar start filled a little bit\n
    """

    A = "<:G_A:1131684728592932874>"
    B = "<:G_B:1131684736700530688>"
    C = "<:G_C:1131684744854253628>"
    D = "<:G_D:1131684752869572678>"
    E = "<:G_E:1131684760746459266>"
    F = "<:G_F:1131684769353179217>"
    G = "<:G_G:1131684777611767828>"
    H = "<:G_H:1131684787111870537>"
    I = "<:G_I:1131684795517247598>"
    J = "<:G_J:1131684803582886049>"
    K = "<:G_K:1131684811422056579>"
    L = "<:G_L:1131684819244421260>"
    M = "<:G_M:1131684827226189884>"
    N = "<:G_N:1131684835472183306>"
    O = "<:G_O:1131684843206496326>"
    P = "<:G_P:1131684853327335556>"
    Q = "<:G_Q:1131684862047293532>"
    R = "<:G_R:1131684870414938142>"
    S = "<:G_S:1131684878702878811>"
    T = "<:G_T:1131684886781100054>"
    U = "<:G_U:1131684895140364298>"
    V = "<:G_V:1131684903109529710>"
    W = "<:G_W:1131684912420880456>"
    X = "<:G_X:1131684919781900309>"
    Y = "<:G_Y:1131684928539607070>"
    Z = "<:G_Z:1131684937385394287>"
    
    # ICON = '<:GroundIC:1133942336204836956>'
    ICON = '<:Ground:1133950684522369044>'
    ICON_IMAGE = 'https://cdn.discordapp.com/attachments/1131642401073676442/1139012115559088240/Ground.png'
    
    BAR_END_FILL = '<:bar_end_fill_ground:1133844404763901982>'
    BAR_START_FILL = '<:bar_start_fill_ground:1133844537421349036>'
    BAR_MIDDLE_FILL_SPLIT = '<:bar_middle_fill_split_ground:1133844460946600018>'
    BAR_MIDDLE_FILL = '<:bar_middle_fill_ground:1133844429157978313>'
    BAR_START_FILL_SPLIT = '<:bar_start_fill_split_ground:1133844478344568832>'
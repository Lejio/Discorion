from enum import Enum

class Steel(Enum):
    """Steel type enums pointing to steel emojis in Discord.\n
    Contains the text emojis, discord icon, icon image, and style bars.\n
    \n
    Contains:\n
    Letters A-Z - Discord emoji pointers to steel letters\n
    ICON - Discord icon\n
    ICON_IMAGE - Icon image link\n
    BAR_END_FILL - End of bar filled\n
    BAR_START_FILL - Start of bar filled\n
    BAR_MIDDLE_FILL_SPLIT - Half filled bar middle\n
    BAR_MIDDLE_FILL - Fully filled bar middle\n
    BAR_START_FILL_SPLIT - Bar start filled a little bit\n
    """
    
    A = "<:S_A:1131677835115905044>"
    B = "<:S_B:1131677843726811207>"
    C = "<:S_C:1131677852283179079>"
    D = "<:S_D:1131677860562735175>"
    E = "<:S_E:1131677868364148756>"
    F = "<:S_F:1131677876492718171>"
    G = "<:S_G:1131677884717748234>"
    H = "<:S_H:1131677892565287022>"
    I = "<:S_I:1131677901352345610>"
    J = "<:S_J:1131677909984215070>"
    K = "<:S_K:1131677919014559764>"
    L = "<:S_L:1131677927235387524>"
    M = "<:S_M:1131677936186044576>"
    N = "<:S_N:1131677944159424603>"
    O = "<:S_O:1131677952678039683>"
    P = "<:S_P:1131677960798220288>"
    Q = "<:S_Q:1131677969174245437>"
    R = "<:S_R:1131677977567043654>"
    S = "<:S_S:1131677985397817426>"
    T = "<:S_T:1131677993463447642>"
    U = "<:S_U:1131678001663328256>"
    V = "<:S_V:1131678009863176353>"
    W = "<:S_W:1131678019711414414>"
    X = "<:S_X:1131678028003561493>"
    Y = "<:S_Y:1131678037314908180>"
    Z = "<:S_Z:1131678045510578318>"
    
    # ICON = '<:SteelIC:1133942008583553125>'
    ICON = '<:Steel:1133951046796980316>'
    ICON_IMAGE = 'https://cdn.discordapp.com/attachments/1131643383396446281/1139012945188233286/Steel.png'

    BAR_END_FILL = '<:bar_end_fill_steel:1133851658825240707>'
    BAR_START_FILL = '<:bar_start_fill_steel:1133851782947283064>'
    BAR_MIDDLE_FILL_SPLIT = '<:bar_middle_fill_split_steel:1133851700613099571>'
    BAR_MIDDLE_FILL = '<:bar_middle_fill_steel:1133851719655227443>'
    BAR_START_FILL_SPLIT = '<:bar_start_fill_split_steel:1133851764718850130>'
from enum import Enum

class Normal(Enum):
    """Normal type enums pointing to normal emojis in Discord.\n
    Contains the text emojis, discord icon, icon image, and style bars.\n
    \n
    Contains:\n
    Letters A-Z - Discord emoji pointers to normal letters\n
    ICON - Discord icon\n
    ICON_IMAGE - Icon image link\n
    BAR_END_FILL - End of bar filled\n
    BAR_START_FILL - Start of bar filled\n
    BAR_MIDDLE_FILL_SPLIT - Half filled bar middle\n
    BAR_MIDDLE_FILL - Fully filled bar middle\n
    BAR_START_FILL_SPLIT - Bar start filled a little bit\n
    """
    
    A = "<:N_A:1131683597250740284>"
    B = "<:N_B:1131683606276878347>"
    C = "<:N_C:1131683614669672568>"
    D = "<:N_D:1131683623553212647>"
    E = "<:N_E:1131683632055066707>"
    F = "<:N_F:1131683640917643264>"
    G = "<:N_G:1131683649490792489>"
    H = "<:N_H:1131683657891975319>"
    I = "<:N_I:1131683666368663695>"
    J = "<:N_J:1131683674497220680>"
    K = "<:N_K:1131683682395107438>"
    L = "<:N_L:1131683690439790612>"
    M = "<:N_M:1131683698622857247>"
    N = "<:N_N:1131683706747232357>"
    O = "<:N_O:1131683715169398925>"
    P = "<:N_P:1131683722970804295>"
    Q = "<:N_Q:1131683730969329845>"
    R = "<:N_R:1131683739525730425>"
    S = "<:N_S:1131683747901747311>"
    T = "<:N_T:1131683755992547329>"
    U = "<:N_U:1131683764901265449>"
    V = "<:N_V:1131683772996276364>"
    W = "<:N_W:1131683780730568785>"
    X = "<:N_X:1131683789123354664>"
    Y = "<:N_Y:1131683796786368513>"
    Z = "<:N_Z:1131683805313380362>"
    
    # ICON = '<:NormalIC:1133941298450137128>'
    ICON = '<:Normal:1133951091030106222>'
    ICON_IMAGE = 'https://cdn.discordapp.com/attachments/1131643449855201322/1139012404827672696/Normal.png'
    
    BAR_END_FILL = '<:bar_end_fill_normal:1133851833488642210>'
    BAR_START_FILL = '<:bar_start_fill_normal:1133851931455012944>'
    BAR_MIDDLE_FILL_SPLIT = '<:bar_middle_fill_split_normal:1133851881404383253>'
    BAR_MIDDLE_FILL = '<:bar_middle_fill_normal:1133851852732121159>'
    BAR_START_FILL_SPLIT = '<:bar_start_fill_split_normal:1133851907975286865>'
from enum import Enum

class Flying(Enum):
    """Flying type enums pointing to flying emojis in Discord.\n
    Contains the text emojis, discord icon, icon image, and style bars.\n
    \n
    Contains:\n
    Letters A-Z - Discord emoji pointers to flying letters\n
    ICON - Discord icon\n
    ICON_IMAGE - Icon image link\n
    BAR_END_FILL - End of bar filled\n
    BAR_START_FILL - Start of bar filled\n
    BAR_MIDDLE_FILL_SPLIT - Half filled bar middle\n
    BAR_MIDDLE_FILL - Fully filled bar middle\n
    BAR_START_FILL_SPLIT - Bar start filled a little bit\n
    """
    
    A = "<:F_A:1131686298634174505>"
    B = "<:F_B:1131686306603339917>"
    C = "<:F_C:1131686315180703754>"
    D = "<:F_D:1131686323321852005>"
    E = "<:F_E:1131686331160997999>"
    F = "<:F_F:1131686339801255936>"
    G = "<:F_G:1131686348256972820>"
    H = "<:F_H:1131686356125499472>"
    I = "<:F_I:1131686364103053314>"
    J = "<:F_J:1131686371933818880>"
    K = "<:F_K:1131686380515368970>"
    L = "<:F_L:1131686388702650509>"
    M = "<:F_M:1131686396747325441>"
    N = "<:F_N:1131686406381633606>"
    O = "<:F_O:1131686415378415648>"
    P = "<:F_P:1131686423808974868>"
    Q = "<:F_Q:1131686431375507678>"
    R = "<:F_R:1131686439617310931>"
    S = "<:F_S:1131686447955574944>"
    T = "<:F_T:1131686456457449562>"
    U = "<:F_U:1131686464749576274>"
    V = "<:F_V:1131686472689385523>"
    W = "<:F_W:1131686480528543834>"
    X = "<:F_X:1131686489525342338>"
    Y = "<:F_Y:1131686497318355085>"
    Z = "<:F_Z:1131686505421737984>"
    
    # ICON = '<:FlyingIC:1133942526735294556>'
    ICON = '<:Flying:1133950570454077531>'
    ICON_IMAGE = 'https://cdn.discordapp.com/attachments/1131642109779255348/1139011783600898198/Flying.png'

    BAR_END_FILL = '<:bar_end_fill_flying:1133843812695941180>'
    BAR_START_FILL = '<:bar_start_fill_flying:1133843981629915186>'
    BAR_MIDDLE_FILL_SPLIT = '<:bar_middle_fill_split_flying:1133843876118016080>'
    BAR_MIDDLE_FILL = '<:bar_middle_fill_flying:1133843851174490192>'
    BAR_START_FILL_SPLIT = '<:bar_start_fill_split_flying:1133843938306953286>'
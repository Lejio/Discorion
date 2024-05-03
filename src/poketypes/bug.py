from enum import Enum


class Bug(Enum):
    """Bug type enums pointing to bug emojis in Discord.\n
    Contains the text emojis, discord icon, icon image, and style bars.\n
    \n
    Contains:\n
    Letters A-Z - Discord emoji pointers to bug letters\n
    ICON - Discord icon\n
    ICON_IMAGE - Icon image link\n
    BAR_END_FILL - End of bar filled\n
    BAR_START_FILL - Start of bar filled\n
    BAR_MIDDLE_FILL_SPLIT - Half filled bar middle\n
    BAR_MIDDLE_FILL - Fully filled bar middle\n
    BAR_START_FILL_SPLIT - Bar start filled a little bit\n
    """
    
    A = "<:B_A:1131688175190945955>"
    B = "<:B_B:1131688183537614920>"
    C = "<:B_C:1131688191666163835>"
    D = "<:B_D:1131688200969142312>"
    E = "<:B_E:1131688208862818314>"
    F = "<:B_F:1131688216760701079>"
    G = "<:B_G:1131688225598099518>"
    H = "<:B_H:1131688235278536764>"
    I = "<:B_I:1131688243432280084>"
    J = "<:B_J:1131688252399698001>"
    K = "<:B_K:1131688260893147296>"
    L = "<:B_L:1131688269206261840>"
    M = "<:B_M:1131688277250945055>"
    N = "<:B_N:1131688285220122724>"
    O = "<:B_O:1131688293214457878>"
    P = "<:B_P:1131688302148325407>"
    Q = "<:B_Q:1131688310201389066>"
    R = "<:B_R:1131688319177216000>"
    S = "<:B_S:1131688327293194260>"
    T = "<:B_T:1131688335178481804>"
    U = "<:B_U:1131688343080538273>"
    V = "<:B_V:1131688351372689509>"
    W = "<:B_W:1131688359698378894>"
    X = "<:B_X:1131688368040845413>"
    Y = "<:B_Y:1131688376437854278>"
    Z = "<:B_Z:1131688384193110056>"
    
    # ICON = '<:BugIC:1133942889710370866>'
    ICON = '<:Bug:1133950296255643738>'
    ICON_IMAGE = "https://cdn.discordapp.com/attachments/1131642327165837364/1139010943863500941/Bug.png"
        
    BAR_END_FILL = '<:bar_end_fill_bug:1133843032026923109>'    
    BAR_START_FILL = '<:bar_start_fill_bug:1133843160200646676>'
    BAR_MIDDLE_FILL_SPLIT = '<:bar_middle_fill_split_bug:1133843136569937960>'
    BAR_MIDDLE_FILL = '<:bar_middle_fill_bug:1133843046715375656>'
    BAR_START_FILL_SPLIT = "<:bar_start_fill_split_bug:1133843202919628910>"
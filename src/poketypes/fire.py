from enum import Enum

class Fire(Enum):
    """Fire type enums pointing to fire emojis in Discord.\n
    Contains the text emojis, discord icon, icon image, and style bars.\n
    \n
    Contains:\n
    Letters A-Z - Discord emoji pointers to fire letters\n
    ICON - Discord icon\n
    ICON_IMAGE - Icon image link\n
    BAR_END_FILL - End of bar filled\n
    BAR_START_FILL - Start of bar filled\n
    BAR_MIDDLE_FILL_SPLIT - Half filled bar middle\n
    BAR_MIDDLE_FILL - Fully filled bar middle\n
    BAR_START_FILL_SPLIT - Bar start filled a little bit\n
    """
    
    A = "<:F_A:1131686695369199757>"
    B = "<:F_B:1131686703992668261>"
    C = "<:F_C:1131686712033169418>"
    D = "<:F_D:1131686720128155718>"
    E = "<:F_E:1131686728659382373>"
    F = "<:F_F:1131686735919726734>"
    G = "<:F_G:1131686743897280643>"
    H = "<:F_H:1131686752306856007>"
    I = "<:F_I:1131686760540282990>"
    J = "<:F_J:1131686769042141335>"
    K = "<:F_K:1131686777418154085>"
    L = "<:F_L:1131686786192646224>"
    M = "<:F_M:1131686793952100444>"
    N = "<:F_N:1131686801870958602>"
    O = "<:F_O:1131686809890472017>"
    P = "<:F_P:1131686817704452131>"
    Q = "<:F_Q:1131686826155966544>"
    R = "<:F_R:1131686834062249994>"
    S = "<:F_S:1131686842777993326>"
    T = "<:F_T:1131686850579398767>"
    U = "<:F_U:1131686858615701564>"
    V = "<:F_V:1131686866358382653>"
    W = "<:F_W:1131686874130436197>"
    X = "<:F_X:1131686882217046056>"
    Y = "<:F_Y:1131686891293524138>"
    Z = "<:F_Z:1131686899786989618>"
    
    # ICON = '<:FireIC:1133942586428620860>'
    ICON = '<:Fire:1133950498345586689>'
    ICON_IMAGE = 'https://cdn.discordapp.com/attachments/1131642028434915370/1139011684195909782/Fire.png'
    
    BAR_END_FILL = '<:bar_end_fill_fire:1133843621632806973>'
    BAR_START_FILL = '<:bar_start_fill_fire:1133843726691737752>'
    BAR_MIDDLE_FILL_SPLIT = '<:bar_middle_fill_split_fire:1133843707397935264>'
    BAR_MIDDLE_FILL = '<:bar_middle_fill_fire:1133843649764007978>'
    BAR_START_FILL_SPLIT = '<:bar_start_fill_split_fire:1133843745431896104>'
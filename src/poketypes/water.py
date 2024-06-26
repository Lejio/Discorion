from enum import Enum

class Water(Enum):
    """Water type enums pointing to water emojis in Discord.\n
    Contains the text emojis, discord icon, icon image, and style bars.\n
    \n
    Contains:\n
    Letters A-Z - Discord emoji pointers to water letters\n
    ICON - Discord icon\n
    ICON_IMAGE - Icon image link\n
    BAR_END_FILL - End of bar filled\n
    BAR_START_FILL - Start of bar filled\n
    BAR_MIDDLE_FILL_SPLIT - Half filled bar middle\n
    BAR_MIDDLE_FILL - Fully filled bar middle\n
    BAR_START_FILL_SPLIT - Bar start filled a little bit\n
    """
    
    A = "<:W_A:1131694697392390345>"
    B = "<:W_B:1131694705659367474>"
    C = "<:W_C:1131694715188809798>"
    D = "<:W_D:1131694723497742376>"
    E = "<:W_E:1131694731601117235>"
    F = "<:W_F:1131694739431895130>"
    G = "<:W_G:1131694747875033188>"
    H = "<:W_H:1131694755911315577>"
    I = "<:W_I:1131694763733692458>"
    J = "<:W_J:1131694772168429679>"
    K = "<:W_K:1131694781014220821>"
    L = "<:W_L:1131694788966613043>"
    M = "<:W_M:1131694797053247559>"
    N = "<:W_N:1131694806653997167>"
    O = "<:W_O:1131694815105519666>"
    P = "<:W_P:1131694823091478538>"
    Q = "<:W_Q:1131694831165509642>"
    R = "<:W_R:1131694839168249937>"
    S = "<:W_S:1131694847376511016>"
    T = "<:W_T:1131694855597346908>"
    U = "<:W_U:1131694863344222348>"
    V = "<:W_V:1131694871560855712>"
    W = "<:W_W:1131694879743950848>"
    X = "<:W_X:1131694887817990225>"
    Y = "<:W_Y:1131694896445657098>"
    Z = "<:W_Z:1131694904259653682>"
    
    # ICON = '<:WaterIC:1133942213601153038>'
    ICON = '<:Water:1133950816500322304>'
    ICON_IMAGE = 'https://cdn.discordapp.com/attachments/1131643070060969986/1139013048045154354/Water.png'

    BAR_END_FILL = '<:bar_end_fill_water:1133844773954920568>'
    BAR_START_FILL = '<:bar_start_fill_water:1133844902862651453>'
    BAR_MIDDLE_FILL_SPLIT = '<:bar_middle_fill_split_water:1133844801834467471>'
    BAR_MIDDLE_FILL = '<:bar_middle_fill_water:1133844859309015131>'
    BAR_START_FILL_SPLIT = '<:bar_start_fill_split_water:1133844886119010356>'
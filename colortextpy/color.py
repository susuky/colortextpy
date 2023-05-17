# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_color.ipynb.

# %% auto 0
__all__ = ['Color', 'rgb2hex', 'hex2rgb']

# %% ../nbs/00_color.ipynb 3
import enum

class _ClassPropertyDescriptor:
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        return self.fget.__get__(obj, klass)()

    
class _EnumMeta(enum.Enum):
    '''
    Add some custom members for `enum.Enum`
    '''
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)
    
    def __str__(self):
        return self.name.lower()
    
    @property
    def str(self):
        return self.name.lower()
    
    @_ClassPropertyDescriptor
    @classmethod
    def available(cls):
        return tuple(cls.__members__.keys())


class Color(_EnumMeta):
    '''
    Use enum.Enum to store color with **hex**, **rgb**, **bgr** format.
    '''
    aliceblue             = (  0, '#f0f8ff', (240, 248, 255), (255, 248, 240))
    antiquewhite          = (  1, '#faebd7', (250, 235, 215), (215, 235, 250))
    aqua                  = (  2, '#00ffff', (0, 255, 255), (255, 255, 0))
    aquamarine            = (  3, '#7fffd4', (127, 255, 212), (212, 255, 127))
    azure                 = (  4, '#f0ffff', (240, 255, 255), (255, 255, 240))
    bisque                = (  5, '#ffe4c4', (255, 228, 196), (196, 228, 255))
    black                 = (  6, '#000000', (0, 0, 0), (0, 0, 0))
    blanchedalmond        = (  7, '#ffebcd', (255, 235, 205), (205, 235, 255))
    blue                  = (  8, '#0000ff', (0, 0, 255), (255, 0, 0))
    blueviolet            = (  9, '#8a2be2', (138, 43, 226), (226, 43, 138))
    brown                 = ( 10, '#a52a2a', (165, 42, 42), (42, 42, 165))
    burlywood             = ( 11, '#deb887', (222, 184, 135), (135, 184, 222))
    cadetblue             = ( 12, '#5f9ea0', (95, 158, 160), (160, 158, 95))
    chartreuse            = ( 13, '#7fff00', (127, 255, 0), (0, 255, 127))
    chocolate             = ( 14, '#d2691e', (210, 105, 30), (30, 105, 210))
    coral                 = ( 15, '#ff7f50', (255, 127, 80), (80, 127, 255))
    cornflowerblue        = ( 16, '#6495ed', (100, 149, 237), (237, 149, 100))
    cornsilk              = ( 17, '#fff8dc', (255, 248, 220), (220, 248, 255))
    crimson               = ( 18, '#dc143c', (220, 20, 60), (60, 20, 220))
    cyan                  = ( 19, '#00ffff', (0, 255, 255), (255, 255, 0))
    c                     = ( 19, '#00ffff', (0, 255, 255), (255, 255, 0))
    dark_blue             = ( 20, '#00008b', (0, 0, 139), (139, 0, 0))
    dark_cyan             = ( 21, '#008b8b', (0, 139, 139), (139, 139, 0))
    dark_goldenrod        = ( 22, '#b8860b', (184, 134, 11), (11, 134, 184))
    dark_gray             = ( 23, '#a9a9a9', (169, 169, 169), (169, 169, 169))
    dark_green            = ( 24, '#006400', (0, 100, 0), (0, 100, 0))
    dark_khaki            = ( 25, '#bdb76b', (189, 183, 107), (107, 183, 189))
    dark_magenta          = ( 26, '#8b008b', (139, 0, 139), (139, 0, 139))
    dark_olivegreen       = ( 27, '#556b2f', (85, 107, 47), (47, 107, 85))
    dark_orange           = ( 28, '#ff8c00', (255, 140, 0), (0, 140, 255))
    dark_orchid           = ( 29, '#9932cc', (153, 50, 204), (204, 50, 153))
    dark_red              = ( 30, '#8b0000', (139, 0, 0), (0, 0, 139))
    dark_salmon           = ( 31, '#e9967a', (233, 150, 122), (122, 150, 233))
    dark_seagreen         = ( 32, '#8fbc8f', (143, 188, 143), (143, 188, 143))
    dark_slateblue        = ( 33, '#483d8b', (72, 61, 139), (139, 61, 72))
    dark_slategray        = ( 34, '#2f4f4f', (47, 79, 79), (79, 79, 47))
    dark_turquoise        = ( 35, '#00ced1', (0, 206, 209), (209, 206, 0))
    dark_violet           = ( 36, '#9400d3', (148, 0, 211), (211, 0, 148))
    deep_pink             = ( 37, '#ff1493', (255, 20, 147), (147, 20, 255))
    deep_skyblue          = ( 38, '#00bfff', (0, 191, 255), (255, 191, 0))
    dim_gray              = ( 39, '#696969', (105, 105, 105), (105, 105, 105))
    dodgerblue            = ( 40, '#1e90ff', (30, 144, 255), (255, 144, 30))
    firebrick             = ( 41, '#b22222', (178, 34, 34), (34, 34, 178))
    floralwhite           = ( 42, '#fffaf0', (255, 250, 240), (240, 250, 255))
    forestgreen           = ( 43, '#228b22', (34, 139, 34), (34, 139, 34))
    fuchsia               = ( 44, '#ff00ff', (255, 0, 255), (255, 0, 255))
    gainsboro             = ( 45, '#dcdcdc', (220, 220, 220), (220, 220, 220))
    ghostwhite            = ( 46, '#f8f8ff', (248, 248, 255), (255, 248, 248))
    gold                  = ( 47, '#ffd700', (255, 215, 0), (0, 215, 255))
    goldenrod             = ( 48, '#daa520', (218, 165, 32), (32, 165, 218))
    gray                  = ( 49, '#808080', (128, 128, 128), (128, 128, 128))
    green                 = ( 50, '#008000', (0, 128, 0), (0, 128, 0))
    g                     = ( 50, '#008000', (0, 128, 0), (0, 128, 0))
    greenyellow           = ( 51, '#adff2f', (173, 255, 47), (47, 255, 173))
    honeydew              = ( 52, '#f0fff0', (240, 255, 240), (240, 255, 240))
    hotpink               = ( 53, '#ff69b4', (255, 105, 180), (180, 105, 255))
    indianred             = ( 54, '#cd5c5c', (205, 92, 92), (92, 92, 205))
    indigo                = ( 55, '#4b0082', (75, 0, 130), (130, 0, 75))
    ivory                 = ( 56, '#fffff0', (255, 255, 240), (240, 255, 255))
    khaki                 = ( 57, '#f0e68c', (240, 230, 140), (140, 230, 240))
    lavender              = ( 58, '#e6e6fa', (230, 230, 250), (250, 230, 230))
    lavenderblush         = ( 59, '#fff0f5', (255, 240, 245), (245, 240, 255))
    lawngreen             = ( 60, '#7cfc00', (124, 252, 0), (0, 252, 124))
    lemonchiffon          = ( 61, '#fffacd', (255, 250, 205), (205, 250, 255))
    light_blue            = ( 62, '#add8e6', (173, 216, 230), (230, 216, 173))
    light_coral           = ( 63, '#f08080', (240, 128, 128), (128, 128, 240))
    light_cyan            = ( 64, '#e0ffff', (224, 255, 255), (255, 255, 224))
    light_goldenrodyellow = ( 65, '#fafad2', (250, 250, 210), (210, 250, 250))
    light_green           = ( 66, '#90ee90', (144, 238, 144), (144, 238, 144))
    light_grey            = ( 67, '#d3d3d3', (211, 211, 211), (211, 211, 211))
    light_pink            = ( 68, '#ffb6c1', (255, 182, 193), (193, 182, 255))
    light_salmon          = ( 69, '#ffa07a', (255, 160, 122), (122, 160, 255))
    light_seagreen        = ( 70, '#20b2aa', (32, 178, 170), (170, 178, 32))
    light_skyblue         = ( 71, '#87cefa', (135, 206, 250), (250, 206, 135))
    light_slategray       = ( 72, '#778899', (119, 136, 153), (153, 136, 119))
    light_steelblue       = ( 73, '#b0c4de', (176, 196, 222), (222, 196, 176))
    light_yellow          = ( 74, '#ffffe0', (255, 255, 224), (224, 255, 255))
    lime                  = ( 75, '#00ff00', (0, 255, 0), (0, 255, 0))
    limegreen             = ( 76, '#32cd32', (50, 205, 50), (50, 205, 50))
    linen                 = ( 77, '#faf0e6', (250, 240, 230), (230, 240, 250))
    magenta               = ( 78, '#ff00ff', (255, 0, 255), (255, 0, 255))
    maroon                = ( 79, '#800000', (128, 0, 0), (0, 0, 128))
    medium_aquamarine     = ( 80, '#66cdaa', (102, 205, 170), (170, 205, 102))
    medium_blue           = ( 81, '#0000cd', (0, 0, 205), (205, 0, 0))
    medium_orchid         = ( 82, '#ba55d3', (186, 85, 211), (211, 85, 186))
    medium_purple         = ( 83, '#9370db', (147, 112, 219), (219, 112, 147))
    medium_seagreen       = ( 84, '#3cb371', (60, 179, 113), (113, 179, 60))
    medium_slateblue      = ( 85, '#7b68ee', (123, 104, 238), (238, 104, 123))
    medium_springgreen    = ( 86, '#00fa9a', (0, 250, 154), (154, 250, 0))
    medium_turquoise      = ( 87, '#48d1cc', (72, 209, 204), (204, 209, 72))
    medium_violetred      = ( 88, '#c71585', (199, 21, 133), (133, 21, 199))
    midnightblue          = ( 89, '#191970', (25, 25, 112), (112, 25, 25))
    mintcream             = ( 90, '#f5fffa', (245, 255, 250), (250, 255, 245))
    mistyrose             = ( 91, '#ffe4e1', (255, 228, 225), (225, 228, 255))
    moccasin              = ( 92, '#ffe4b5', (255, 228, 181), (181, 228, 255))
    navajowhite           = ( 93, '#ffdead', (255, 222, 173), (173, 222, 255))
    navy                  = ( 94, '#000080', (0, 0, 128), (128, 0, 0))
    oldlace               = ( 95, '#fdf5e6', (253, 245, 230), (230, 245, 253))
    olive                 = ( 96, '#808000', (128, 128, 0), (0, 128, 128))
    olivedrab             = ( 97, '#6b8e23', (107, 142, 35), (35, 142, 107))
    orange                = ( 98, '#ffa500', (255, 165, 0), (0, 165, 255))
    orangered             = ( 99, '#ff4500', (255, 69, 0), (0, 69, 255))
    orchid                = (100, '#da70d6', (218, 112, 214), (214, 112, 218))
    palegoldenrod         = (101, '#eee8aa', (238, 232, 170), (170, 232, 238))
    palegreen             = (102, '#98fb98', (152, 251, 152), (152, 251, 152))
    paleturquoise         = (103, '#afeeee', (175, 238, 238), (238, 238, 175))
    palevioletred         = (104, '#db7093', (219, 112, 147), (147, 112, 219))
    papayawhip            = (105, '#ffefd5', (255, 239, 213), (213, 239, 255))
    peachpuff             = (106, '#ffdab9', (255, 218, 185), (185, 218, 255))
    peru                  = (107, '#cd853f', (205, 133, 63), (63, 133, 205))
    pink                  = (108, '#ffc0cb', (255, 192, 203), (203, 192, 255))
    plum                  = (109, '#dda0dd', (221, 160, 221), (221, 160, 221))
    powderblue            = (110, '#b0e0e6', (176, 224, 230), (230, 224, 176))
    purple                = (111, '#800080', (128, 0, 128), (128, 0, 128))
    red                   = (112, '#ff0000', (255, 0, 0), (0, 0, 255))
    r                     = (112, '#ff0000', (255, 0, 0), (0, 0, 255))
    rosybrown             = (113, '#bc8f8f', (188, 143, 143), (143, 143, 188))
    royalblue             = (114, '#4169e1', (65, 105, 225), (225, 105, 65))
    saddlebrown           = (115, '#8b4513', (139, 69, 19), (19, 69, 139))
    salmon                = (116, '#fa8072', (250, 128, 114), (114, 128, 250))
    sandybrown            = (117, '#f4a460', (244, 164, 96), (96, 164, 244))
    seagreen              = (118, '#2e8b57', (46, 139, 87), (87, 139, 46))
    seashell              = (119, '#fff5ee', (255, 245, 238), (238, 245, 255))
    sienna                = (120, '#a0522d', (160, 82, 45), (45, 82, 160))
    silver                = (121, '#c0c0c0', (192, 192, 192), (192, 192, 192))
    skyblue               = (122, '#87ceeb', (135, 206, 235), (235, 206, 135))
    slateblue             = (123, '#6a5acd', (106, 90, 205), (205, 90, 106))
    slategray             = (124, '#708090', (112, 128, 144), (144, 128, 112))
    snow                  = (125, '#fffafa', (255, 250, 250), (250, 250, 255))
    springgreen           = (126, '#00ff7f', (0, 255, 127), (127, 255, 0))
    steelblue             = (127, '#4682b4', (70, 130, 180), (180, 130, 70))
    tan                   = (128, '#d2b48c', (210, 180, 140), (140, 180, 210))
    teal                  = (129, '#008080', (0, 128, 128), (128, 128, 0))
    thistle               = (130, '#d8bfd8', (216, 191, 216), (216, 191, 216))
    tomato                = (131, '#ff6347', (255, 99, 71), (71, 99, 255))
    turquoise             = (132, '#40e0d0', (64, 224, 208), (208, 224, 64))
    violet                = (133, '#ee82ee', (238, 130, 238), (238, 130, 238))
    wheat                 = (134, '#f5deb3', (245, 222, 179), (179, 222, 245))
    white                 = (135, '#ffffff', (255, 255, 255), (255, 255, 255))
    w                     = (135, '#ffffff', (255, 255, 255), (255, 255, 255))
    whitesmoke            = (136, '#f5f5f5', (245, 245, 245), (245, 245, 245))
    yellow                = (137, '#ffff00', (255, 255, 0), (0, 255, 255))
    y                     = (137, '#ffff00', (255, 255, 0), (0, 255, 255))

    def __init__(self, value, hex_code, rgb, bgr):
        self._value_ = value
        self._hex_code = hex_code
        self._rgb = rgb
        self._bgr = bgr
    
    @property
    def hex(self):
        return self._hex_code
    
    @property
    def rgb(self):
        return self._rgb
                            
    @property
    def bgr(self):
        return self._bgr
    
    @property
    def __contains__(cls, other):
        return other in cls.available

# %% ../nbs/00_color.ipynb 11
# def rgb2hex(*rgb) -> str:
#     return '#{0:x}{1:x}{2:x}'.format(*rgb)


def rgb2hex(r: int, g: int, b: int) -> str:
    '''
    convert rgb color to hex
    
    Examples
    --------
    >>> rgb = (255, 255, 255)
    >>> rgb2hex(*rgb)
    >>> '#ffffff'
    >>> rgb2hex(43, 159, 225)
    >>> '#2b9fe1'
    '''
    return f'#{r:x}{g:x}{b:x}'

def hex2rgb(h: str) -> tuple:
    '''
    convert hex color to rgb tuple
    
    Examples
    --------
    >>> hex2rgb('#ffffff')
    >>> (255, 255, 255)
    >>> hex2rgb('#1af1eb')
    >>> (26, 241, 235)
    '''    
    return tuple(int(h[2*i+1:2*i+3], base=16) for i in range(3))

import sys, ctypes, atexit

_platform = sys.platform
_hdc = None
_pixel_data = None
_context = None
_draw_rect = None
_CG = None

def get_position():
    if _platform == 'win32':
        import ctypes.wintypes
        pt = ctypes.wintypes.POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
        return pt.x, pt.y
    elif _platform == 'darwin':
        event = _CG.CGEventCreate(None)
        loc = _CG.CGEventGetLocation(event)
        return int(loc.x), int(loc.y)

def get_color(x, y):
    if _platform == 'win32':
        color_ref = ctypes.windll.gdi32.GetPixel(_hdc, x, y)
        return (color_ref & 0xFF, (color_ref >> 8) & 0xFF, (color_ref >> 16) & 0xFF)
    elif _platform == 'darwin':
        with objc.autorelease_pool():
            image_ref = _CG.CGWindowListCreateImage(_CG.CGRectMake(x, y, 1, 1), 1, 0, 0)
            _CG.CGContextDrawImage(_context, _draw_rect, image_ref)
            return (_pixel_data[0], _pixel_data[1], _pixel_data[2])

def get_position_and_color():
    x, y = get_position()
    return (x, y), get_color(x, y)
    
if _platform == 'win32':
    import ctypes.wintypes
    _hdc = ctypes.windll.user32.GetDC(0)
    atexit.register(lambda: ctypes.windll.user32.ReleaseDC(0, _hdc) if _hdc else None)
elif _platform == 'darwin':
    import AppKit, objc
    import Quartz.CoreGraphics as CG
    _CG = CG
    srgb_space = AppKit.NSColorSpace.sRGBColorSpace().CGColorSpace()
    bitmap_info = CG.kCGImageAlphaPremultipliedLast | CG.kCGBitmapByteOrder32Big
    _pixel_data = (ctypes.c_ubyte * 4)()
    _context = CG.CGBitmapContextCreate(_pixel_data, 1, 1, 8, 4, srgb_space, bitmap_info)
    _draw_rect = CG.CGRectMake(0, 0, 1, 1)
else:
    raise NotImplementedError('Only Windows and macOS are supported')
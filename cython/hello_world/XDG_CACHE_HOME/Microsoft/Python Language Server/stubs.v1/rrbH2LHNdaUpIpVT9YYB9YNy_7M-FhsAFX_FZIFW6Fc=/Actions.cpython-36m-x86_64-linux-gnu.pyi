import builtins as _mod_builtins

class Action(_mod_builtins.object):
    __class__ = Action
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def same_as(self, other):
        pass
    

class Begin(Action):
    '\n    Begin(state_name) is a Plex action which causes the Scanner to\n    enter the state |state_name|. See the docstring of Plex.Lexicon\n    for more information.\n    '
    __class__ = Begin
    def __init__(self, *args, **kwargs):
        '\n    Begin(state_name) is a Plex action which causes the Scanner to\n    enter the state |state_name|. See the docstring of Plex.Lexicon\n    for more information.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def same_as(self, other):
        pass
    

class Call(Action):
    '\n    Internal Plex action which causes a function to be called.\n    '
    __class__ = Call
    def __init__(self, *args, **kwargs):
        '\n    Internal Plex action which causes a function to be called.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def same_as(self, other):
        pass
    

IGNORE = Ignore()
class Ignore(Action):
    '\n    IGNORE is a Plex action which causes its associated token\n    to be ignored. See the docstring of Plex.Lexicon  for more\n    information.\n    '
    __class__ = Ignore
    def __init__(self, *args, **kwargs):
        '\n    IGNORE is a Plex action which causes its associated token\n    to be ignored. See the docstring of Plex.Lexicon  for more\n    information.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Return(Action):
    '\n    Internal Plex action which causes |value| to\n    be returned as the value of the associated token\n    '
    __class__ = Return
    def __init__(self, *args, **kwargs):
        '\n    Internal Plex action which causes |value| to\n    be returned as the value of the associated token\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def same_as(self, other):
        pass
    

TEXT = Text()
class Text(Action):
    '\n    TEXT is a Plex action which causes the text of a token to\n    be returned as the value of the token. See the docstring of\n    Plex.Lexicon  for more information.\n    '
    __class__ = Text
    def __init__(self, *args, **kwargs):
        '\n    TEXT is a Plex action which causes the text of a token to\n    be returned as the value of the token. See the docstring of\n    Plex.Lexicon  for more information.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/huy/.local/lib/python3.6/site-packages/Cython/Plex/Actions.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'Cython.Plex.Actions'
__package__ = 'Cython.Plex'
__test__ = _mod_builtins.dict()

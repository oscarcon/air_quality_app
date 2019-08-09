import Cython.Tempita._looper as _mod_Cython_Tempita__looper
import _io as _mod__io
import _sre as _mod__sre
import builtins as _mod_builtins

def Empty(self, *args, **kw):
    pass

class HTMLTemplate(Template):
    __class__ = HTMLTemplate
    __dict__ = {}
    def __init__(self, content, name, namespace, stacklevel, get_template, default_inherit, line_offset, delimeters):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _repr(self, value, pos):
        pass
    
    default_namespace = _mod_builtins.dict()
    def from_filename(self, cls, filename, namespace, encoding, default_inherit, get_template):
        pass
    

StringIO = _mod__io.StringIO
class Template(_mod_builtins.object):
    __class__ = Template
    __dict__ = {}
    def __init__(self, content, name, namespace, stacklevel, get_template, default_inherit, line_offset, delimeters):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Tempita._tempita'
    def __repr__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def _add_line_info(self, msg, pos):
        pass
    
    def _eval(self, code, ns, pos):
        pass
    
    def _exec(self, code, ns, pos):
        pass
    
    def _interpret(self, ns):
        pass
    
    def _interpret_code(self, code, ns, out, defs):
        pass
    
    def _interpret_codes(self, codes, ns, out, defs):
        pass
    
    def _interpret_for(self, vars, expr, content, ns, out, defs):
        pass
    
    def _interpret_if(self, parts, ns, out, defs):
        pass
    
    def _interpret_inherit(self, body, defs, inherit_template, ns):
        pass
    
    def _repr(self, value, pos):
        pass
    
    default_encoding = 'utf8'
    default_inherit = None
    default_namespace = _mod_builtins.dict()
    def from_filename(self, cls, filename, namespace, encoding, default_inherit, get_template):
        pass
    
    def substitute(self, *args, **kw):
        pass
    

class TemplateDef(_mod_builtins.object):
    def __call__(self, *args, **kw):
        pass
    
    __class__ = TemplateDef
    __dict__ = {}
    def __get__(self, obj, type):
        return TemplateDef()
    
    def __init__(self, template, func_name, func_signature, body, ns, pos, bound_self):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Tempita._tempita'
    def __repr__(self):
        return ''
    
    def __str__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def _parse_signature(self, args, kw):
        pass
    

class TemplateError(_mod_builtins.Exception):
    'Exception raised while parsing a template\n    '
    __class__ = TemplateError
    __dict__ = {}
    def __init__(self, message, position, name):
        'Exception raised while parsing a template\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Tempita._tempita'
    def __str__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class TemplateObject(_mod_builtins.object):
    __class__ = TemplateObject
    __dict__ = {}
    def __init__(self, name):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Tempita._tempita'
    def __repr__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class TemplateObjectGetter(_mod_builtins.object):
    __class__ = TemplateObjectGetter
    __dict__ = {}
    def __getattr__(self, attr):
        pass
    
    def __init__(self, template_obj):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Tempita._tempita'
    def __repr__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class _TemplateBreak(_mod_builtins.Exception):
    __class__ = _TemplateBreak
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Tempita._tempita'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class _TemplateContinue(_mod_builtins.Exception):
    __class__ = _TemplateContinue
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Tempita._tempita'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = "\nA small templating language\n\nThis implements a small templating language.  This language implements\nif/elif/else, for/continue/break, expressions, and blocks of Python\ncode.  The syntax is::\n\n  {{any expression (function calls etc)}}\n  {{any expression | filter}}\n  {{for x in y}}...{{endfor}}\n  {{if x}}x{{elif y}}y{{else}}z{{endif}}\n  {{py:x=1}}\n  {{py:\n  def foo(bar):\n      return 'baz'\n  }}\n  {{default var = default_value}}\n  {{# comment}}\n\nYou use this with the ``Template`` class or the ``sub`` shortcut.\nThe ``Template`` class takes the template string and the name of\nthe template (for errors) and a default namespace.  Then (like\n``string.Template``) you can call the ``tmpl.substitute(**kw)``\nmethod to make a substitution (or ``tmpl.substitute(a_dict)``).\n\n``sub(content, **kw)`` substitutes the template immediately.  You\ncan use ``__name='tmpl.html'`` to set the name of the template.\n\nIf there are syntax errors ``TemplateError`` will be raised.\n"
__file__ = '/home/huy/.local/lib/python3.6/site-packages/Cython/Tempita/_tempita.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'Cython.Tempita._tempita'
__package__ = 'Cython.Tempita'
__test__ = _mod_builtins.dict()
_fill_command_usage = '%prog [OPTIONS] TEMPLATE arg=value\n\nUse py:arg=value to set a Python value; otherwise all values are\nstrings.\n'
def attr(**kw):
    pass

basestring_ = _mod_builtins.tuple()
class bunch(_mod_builtins.dict):
    __class__ = bunch
    __dict__ = {}
    def __getattr__(self, name):
        pass
    
    def __getitem__(self, key):
        pass
    
    def __init__(self, **kw):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Tempita._tempita'
    def __repr__(self):
        return ''
    
    def __setattr__(self, name, value):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def fromkeys(cls, type, iterable, value):
        'Returns a new dict with keys from iterable and values equal to value.'
        pass
    

bytes = _mod_builtins.bytes
def coerce_text(v):
    pass

def fill_command(args):
    pass

def find_position(string, index, last_index, last_pos):
    'Given a string and index, return (line, column)'
    pass

def get_file_template(name, from_template):
    pass

class html(_mod_builtins.object):
    __class__ = html
    __dict__ = {}
    def __html__(self):
        pass
    
    def __init__(self, value):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Tempita._tempita'
    def __repr__(self):
        return ''
    
    def __str__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def html_quote(value, force):
    pass

in_re = _mod__sre.SRE_Pattern()
def is_unicode(obj):
    pass

def isolate_expression(string, start_pos, end_pos):
    pass

lead_whitespace_re = _mod__sre.SRE_Pattern()
def lex(s, name, trim_whitespace, line_offset, delimeters):
    "\n    Lex a string into chunks:\n\n        >>> lex('hey')\n        ['hey']\n        >>> lex('hey {{you}}')\n        ['hey ', ('you', (1, 7))]\n        >>> lex('hey {{')\n        Traceback (most recent call last):\n            ...\n        TemplateError: No }} to finish last expression at line 1 column 7\n        >>> lex('hey }}')\n        Traceback (most recent call last):\n            ...\n        TemplateError: }} outside expression at line 1 column 7\n        >>> lex('hey {{ {{')\n        Traceback (most recent call last):\n            ...\n        TemplateError: {{ inside expression at line 1 column 10\n\n    "
    pass

looper = _mod_Cython_Tempita__looper.looper
def next(iterator, default=None):
    'next(iterator[, default])\n\nReturn the next item from the iterator. If default is given and the iterator\nis exhausted, it is returned instead of raising StopIteration.'
    pass

def parse(s, name, line_offset, delimeters):
    '\n    Parses a string into a kind of AST\n\n        >>> parse(\'{{x}}\')\n        [(\'expr\', (1, 3), \'x\')]\n        >>> parse(\'foo\')\n        [\'foo\']\n        >>> parse(\'{{if x}}test{{endif}}\')\n        [(\'cond\', (1, 3), (\'if\', (1, 3), \'x\', [\'test\']))]\n        >>> parse(\'series->{{for x in y}}x={{x}}{{endfor}}\')\n        [\'series->\', (\'for\', (1, 11), (\'x\',), \'y\', [\'x=\', (\'expr\', (1, 27), \'x\')])]\n        >>> parse(\'{{for x, y in z:}}{{continue}}{{endfor}}\')\n        [(\'for\', (1, 3), (\'x\', \'y\'), \'z\', [(\'continue\', (1, 21))])]\n        >>> parse(\'{{py:x=1}}\')\n        [(\'py\', (1, 3), \'x=1\')]\n        >>> parse(\'{{if x}}a{{elif y}}b{{else}}c{{endif}}\')\n        [(\'cond\', (1, 3), (\'if\', (1, 3), \'x\', [\'a\']), (\'elif\', (1, 12), \'y\', [\'b\']), (\'else\', (1, 23), None, [\'c\']))]\n\n    Some exceptions::\n\n        >>> parse(\'{{continue}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: continue outside of for loop at line 1 column 3\n        >>> parse(\'{{if x}}foo\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: No {{endif}} at line 1 column 3\n        >>> parse(\'{{else}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: else outside of an if block at line 1 column 3\n        >>> parse(\'{{if x}}{{for x in y}}{{endif}}{{endfor}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: Unexpected endif at line 1 column 25\n        >>> parse(\'{{if}}{{endif}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: if with no expression at line 1 column 3\n        >>> parse(\'{{for x y}}{{endfor}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: Bad for (no "in") in \'x y\' at line 1 column 3\n        >>> parse(\'{{py:x=1\\ny=2}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: Multi-line py blocks must start with a newline at line 1 column 3\n    '
    pass

def parse_cond(tokens, name, context):
    pass

def parse_def(tokens, name, context):
    pass

def parse_default(tokens, name, context):
    pass

def parse_expr(tokens, name, context):
    pass

def parse_for(tokens, name, context):
    pass

def parse_inherit(tokens, name, context):
    pass

def parse_one_cond(tokens, name, context):
    pass

def parse_signature(sig_text, name, pos):
    pass

def paste_script_template_renderer(content, vars, filename):
    pass

single_statements = _mod_builtins.list()
statement_re = _mod__sre.SRE_Pattern()
def sub(content, delimeters, **kw):
    pass

def sub_html(content, **kw):
    pass

trail_whitespace_re = _mod__sre.SRE_Pattern()
def trim_lex(tokens):
    "\n    Takes a lexed set of tokens, and removes whitespace when there is\n    a directive on a line by itself:\n\n       >>> tokens = lex('{{if x}}\\nx\\n{{endif}}\\ny', trim_whitespace=False)\n       >>> tokens\n       [('if x', (1, 3)), '\\nx\\n', ('endif', (3, 3)), '\\ny']\n       >>> trim_lex(tokens)\n       [('if x', (1, 3)), 'x\\n', ('endif', (3, 3)), 'y']\n    "
    pass

unicode_ = _mod_builtins.str
def url(v):
    pass

def url_quote(string, safe, encoding, errors):
    'quote(\'abc def\') -> \'abc%20def\'\n\n    Each part of a URL, e.g. the path info, the query, etc., has a\n    different set of reserved characters that must be quoted.\n\n    RFC 2396 Uniform Resource Identifiers (URI): Generic Syntax lists\n    the following reserved characters.\n\n    reserved    = ";" | "/" | "?" | ":" | "@" | "&" | "=" | "+" |\n                  "$" | ","\n\n    Each of these characters is reserved in some component of a URL,\n    but not necessarily in all of them.\n\n    By default, the quote function is intended for quoting the path\n    section of a URL.  Thus, it will not encode \'/\'.  This character\n    is reserved, but in typical usage the quote function is being\n    called on a path where the existing slash characters are used as\n    reserved characters.\n\n    string and safe may be either str or bytes objects. encoding and errors\n    must not be specified if string is a bytes object.\n\n    The optional encoding and errors parameters specify how to deal with\n    non-ASCII characters, as accepted by the str.encode method.\n    By default, encoding=\'utf-8\' (characters are encoded with UTF-8), and\n    errors=\'strict\' (unsupported characters raise a UnicodeEncodeError).\n    '
    pass

var_re = _mod__sre.SRE_Pattern()

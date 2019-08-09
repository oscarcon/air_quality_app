import builtins as _mod_builtins

class CythonTransform(VisitorTransform):
    '\n    Certain common conventions and utilities for Cython transforms.\n\n     - Sets up the context of the pipeline in self.context\n     - Tracks directives in effect in self.current_directives\n    '
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    
    __class__ = CythonTransform
    def __init__(self, *args, **kwargs):
        '\n    Certain common conventions and utilities for Cython transforms.\n\n     - Sets up the context of the pipeline in self.context\n     - Tracks directives in effect in self.current_directives\n    '
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
    
    @property
    def context(self):
        pass
    
    @property
    def current_directives(self):
        pass
    
    def visit_CompilerDirectivesNode(self, node):
        pass
    
    def visit_Node(self, node):
        pass
    

class EnvTransform(CythonTransform):
    '\n    This transformation keeps a stack of the environments.\n    '
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    
    __class__ = EnvTransform
    def __init__(self, *args, **kwargs):
        '\n    This transformation keeps a stack of the environments.\n    '
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
    
    def current_env(self):
        pass
    
    def current_scope_node(self):
        pass
    
    def enter_scope(self, node, scope):
        pass
    
    @property
    def env_stack(self):
        pass
    
    def exit_scope(self):
        pass
    
    def global_scope(self):
        pass
    
    def visit_CArgDeclNode(self, node):
        pass
    
    def visit_CStructOrUnionDefNode(self, node):
        pass
    
    def visit_ClassDefNode(self, node):
        pass
    
    def visit_FuncDefNode(self, node):
        pass
    
    def visit_GeneratorBodyDefNode(self, node):
        pass
    
    def visit_ScopedExprNode(self, node):
        pass
    

class MethodDispatcherTransform(EnvTransform):
    '\n    Base class for transformations that want to intercept on specific\n    builtin functions or methods of builtin types, including special\n    methods triggered by Python operators.  Must run after declaration\n    analysis when entries were assigned.\n\n    Naming pattern for handler methods is as follows:\n\n    * builtin functions: _handle_(general|simple|any)_function_NAME\n\n    * builtin methods: _handle_(general|simple|any)_method_TYPENAME_METHODNAME\n    '
    __class__ = MethodDispatcherTransform
    def __init__(self, *args, **kwargs):
        '\n    Base class for transformations that want to intercept on specific\n    builtin functions or methods of builtin types, including special\n    methods triggered by Python operators.  Must run after declaration\n    analysis when entries were assigned.\n\n    Naming pattern for handler methods is as follows:\n\n    * builtin functions: _handle_(general|simple|any)_function_NAME\n\n    * builtin methods: _handle_(general|simple|any)_method_TYPENAME_METHODNAME\n    '
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
    
    def _handle_function(self, node, function_name, function, arg_list, kwargs):
        'Fallback handler'
        pass
    
    def _handle_method(self, node, type_name, attr_name, function, arg_list, is_unbound_method, kwargs):
        'Fallback handler'
        pass
    
    def visit_BinopNode(self, node):
        pass
    
    def visit_GeneralCallNode(self, node):
        pass
    
    def visit_PrimaryCmpNode(self, node):
        pass
    
    def visit_SimpleCallNode(self, node):
        pass
    
    def visit_UnopNode(self, node):
        pass
    

class NodeFinder(TreeVisitor):
    '\n    Find out if a node appears in a subtree.\n    '
    __class__ = NodeFinder
    def __init__(self, *args, **kwargs):
        '\n    Find out if a node appears in a subtree.\n    '
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
    
    @property
    def found(self):
        pass
    
    def visit_Node(self, node):
        pass
    

class NodeRefCleanupMixin(_mod_builtins.object):
    '\n    Clean up references to nodes that were replaced.\n\n    NOTE: this implementation assumes that the replacement is\n    done first, before hitting any further references during\n    normal tree traversal.  This needs to be arranged by calling\n    "self.visitchildren()" at a proper place in the transform\n    and by ordering the "child_attrs" of nodes appropriately.\n    '
    __class__ = NodeRefCleanupMixin
    __dict__ = {}
    def __init__(self, *args):
        '\n    Clean up references to nodes that were replaced.\n\n    NOTE: this implementation assumes that the replacement is\n    done first, before hitting any further references during\n    normal tree traversal.  This needs to be arranged by calling\n    "self.visitchildren()" at a proper place in the transform\n    and by ordering the "child_attrs" of nodes appropriately.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Compiler.Visitor'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def replace(self, node, replacement):
        pass
    
    def visit_CloneNode(self, node):
        pass
    
    def visit_ResultRefNode(self, node):
        pass
    

class PrintTree(TreeVisitor):
    'Prints a representation of the tree to standard output.\n    Subclass and override repr_of to provide more information\n    about nodes. '
    def __call__(self, tree, phase):
        pass
    
    __class__ = PrintTree
    __dict__ = {}
    def __init__(self, start, end):
        'Prints a representation of the tree to standard output.\n    Subclass and override repr_of to provide more information\n    about nodes. '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def _print_node(self, node):
        pass
    
    def indent(self):
        pass
    
    def repr_of(self, node):
        pass
    
    def unindent(self):
        pass
    
    def visit_CloneNode(self, node):
        pass
    
    def visit_Node(self, node):
        pass
    

class RecursiveNodeReplacer(VisitorTransform):
    '\n    Recursively replace all occurrences of a node in a subtree by\n    another node.\n    '
    __class__ = RecursiveNodeReplacer
    def __init__(self, *args, **kwargs):
        '\n    Recursively replace all occurrences of a node in a subtree by\n    another node.\n    '
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
    
    @property
    def new_node(self):
        pass
    
    @property
    def orig_node(self):
        pass
    
    def visit_CloneNode(self, node):
        pass
    
    def visit_Node(self, node):
        pass
    

class ScopeTrackingTransform(CythonTransform):
    __class__ = ScopeTrackingTransform
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
    
    @property
    def scope_node(self):
        pass
    
    @property
    def scope_type(self):
        pass
    
    def visit_CClassDefNode(self, node):
        pass
    
    def visit_CStructOrUnionDefNode(self, node):
        pass
    
    def visit_FuncDefNode(self, node):
        pass
    
    def visit_ModuleNode(self, node):
        pass
    
    def visit_PyClassDefNode(self, node):
        pass
    

class TreeVisitor(_mod_builtins.object):
    '\n    Base class for writing visitors for a Cython tree, contains utilities for\n    recursing such trees using visitors. Each node is\n    expected to have a child_attrs iterable containing the names of attributes\n    containing child nodes or lists of child nodes. Lists are not considered\n    part of the tree structure (i.e. contained nodes are considered direct\n    children of the parent node).\n\n    visit_children visits each of the children of a given node (see the visit_children\n    documentation). When recursing the tree using visit_children, an attribute\n    access_path is maintained which gives information about the current location\n    in the tree as a stack of tuples: (parent_node, attrname, index), representing\n    the node, attribute and optional list index that was taken in each step in the path to\n    the current node.\n\n    Example:\n\n    >>> class SampleNode(object):\n    ...     child_attrs = ["head", "body"]\n    ...     def __init__(self, value, head=None, body=None):\n    ...         self.value = value\n    ...         self.head = head\n    ...         self.body = body\n    ...     def __repr__(self): return "SampleNode(%s)" % self.value\n    ...\n    >>> tree = SampleNode(0, SampleNode(1), [SampleNode(2), SampleNode(3)])\n    >>> class MyVisitor(TreeVisitor):\n    ...     def visit_SampleNode(self, node):\n    ...         print("in %s %s" % (node.value, self.access_path))\n    ...         self.visitchildren(node)\n    ...         print("out %s" % node.value)\n    ...\n    >>> MyVisitor().visit(tree)\n    in 0 []\n    in 1 [(SampleNode(0), \'head\', None)]\n    out 1\n    in 2 [(SampleNode(0), \'body\', 0)]\n    out 2\n    in 3 [(SampleNode(0), \'body\', 1)]\n    out 3\n    out 0\n    '
    __class__ = TreeVisitor
    def __init__(self, *args, **kwargs):
        '\n    Base class for writing visitors for a Cython tree, contains utilities for\n    recursing such trees using visitors. Each node is\n    expected to have a child_attrs iterable containing the names of attributes\n    containing child nodes or lists of child nodes. Lists are not considered\n    part of the tree structure (i.e. contained nodes are considered direct\n    children of the parent node).\n\n    visit_children visits each of the children of a given node (see the visit_children\n    documentation). When recursing the tree using visit_children, an attribute\n    access_path is maintained which gives information about the current location\n    in the tree as a stack of tuples: (parent_node, attrname, index), representing\n    the node, attribute and optional list index that was taken in each step in the path to\n    the current node.\n\n    Example:\n\n    >>> class SampleNode(object):\n    ...     child_attrs = ["head", "body"]\n    ...     def __init__(self, value, head=None, body=None):\n    ...         self.value = value\n    ...         self.head = head\n    ...         self.body = body\n    ...     def __repr__(self): return "SampleNode(%s)" % self.value\n    ...\n    >>> tree = SampleNode(0, SampleNode(1), [SampleNode(2), SampleNode(3)])\n    >>> class MyVisitor(TreeVisitor):\n    ...     def visit_SampleNode(self, node):\n    ...         print("in %s %s" % (node.value, self.access_path))\n    ...         self.visitchildren(node)\n    ...         print("out %s" % node.value)\n    ...\n    >>> MyVisitor().visit(tree)\n    in 0 []\n    in 1 [(SampleNode(0), \'head\', None)]\n    out 1\n    in 2 [(SampleNode(0), \'body\', 0)]\n    out 2\n    in 3 [(SampleNode(0), \'body\', 1)]\n    out 3\n    out 0\n    '
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
    
    def _find_node_path(self, stacktrace):
        pass
    
    @property
    def access_path(self):
        pass
    
    def dump_node(self, node):
        pass
    
    def visit(self, obj):
        pass
    
    def visitchildren(self, parent, attrs):
        pass
    

class VisitorTransform(TreeVisitor):
    '\n    A tree transform is a base class for visitors that wants to do stream\n    processing of the structure (rather than attributes etc.) of a tree.\n\n    It implements __call__ to simply visit the argument node.\n\n    It requires the visitor methods to return the nodes which should take\n    the place of the visited node in the result tree (which can be the same\n    or one or more replacement). Specifically, if the return value from\n    a visitor method is:\n\n    - [] or None; the visited node will be removed (set to None if an attribute and\n    removed if in a list)\n    - A single node; the visited node will be replaced by the returned node.\n    - A list of nodes; the visited nodes will be replaced by all the nodes in the\n    list. This will only work if the node was already a member of a list; if it\n    was not, an exception will be raised. (Typically you want to ensure that you\n    are within a StatListNode or similar before doing this.)\n    '
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    
    __class__ = VisitorTransform
    def __init__(self, *args, **kwargs):
        '\n    A tree transform is a base class for visitors that wants to do stream\n    processing of the structure (rather than attributes etc.) of a tree.\n\n    It implements __call__ to simply visit the argument node.\n\n    It requires the visitor methods to return the nodes which should take\n    the place of the visited node in the result tree (which can be the same\n    or one or more replacement). Specifically, if the return value from\n    a visitor method is:\n\n    - [] or None; the visited node will be removed (set to None if an attribute and\n    removed if in a list)\n    - A single node; the visited node will be replaced by the returned node.\n    - A list of nodes; the visited nodes will be replaced by all the nodes in the\n    list. This will only work if the node was already a member of a list; if it\n    was not, an exception will be raised. (Typically you want to ensure that you\n    are within a StatListNode or similar before doing this.)\n    '
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
    
    def recurse_to_children(self, node):
        pass
    
    def visitchildren(self, parent, attrs, exclude):
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/huy/.local/lib/python3.6/site-packages/Cython/Compiler/Visitor.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'Cython.Compiler.Visitor'
__package__ = 'Cython.Compiler'
__test__ = _mod_builtins.dict()
def find_special_method_for_binary_operator():
    'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
    pass

def find_special_method_for_unary_operator():
    'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
    pass

def recursively_replace_node(tree, old_node, new_node):
    pass

def replace_node(ptr, value):
    'Replaces a node. ptr is of the form used on the access path stack\n    (parent, attrname, listidx|None)\n    '
    pass

def tree_contains(tree, node):
    pass


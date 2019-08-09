import Cython.Compiler.ExprNodes as _mod_Cython_Compiler_ExprNodes
import Cython.Compiler.Nodes as _mod_Cython_Compiler_Nodes
import Cython.Utils as _mod_Cython_Utils
import builtins as _mod_builtins

CFuncDefNode = _mod_Cython_Compiler_Nodes.CFuncDefNode
CloneNode = _mod_Cython_Compiler_ExprNodes.CloneNode
DefNode = _mod_Cython_Compiler_Nodes.DefNode
FuncDefNode = _mod_Cython_Compiler_Nodes.FuncDefNode
class FusedCFuncDefNode(_mod_Cython_Compiler_Nodes.StatListNode):
    "\n    This node replaces a function with fused arguments. It deep-copies the\n    function for every permutation of fused types, and allocates a new local\n    scope for it. It keeps track of the original function in self.node, and\n    the entry of the original function in the symbol table is given the\n    'fused_cfunction' attribute which points back to us.\n    Then when a function lookup occurs (to e.g. call it), the call can be\n    dispatched to the right function.\n\n    node    FuncDefNode    the original function\n    nodes   [FuncDefNode]  list of copies of node with different specific types\n    py_func DefNode        the fused python function subscriptable from\n                           Python space\n    __signatures__         A DictNode mapping signature specialization strings\n                           to PyCFunction nodes\n    resulting_fused_function  PyCFunction for the fused DefNode that delegates\n                              to specializations\n    fused_func_assignment   Assignment of the fused function to the function name\n    defaults_tuple          TupleNode of defaults (letting PyCFunctionNode build\n                            defaults would result in many different tuples)\n    specialized_pycfuncs    List of synthesized pycfunction nodes for the\n                            specializations\n    code_object             CodeObjectNode shared by all specializations and the\n                            fused function\n\n    fused_compound_types    All fused (compound) types (e.g. floating[:])\n    "
    __class__ = FusedCFuncDefNode
    __dict__ = {}
    def __init__(self, node, env):
        "\n    This node replaces a function with fused arguments. It deep-copies the\n    function for every permutation of fused types, and allocates a new local\n    scope for it. It keeps track of the original function in self.node, and\n    the entry of the original function in the symbol table is given the\n    'fused_cfunction' attribute which points back to us.\n    Then when a function lookup occurs (to e.g. call it), the call can be\n    dispatched to the right function.\n\n    node    FuncDefNode    the original function\n    nodes   [FuncDefNode]  list of copies of node with different specific types\n    py_func DefNode        the fused python function subscriptable from\n                           Python space\n    __signatures__         A DictNode mapping signature specialization strings\n                           to PyCFunction nodes\n    resulting_fused_function  PyCFunction for the fused DefNode that delegates\n                              to specializations\n    fused_func_assignment   Assignment of the fused function to the function name\n    defaults_tuple          TupleNode of defaults (letting PyCFunctionNode build\n                            defaults would result in many different tuples)\n    specialized_pycfuncs    List of synthesized pycfunction nodes for the\n                            specializations\n    code_object             CodeObjectNode shared by all specializations and the\n                            fused function\n\n    fused_compound_types    All fused (compound) types (e.g. floating[:])\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Compiler.FusedNode'
    __signatures__ = None
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _buffer_check_numpy_dtype(self, pyx_code, specialized_buffer_types, pythran_types):
        '\n        Match a numpy dtype object to the individual specializations.\n        '
        pass
    
    def _buffer_check_numpy_dtype_setup_cases(self, pyx_code):
        'Setup some common cases to match dtypes against specializations'
        pass
    
    def _buffer_checks(self, buffer_types, pythran_types, pyx_code, decl_code, env):
        '\n        Generate Cython code to match objects to buffer specializations.\n        First try to get a numpy dtype object and match it against the individual\n        specializations. If that fails, try naively to coerce the object\n        to each specialization, which obtains the buffer each time and tries\n        to match the format string.\n        '
        pass
    
    def _buffer_declarations(self, pyx_code, decl_code, all_buffer_types, pythran_types):
        '\n        If we have any buffer specializations, write out some variable\n        declarations and imports.\n        '
        pass
    
    def _buffer_parse_format_string_check(self, pyx_code, decl_code, specialized_type, env):
        '\n        For each specialized type, try to coerce the object to a memoryview\n        slice of that type. This means obtaining a buffer and parsing the\n        format string.\n        TODO: separate buffer acquisition from format parsing\n        '
        pass
    
    def _dtype_name(self, dtype):
        pass
    
    def _dtype_type(self, dtype):
        pass
    
    def _fused_instance_checks(self, normal_types, pyx_code, env):
        '\n        Generate Cython code for instance checks, matching an object to\n        specialized types.\n        '
        pass
    
    def _get_fused_base_types(self, fused_compound_types):
        '\n        Get a list of unique basic fused types, from a list of\n        (possibly) compound fused types.\n        '
        pass
    
    def _sizeof_dtype(self, dtype):
        pass
    
    def _specialize_function_args(self, args, fused_to_specific):
        pass
    
    def _split_fused_types(self, arg):
        '\n        Specialize fused types and split into normal types and buffer types.\n        '
        pass
    
    def _unpack_argument(self, pyx_code):
        pass
    
    def analyse_expressions(self, env):
        '\n        Analyse the expressions. Take care to only evaluate default arguments\n        once and clone the result for all specializations\n        '
        pass
    
    def annotate(self, code):
        pass
    
    child_attrs = _mod_builtins.list()
    def copy_cdef(self, env):
        '\n        Create a copy of the original c(p)def function for all specialized\n        versions.\n        '
        pass
    
    def copy_def(self, env):
        '\n        Create a copy of the original def or lambda function for specialized\n        versions.\n        '
        pass
    
    def create_new_local_scope(self, node, env, f2s):
        '\n        Create a new local scope for the copied node and append it to\n        self.nodes. A new local scope is needed because the arguments with the\n        fused types are already in the local scope, and we need the specialized\n        entries created after analyse_declarations on each specialized version\n        of the (CFunc)DefNode.\n        f2s is a dict mapping each fused type to its specialized version\n        '
        pass
    
    decorators = None
    defaults_tuple = None
    fused_func_assignment = None
    def generate_execution_code(self, code):
        pass
    
    def generate_function_definitions(self, env, code):
        pass
    
    def make_fused_cpdef(self, orig_py_func, env, is_def):
        "\n        This creates the function that is indexable from Python and does\n        runtime dispatch based on the argument types. The function gets the\n        arg tuple and kwargs dict (or None) and the defaults tuple\n        as arguments from the Binding Fused Function's tp_call.\n        "
        pass
    
    match = "dest_sig[{{dest_sig_idx}}] = '{{specialized_type_name}}'"
    no_match = 'dest_sig[{{dest_sig_idx}}] = None'
    def replace_fused_typechecks(self, copied_node):
        '\n        Branch-prune fused type checks like\n\n            if fused_t is int:\n                ...\n\n        Returns whether an error was issued and whether we should stop in\n        in order to prevent a flood of errors.\n        '
        pass
    
    resulting_fused_function = None
    def specialize_copied_def(self, node, cname, py_entry, f2s, fused_compound_types):
        'Specialize the copy of a DefNode given the copied node,\n        the specialization cname and the original DefNode entry'
        pass
    
    def synthesize_defnodes(self):
        '\n        Create the __signatures__ dict of PyCFunctionNode specializations.\n        '
        pass
    
    def update_fused_defnode_entry(self, env):
        pass
    

OrderedSet = _mod_Cython_Utils.OrderedSet
ProxyNode = _mod_Cython_Compiler_ExprNodes.ProxyNode
StatListNode = _mod_Cython_Compiler_Nodes.StatListNode
TupleNode = _mod_Cython_Compiler_ExprNodes.TupleNode
__builtins__ = {}
__doc__ = None
__file__ = '/home/huy/.local/lib/python3.6/site-packages/Cython/Compiler/FusedNode.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'Cython.Compiler.FusedNode'
__package__ = 'Cython.Compiler'
__test__ = _mod_builtins.dict()

import sys, ctypes
from pathlib import Path
from ctypes import c_uint32, CFUNCTYPE, Structure, POINTER

# extension is .so for linux, .dylib for OSX and .dll for windows
extension = {'darwin': '.dylib', 'win32': '.dll'}.get(sys.platform, '.so') 
# add prefix lib to all but windows
prefix = {'win32': ''}.get(sys.platform, 'lib') 
# You can change 'debug' => 'release' if you do Cargo build --release
lib_name = Path(Path(__file__).parent.parent, 'target', 'debug', prefix + "callback" + extension).resolve()

print(f"loading {lib_name}", flush=True)

lib = ctypes.cdll.LoadLibrary(lib_name)  # Load the library

CBFUNC = CFUNCTYPE(None, c_uint32)

class PTicker(Structure):
    pass

lib.ticker_new.argtypes = (c_uint32,)
lib.ticker_new.restype = POINTER(PTicker)
lib.ticker_free.argtypes = (POINTER(PTicker), )
lib.ticker_set_callback.argtypes = (POINTER(PTicker), CBFUNC)

class PTicker:
    def __init__(self, limit=2):
        self.obj = lib.ticker_new(limit)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        lib.ticker_free(self.obj)

    def set_callback(self, callback):
        cb = CBFUNC(callback)
        print(f"PTicker.set_callback callback: {callback}, cb: {cb}")
        lib.ticker_set_callback(self.obj, cb)

    def tick(self):
        lib.ticker_tick(self.obj)


def msg(x):
    print(f"Alert: {x} ticks!")

with PTicker(2) as ticker:
    ticker.tick()
    ticker.tick()
    ticker.set_callback(msg)
    ticker.tick()
    ticker.tick()
    ticker.tick()
    ticker.tick()

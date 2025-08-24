# C++ function source - build from .header
cdef extern from "../cpp_src/system_info.h" namespace "sysinfo":
    int getOSname();
    int getCPUinfo();

# Python wrapping
def getOSname_py():
    return getOSname()

def getCPUinfo_py():
    return getCPUinfo()
# Import int_64 class
from libc.stdint cimport int64_t

# C++ function source - build from .header
cdef extern from "../cpp_src/system_info.h" namespace "sysinfo":
    # System Info Storage Structure
    struct SystemInfoStatic:
        int64_t totalMemoryMB
        int numCPUCores
        int OS_true_name # 0 = Linux, 1 = macOS, 2 = Unix

    # Function declarations
    int getOSname();
    SystemInfoStatic getSystemInfoStatic();

# Python wrapping
def getOSname_py():
    return getOSname()

def getSystemInfoStatic_py():
    return getSystemInfoStatic()

# TODO
# This belongs in the C++ calls
#    struct SystemInfoDynamic:
#        int64_t currentMemoryUsageMB
#        int numCPUProcesses
#        int64_t networkUsageMB
#        int OS_true_name # 0 = Linux, 1 = macOS, 2 = Unix
#    SystemInfoDynamic getSystemInfoDynamic();

# This belongs in Python wrapping
# def getSystemInfoDynamic_py():
#    return getSystemInfoDynamic()
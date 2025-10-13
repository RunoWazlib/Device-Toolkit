# Import int_64 class
from libc.stdint cimport int64_t

# C++ function source - build from .header
cdef extern from "../cpp_src/system_info.h" namespace "sysinfo":
    # System Info Storage Structure
    struct SystemInfoStatic:
        int64_t totalMemoryMB
        int numCPUCores
        int OS_true_name # 0 = Linux, 1 = macOS, 2 = Unix

    struct SystemInfoDynamic:
        int64_t currentMemoryUsageMB
        int numCPUProcesses
        int64_t networkUsageMB
        int OS_true_name # 0 = Linux, 1 = macOS, 2 = Unix

    # Function declarations
    int getOSname();
    SystemInfoStatic getSystemInfoStatic();
    SystemInfoDynamic getSystemInfoDynamic();

# Python wrapping
def getOSname_py():
    return getOSname()

def getSystemInfoStatic_py():
    return getSystemInfoStatic()

def getSystemInfoDynamic_py():
    return getSystemInfoDynamic()
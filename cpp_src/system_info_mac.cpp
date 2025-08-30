#include "system_info.h"
#include <sys/sysctl.h>

namespace sysinfo {
    SystemInfoStatic info;

    // Function to determine CPU data
    SystemInfoStatic getSystemInfoStatic() {
        // Check OS == "Darwin"
        int os = sysinfo::getOSname();
        if (os == 1) {
            //Set OS name flag
            info.OS_true_name = os;

            // Variables for sysctl calls
            int mib[2];
            size_t len;
            int64_t mem;

            // Get total physical memory
            mib[0] = CTL_HW;
            mib[1] = HW_MEMSIZE;
            len = sizeof(mem);
            sysctl(mib, 2, &mem, &len, NULL, 0);
            info.totalMemoryMB = mem / (1024 * 1024);

            // Get number of CPU cores
            int ncpu;
            mib[0] = CTL_HW;
            mib[1] = HW_NCPU;
            len = sizeof(ncpu);
            sysctl(mib, 2, &ncpu, &len, NULL, 0);
            info.numCPUCores = ncpu;
    }
        // Return struct
        return info;
    }
}
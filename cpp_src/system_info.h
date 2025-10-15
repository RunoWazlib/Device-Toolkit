#pragma once
#include <stdint.h> // For int64_t

namespace sysinfo {
    // System Info Storage
    struct SystemInfoStatic {
        int64_t totalMemoryMB;
        int numCPUCores;
        int OS_true_name; // 0 = Linux, 1 = macOS, 2 = Unix
    };

    struct SystemInfoDynamic {
        int64_t currentMemoryUsageMB;
        int numCPUProcesses;
        int64_t networkUsageMB;
        int OS_true_name; // 0 = Linux, 1 = macOS, 2 = Unix
    };
    // Function to determine what OS is on system
    int getOSname();

    // Function to determine total system resources
    SystemInfoStatic getSystemInfoStatic();

    // Function to determine current usage
    // SystemInfoDynamic getSystemInfoDynamic();
}
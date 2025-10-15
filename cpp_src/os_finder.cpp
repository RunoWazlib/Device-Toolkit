#include "system_info.h"
#include <sys/utsname.h>
// TODO: Add Windows support
// #include <windows.h>
#include <iostream>

namespace sysinfo {
    // Function to determine what OS is on system
    int getOSname() {
        struct utsname info;

        // Error handling
        if (uname(&info) == -1) {
            perror("uname");
            return -1;
        }

        uname(&info);
        std::string os_name = info.sysname;
        // Print output for debugging
        // std::cout << "Operating System: " << os_name << std::endl;

        if (os_name == "Linux") {
            return 0; // Linux
        } else if (os_name == "Darwin") {
            return 1; // macOS
        } else {
            return 2; // Unix OS
        }
    }
}
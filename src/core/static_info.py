import cpp_bindings as c

class StaticInfo: 
    def getOSname(self):
        # Determine OS name using the C++ function
        self.osDict = {0:"Linux", 1:"MacOS", 2:"Windows"}
        self.osName = self.osDict[c.getOSname_py()]
        return self.osName

    def getHardwareStats(self):
        self.hardware = c.getSystemInfoStatic_py()
        return self.hardware
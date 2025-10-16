from src.core.static_info import StaticInfo

# Generate StaticInfo instance
StaticInfoInstance = StaticInfo()
osName = StaticInfoInstance.getOSname()
hardwareStats = StaticInfoInstance.getHardwareStats()

# Outputs
print("[*] Static Information:")
print(f"operatingSystem: {osName}")
for key in hardwareStats.keys():
    print(f"{key}: {StaticInfoInstance.hardware[key]}")
# # Assess current system operations while program is running
# while True:
#     pass
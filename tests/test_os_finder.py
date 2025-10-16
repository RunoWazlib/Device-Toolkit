import pytest, os, sys
# Ensure src is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.static_info import StaticInfo
                                                
@pytest.mark.skipif(sys.platform != "linux", reason="Test only valid on Linux")
def test_getOSnameLinux():
    StaticInfoInstance = StaticInfo()
    # Get OS name
    osName = StaticInfoInstance.getOSname()
    # OS name should be Linux for this testing environment 
    assert osName == "Linux"

@pytest.mark.skipif(sys.platform != "darwin", reason="Test only valid on MacOS")
def test_getOSnameMacOS():
    StaticInfoInstance = StaticInfo()
    # Get OS name
    osName = StaticInfoInstance.getOSname()
    # OS name should be MacOS for this testing environment 
    assert osName == "MacOS"

@pytest.mark.skipif(sys.platform != "win32", reason="Test only valid on Windows")
def test_getOSnameWindows():
    StaticInfoInstance = StaticInfo()
    # Get OS name
    osName = StaticInfoInstance.getOSname()
    # OS name should be Windows for this testing environment 
    assert osName == "Windows"
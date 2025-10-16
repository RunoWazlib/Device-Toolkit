import pytest, os, sys
# Ensure src is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.static_info import StaticInfo

def test_cythonCompiled():
        try:
            import cpp_bindings
        except ImportError as e:
            assert False, f"[!] Could not import cpp_bindings: {e}"
    
def test_cppFunctions():
    import cpp_bindings as c
    assert hasattr(c, 'getOSname_py'), "[!] cpp_bindings missing getOSname_py"
    assert hasattr(c, 'getSystemInfoStatic_py'), "[!] cpp_bindings missing getSystemInfoStatic_py"

def test_getHardwareStats():
        StaticInfoInstance = StaticInfo()
        # Get hardware stats
        hardwareStats = StaticInfoInstance.getHardwareStats()
        
        # Hardware stats should be a dict
        assert isinstance(hardwareStats, dict)

        # Hardware stats should be present
        assert "totalMemoryMB" in hardwareStats, "[!] totalMemoryMB missing in hardware stats"
        assert "numCPUCores" in hardwareStats, "[!] numCPUCores missing in hardware stats"

        # These values should be greater than 0
        assert hardwareStats["totalMemoryMB"] > 0
        assert hardwareStats["numCPUCores"] > 0
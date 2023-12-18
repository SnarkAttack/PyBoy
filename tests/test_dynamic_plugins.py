from pyboy import PyBoy
from pyboy.plugins.base_plugin import PyBoyGameWrapper

class DummyGameWrapper(PyBoyGameWrapper):
    # Dummy game wrapper class

    cartridge_title = "FAKE GAME"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class DefaultRomGameWrapper(PyBoyGameWrapper):

    cartridge_title = "NO-ROM"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_cartridge_type(self):
        return self.pyboy.get_memory_value(0x147)

def test_default_plugins(default_rom):
    pyboy = PyBoy(default_rom, window_type="headless")
    # ScreenRecorder and ScreenshotRecorder enabled by default,
    # WindowHeadless enabled in PyBoy arguments
    expected_plugin_names = ['WindowHeadless', 'ScreenRecorder', 'ScreenshotRecorder']
    assert set(expected_plugin_names) == set(pyboy.plugin_manager.plugin_mapping.keys())

def test_dynamic_plugin_loading(default_rom):
    pyboy = PyBoy(default_rom, window_type="headless")
    DefaultRomGameWrapper.register(pyboy)
    wrapper = pyboy.game_wrapper()
    assert wrapper is not None
    assert len(pyboy.plugin_manager.enabled_gamewrappers) == 1

    # Check that trying to re-register plugin does not actually
    # add plugin twice

    DefaultRomGameWrapper.register(pyboy)
    assert len(pyboy.plugin_manager.enabled_gamewrappers) == 1
      
def test_dynamic_plugins_no_enable_game_wrapper(default_rom):
    # Should not enable as cartridge name won't match anything
    pyboy = PyBoy(default_rom, window_type="headless")
    DummyGameWrapper.register(pyboy)
    assert len(pyboy.plugin_manager.enabled_gamewrappers) == 0

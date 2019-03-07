import os

from conans import ConanFile, CMake, tools


class XdgutilscxxTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    options = {"fPIC": [True, False]}
    default_options = {"fPIC": True}
    generators = ["cmake", "cmake_paths"]

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self.settings):
            self.run(".%sexample" % os.sep)

from conans import ConanFile, CMake, tools


class XdgutilscxxConan(ConanFile):
    name = "xdg-utils-cxx"
    version = "0.1.1"
    license = "MIT"
    author = "Alexis Lopez Zubieta (contact at azubieta.net)"
    url = "https://github.com/azubieta/conan-xdg-utils-cxx"
    description = "Implementation of the FreeDesktop specifications to be used in c++ projects"
    topics = ("FreeDesktop", "xdg-utils", "c++")
    settings = "compiler", "build_type", "arch"
    options = {"fPIC": [True, False]}
    default_options = {"fPIC": True}
    build_requires = "cmake_installer/3.13.0@conan/stable"
    generators = ["cmake_paths"]

    def source(self):
        self.run("git clone https://github.com/azubieta/xdg-utils-cxx.git")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_PROJECT_XdgUtils_INCLUDE"] = self.build_folder + "/conan_paths.cmake"
        cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.configure(source_folder="xdg-utils-cxx")
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["XdgUtilsBaseDir", "XdgUtilsDesktopEntry"]
        self.cpp_info.builddirs = ["lib/cmake/XdgUtils/"]
        self.cpp_info.includedirs = ["include/"]

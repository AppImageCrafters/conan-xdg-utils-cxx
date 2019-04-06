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
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = ["cmake"]

    def source(self):
        self.run("git clone https://github.com/azubieta/xdg-utils-cxx.git")

    def build(self):
        cmake = CMake(self)
        args = []

        # enable fPIC
        if self.options.fPIC:
            args.append("-DPOSITION_INDEPENDENT_CODE=ON")

        cmake.configure(source_folder="xdg-utils-cxx", args=args)
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["XdgUtilsBaseDir", "XdgUtilsDesktopEntry"]

from conans import ConanFile, CMake, tools
import os


class OpensslConan(ConanFile):
    name = "OpenSSL"
    version = "1.0.2a"
    requires = "Perl_installer/1.0@Zitrax/testing"
    #license = "<Put the package license here>"
    #url = "<Package recipe repository url here, for issues about the package>"
    #settings = "os", "compiler", "build_type", "arch"
    settings = {"os": ["Windows"], "arch": ["x86_64"], "compiler": {"Visual Studio": {"version": ['15']}}}
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "visual_studio"

    def source(self):
        self.run("git -c advice.detachedHead=false clone --depth=1 -b OpenSSL_1_0_2a git://git.openssl.org/openssl.git")

    def build(self):
        self.run(r'perl Configure VC-WIN32 no-asm --prefix=c:/some/openssl/dir', cwd='openssl')
        self.run(r'ms\do_ms', cwd='openssl')
        # Note that for VS 2017 you need to set something like:
        #   set VS150COMNTOOLS=D:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\Tools\
        # manually before running this.
        vcvars = tools.vcvars_command(self.settings)
        self.run(r'{} && nmake -f ms\ntdll.mak test'.format(vcvars), cwd='openssl')
        raise Exception("Not implemented")

    def package(self):
        raise Exception("Not implemented")
        #self.copy("*.h", dst="include", src="hello")

    def package_info(self):
        raise Exception("Not implemented")
        #self.cpp_info.libs = ["hello"]

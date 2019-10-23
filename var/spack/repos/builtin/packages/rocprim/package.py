# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install rocprim
#
# You can edit this file again by typing:
#
#     spack edit rocprim
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Rocprim(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/ROCmSoftwarePlatform/rocPRIM/archive/2.9.0.tar.gz"

    version('2.9.0', sha256='9e4db3ecd344abfacde3e71f429df5f76174b2766632d07c3e487eba08553227')
    version('2.8.0', sha256='35e2120f113f0925ed9eddc7965643688d0819b585570e0afb208f994f35c8ff')
    version('2.7.2', sha256='2cf0962926bb6b74cc55b5f50c1bc1fe38edf6eb236b4157f75c29b599c8d7e6')
    version('2.7.0', sha256='d4eef33de15b3f55a99a6348ab40167c31eba38033f6f96f243fb86bfb232a3a')
    version('2.6.0', sha256='d67299749d9a356f5cbf69bea8f4db9fb86c87ea63dcc92c2440598705744df7')

    depends_on('cmake@3.5.1:', type='build')
    # FIXME: Add dependencies if required.
    # depends_on('foo')
    def install(self, spec, prefix):
        env.set('LD_LIBRARY_PATH', '/opt/rocm/lib:/opt/rocm/hcc/lib')
        # FIXME: Unknown build system
        cmake("-G \"Tests\" -D CMAKE_C_COMPILER=hcc -D CMAKE_CXX_COMPILER=hcc /opt/rocm/bin/")
        make()
        make('install')
    def cmake_args(self):
#        args = ["-DCMAKE_C_COMPILER=/opt/rocm/bin/hcc -DCMAKE_CXX_COMPILER=/opt/rocm/bin/hcc -DBUILD_BENCHMARK=OFF"]

        args = ['-DCMAKE_C_COMPILER=/opt/rocm/bin/hipcc',
                '-DCMAKE_CXX_COMPILER=/opt/rocm/bin/hipcc',
                '-DCMAKE_MODULE_PATH=/opt/rocm/lib/cmake/:/opt/rocm/:/opt/rocm/lib/:/opt/rocm/lib/cmake/amd_comgr:/opt/rocm/share/amd_comgr',
                '-DCMAKE_PREFIX_PATH=$CMAKE_PREFIX_PATH:/opt/rocm/share/amd_comgr:/opt/rocm/lib/:/opt/rocm/lib/cmake/amd_comgr/:/opt/rocm:/opt/rocm/hip/lib/cmake/:/opt/rocm/hcc:/opt/rocm/hip',
                '-DBUILD_TEST=OFF']
        #        if self.spec.satisfies("^dyninst@9.3.0:"):
        #            std.flag = self.compiler.cxx_flag
        #            args.append("-DCMAKE_CXX_FLAGS='{0}' -fpermissive'".format(
        #                std_flag))
        
        return args

                                                                    
#    def build_targets(self):
#        targets.append('COMPILER_SUITE=pgi')
#        return targets

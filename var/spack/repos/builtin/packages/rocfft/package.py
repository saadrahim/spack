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
#     spack install rocfft
#
# You can edit this file again by typing:
#
#     spack edit rocfft
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Rocfft(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/ROCmSoftwarePlatform/rocFFT/archive/rocm-2.9.tar.gz"

    version('2.9', sha256='edb21cb8861bb790eebf704ef16c6cf298d16e26f7df4d3461171af893120814')
    version('2.8', sha256='647c67bb0dcfd4a9183b798bffc9afcd81f6d30400a732af2798f7a16952f6e7')
    version('2.7', sha256='ae5002575538a4e60994b9a408ddd2284d6d8f7ea5638f42d7c921f8b7fb68cc')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ['-DCMAKE_C_COMPILER=/opt/rocm/bin/hcc',
                '-DCMAKE_CXX_COMPILER=/opt/rocm/bin/hcc',
                '-DBUILD_TEST=OFF',
                '-Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr/']

        return args

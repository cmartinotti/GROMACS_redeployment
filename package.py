# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os


class Gromacs(CMakePackage):
    """GROMACS (GROningen MAchine for Chemical Simulations) is a molecular
    dynamics package primarily designed for simulations of proteins, lipids
    and nucleic acids. It was originally developed in the Biophysical
    Chemistry department of University of Groningen, and is now ftp://ftp.gromacs.org/gromacs/gromacs-2023.tar.gzmaintained
    by contributors in universities and research centers across the world.

    GROMACS is one of the fastest and most popular software packages
    available and can run on CPUs as well as GPUs. It is free, open source
    released under the GNU General Public License. Starting from version 4.6,
    GROMACS is released under the GNU Lesser General Public License.
    """

    homepage = 'http://www.gromacs.org'
    url      = 'file://{}/gromacs.5.1.2.tar.gz'.format(os.getcwd())
    git      = 'https://github.com/gromacs/gromacs.git'
    maintainers = ['junghans', 'marvinbernhardt']
    
    depends_on('mpi')

    def cmake_args(self):

        options = ['-DGMX_BUILD_OWN_FFTW=ON','-DGMX_CPU_ACCELERATION=SSE4.1', '-DGMX_MPI=ON', '-DGMX_GPU=OFF']
        options.extend([
                    '-DCMAKE_C_COMPILER=%s' % spack_cc,
                    '-DCMAKE_CXX_COMPILER=%s' % spack_cxx,
                    '-DMPI_C_COMPILER=%s' % self.spec['mpi'].mpicc,
                    '-DMPI_CXX_COMPILER=%s' % self.spec['mpi'].mpicxx
        ])
        return options

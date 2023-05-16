FROM ubuntu:18.04

RUN apt-get update && apt-get install -y git cmake mpich

WORKDIR /opt/
RUN git clone https://github.com/CurtinIC/gromacs && mkdir gromacs/build /mnt/data
WORKDIR /opt/gromacs/build
RUN cmake -DGMX_BUILD_OWN_FFTW=ON -DGMX_MPI=ON -DGMX_GPU=OFF ../ && make -j8 && make -j8 install
ENV PATH="/usr/local/gromacs/bin:${PATH}"
WORKDIR /mnt/data

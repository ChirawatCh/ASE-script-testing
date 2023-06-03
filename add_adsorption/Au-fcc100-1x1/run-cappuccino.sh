#!/bin/bash
#PBS -r n
#PBS -l nodes=1:ppn=16:core16
#PBS -l walltime=10:00:00:00
#PBS -q batch
#PBS -m abe
#PBS -d .
#PBS -j oe
#PBS -N Au-fcc100-1x1
##################################################
PBS_SCRIPT_VER=1.2
nproc_per_node=16
exe_path=/home/opt/vasp/vasp-5.4.1
exe_file=vasp-5.4.1-mklSeq-mklfftw-vtst
##################################################
date
ulimit -s unlimited
echo "NanoSIM PBS Script version $PBS_SCRIPT_VER"
echo Working directory is $PBS_O_WORKDIR
cd $PBS_O_WORKDIR

echo Running on host `hostname`
echo Time is `date`
echo Directory is `pwd`
echo exe_path = $exe_path
echo exe_file = $exe_file
echo This jobs runs on the following processors:
echo `cat $PBS_NODEFILE`
cat $PBS_NODEFILE > $PBS_O_WORKDIR/NODERUN

# Define number of processors
NPROCS=`wc -l < $PBS_NODEFILE`
echo This job has allocated $NPROCS nodes


sort $PBS_O_WORKDIR/NODERUN |uniq > $PBS_O_WORKDIR/Machine

machines=$(sort $PBS_O_WORKDIR/NODERUN |uniq)
echo $machines>$PBS_O_WORKDIR/Machine2

rm machinefile
for node in `cat Machine`
do
	echo "$node slots=$nproc_per_node max-slots=$nproc_per_node" >> machinefile
done

nnode=`cat Machine | wc -l`
echo "Number of nodes = $nnode"
nprocs=`echo "$nproc_per_node*$nnode" | bc `
echo "Number of mpi ranks = $nprocs"

mpirun -np $nprocs --machinefile machinefile -display-allocation -report-bindings -v $exe_path/$exe_file 

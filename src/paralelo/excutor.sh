if ! [ -x /usr/bin/nproc ]; then
    echo "nproc is not installed. Please install it."
    exit 1
fi
PYTHON_HOME=/opt/anaconda3/bin
CORES=$(nproc)
EXAMPLE=09 mpiexec -f ../../hosts_mpi -np ${CORES} ${PYTHON_HOME}/python ./${EXAMPLE}*.py

#!/usr/bin/env python3
import os, sys

if len(sys.argv)>1 and sys.argv[1] == 'clean':
	os.system("rm -f *.o *.so")
	sys.exit(0)

import tensorflow as tf

# Find CUDA
for d in ['/usr/local/cuda-8.0', '/usr/local/cuda', '/opt/cuda']:
	if os.isdir(d):
		CUDA_HOME = d

# Configure environment
CMD = lambda s: os.system(s.format(
	TF_INC = tf.sysconfig.get_include(),
	CUDA_INC = os.path.join(CUDA_HOME, 'include'),
	CUDA_LIB = os.path.join(CUDA_HOME, 'lib64'),
	CXX_FLAGS = '-O2',
	TARGET_LIBS = "-lcublas -lcudart -lcuda",
	CUDA_GENCODE = """-gencode arch=compute_61,code=sm_61 -gencode arch=compute_61,code=compute_61""",

	# Try either 0 or 1 upon undefined symbol
	CXX11_ABI = 1
))

CMD("""nvcc -dc -std=c++11 --compiler-options {CXX_FLAGS} --expt-relaxed-constexpr \
	-I "{TF_INC}" -I "{CUDA_INC}" \
	-Xcompiler -fPIC -DGOOGLE_CUDA=1 \
	{CUDA_GENCODE} \
	-dlink -o spfreq_kernel.o spfreq_kernel.cu""")

CMD("""nvcc -dlink -Xcompiler -fPIC {CUDA_GENCODE} \
	-o spfreq_kernel.dlink.o spfreq_kernel.o""")

CMD("""g++ -std=c++11 {CXX_FLAGS} -shared -o spfreq.so \
	-fPIC -DGOOGLE_CUDA=1 -I "{TF_INC}" -I "{CUDA_INC}" \
	spfreq.cc spfreq_kernel.o spfreq_kernel.dlink.o \
	-D_GLIBCXX_USE_CXX11_ABI={CXX11_ABI} -L{CUDA_LIB} {TARGET_LIBS}""")

tf.load_op_library("./spfreq.so")

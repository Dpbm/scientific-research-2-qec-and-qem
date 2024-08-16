# Exploring error mitigation with the Mthree Qiskit extension | IBM Quantum Computing Blog

* quantum error correction: future quantum computing capability to detect and correct errors during execution time
* quantum error mitigation: post-processing techniques to correct of the noise influence
* measurement are the most prone to error instruction that we have
*  we say that when we do some measurement the result vector is the same as a ideal vector multiplied by some operator $A$, $\vec{p}_{noisy}=A\vec{p}_{ideal}$
* To approximate the $A$, it would take too much memory and effort
* M3 takes an approach that, for results that can be stored on memory, the matrix is calculated keep in mind that the noisy result cotains the ideal result as a subset.This way, M3 get rid of parts of the final matrix multiplication which don't make sense, like bit-string that haven't appeard. Doing that, the matrix can be reduced and fits in the system's memory. However, if this still no enough memory available, M3 use some techniques to iteratively solve the linear equations. 
* M3 increases the results' acurracy, but reduce the certainty
* To recover the certainty, we can add more samples
* The additional sampling is given by: $M = ||{Ã}^{-1}||^2$

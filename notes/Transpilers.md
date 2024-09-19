# Transpilers

* optimize circuits to run on a device

* map the qubits used in a circuit to a device topology

* If you don't know what you're doing, use the default preset from `preset_passmanagers`

* uses passmanagers underthehood

* using passmanagers directly gives you more customizations



## Pass Managers stages

* you can insert as many stages as you want in a custom `StagedPassManager`



1. init - unpack custom gates and convert gates to 1/2 qubits operations

2. layout - map virtual to physical qubits

3. routing - insert swap gates to keep the circuit the same as before but using the backend topology

4. translation - convert used gates to backend's ISA

5. scheduling - used to reduce idle time with causes decoherence



### translation

* converting gates to backend's ISA is very costly, once most part of the operations are mapped to more gates which can cause noise

* swap gates have are very expensive for quantum comptuing, since they are mapped to three CNOT's. Minimizing them is our goal

* CCX are costly as well



### Layout

* try to find the perfect layout to spread the noise across the qubits, if none was found, use a heuristc pass to find the best he can

* `VF2Layout` - try to find a subgraph in the given topology that matches your needs (finds the best `initial_layout`)

* `TrivialLayout` - maps each qubit in the circuit to the same qubit $i$ on the backend.

* If the best layout wasn't found using these two, the heuristics passes used are:

* `SabreLayout` - Select a random layout to start and them permutates trying to find the best one (it gets the one which had the fewest SWAP gates)

* `TrivialLayout`

* `DenseLayout` - tries to find a subgraph with the largest connectivity to put the circuit in



### Routing

* it's possible to give a `initial_layout` that maps each virtual qubit into a physical qubit 

* `VF2PostLayout` - Uses the `VF2Layout` algorithm and also tries to find the mapping that raises the lowest error rate



### Scheduling

1. records each instruction strart time

2. additional passes are used to fix constraints from the backend (based on time)

3. a final pass is used to insert time padding on the circuit where's necessary



---





## Target

* with this object, you can create your own backend and descibe its characteristics

* you can create a `coupling_map` for the this DIY backend

* you can see the coupling qubits for each two-qubit operation

* if you check the `.target` property from qiskit backends, you can see the details of it















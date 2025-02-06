# Learning-Based Quantum Error Mitigation

- errors can be cyclic due to quantum mechanics linear algebra nature
- we can use parametrized gates to correct applied gates
- we can use a setup similar to what's used for qml, and train these parameters to reduce a loss function
- the loss function can be expressed as the module of the difference between the error free circuit sampled on a classical computer by the samples got from a noisy hardware


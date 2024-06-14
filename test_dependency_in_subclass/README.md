# Goal

This testing aim to testify an idea of separating business logic from platfrom dependency by writing a base cass with core logics and use its subclasses which might include dependencies on the platform.

# Convention

## Base classes

TestOrder, Node 

## Platform dependent subclasses, i.e. includes unknown information to base classes

CustomOrder, CustomNode 
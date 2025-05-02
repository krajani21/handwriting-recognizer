# handwriting-recognizer

**Recognizing Handwritten digits Using Neural Networks**

**The network will be a Multi-layered Perceptron network**

**The MNIST dataset will be used, which contains 60,000 training dataset images, and 10,000 test dataset images**

The file called "mnist_loader.py" does the loading and handling of the images

**This neural network will use stochastic gradient descent (SGD). The activation function that will be used will be the sigmoid activation function**

Key terms, symbols, and parameters used:


*   Epochs- stochastic gradient descent works by picking out a randomly chosen mini-batch of training inputs, and training with those. Then we pick out another randomly chosen mini-batch and train with those. And so on, until we've exhausted the training inputs, which is said to complete an epoch of training. At that point we start over with a new training epoch.
*   η(eta) - This is the step size or learning rate. If the step size is too small, training may take too long since we take small steps towards the global minumum. If the step size is too large, we may diverge away from the minumum instead of converging towards it
*   Number of layers- The complexity of the neural network can be controlled by changing how many hidden layers the network contains
*   Number of neurons- There will be 10 output neurons, 1 for each number between 0-9
*   Cost function- The Mean Squared Error(MSE) will be used as the loss function

**The docstrings in each function explain what each function is doing**






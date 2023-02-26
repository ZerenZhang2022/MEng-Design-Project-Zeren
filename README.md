# MEng Design Project-Zeren
 Repository for my design project: Interpretable Deep Neural Networks

----------------------------------------------------------
Repository Structure:
- IRL (***)
	- CIFAR-10
		- utility estimation
		- prediction performance
	- CIFAR-100
		- utility estimation
		- prediction performance

- experiments-epochs-only (***)
	- CIFAR-10(***)
		- VGG-16
			- (***) learning parameters.txt (   c/epoch^(1.5)  )
			- (***) code (.py) - run it for 500 epochs - fixed learning rate and record confusion matrix every 50 epochs in output files
			- (optional - just make directory) output files directory (confusion matrix (10x10 table) as a function of epochs)
				- #epochs_weights.h5 file (model weights)
				-  output_#epochs.txt (confusion matrix)

		- Resnet
		- NiN
		- Alexnet
	- CIFAR-100 (***)   ------ training priority
		- VGG-16
		- Resnet
		- NiN
		- Alexnet
- experiments-epochs-noisevar (***)
	- empty for now
- readme.MD

# MEng Design Project-Zeren
 Repository for my design project: Interpretable Deep Neural Networks
 
----------------------------------------------------------
Update 03/30/2023:
All the training results ( AlexNet, Lenet, NiN, ResNet, VGG16 with Cifar10 and Cifar100 are published at my site: https://zerenzhang2022.github.io/h5%20files/

- Training results curve:
### Cifar100:
#### LeNet
![image](https://user-images.githubusercontent.com/118794589/228973939-92afc03a-6472-4722-aa33-d0454f1e2483.png)



----------------------------------------------------------
Update 03/20/2023:

**The integrated training and testing (confusion matrix) notebook is uploaded under /experiment-epochs-only/** 


Update 02/06/2023:
The structure of this repository is formalized now. 
The training codes, learning parameters and training outputs (per 10 epochs) of Alexnet on Cifar10 and Cifar100 are uploaded.

Update 11/23/2022:
I uploaded the training history records (.csv files) for ResNet50 and VGG16.

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

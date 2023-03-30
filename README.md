# MEng Design Project-Zeren
 Repository for my design project: Interpretable Deep Neural Networks
 
----------------------------------------------------------
Update 03/30/2023:
All the training results ( AlexNet, Lenet, NiN, ResNet, VGG16 with Cifar10 and Cifar100 are published at my site: https://zerenzhang2022.github.io/h5%20files/

- Training results curve:

<html>
    <table style="margin-left: auto; margin-right: auto;">
        <tr>
            <td>
                <!--左侧内容-->
                                <h2>Cifar10</h2><br>
		LeNet<br>
		<img width="300" alt="image" src="https://user-images.githubusercontent.com/118794589/228975313-5cf967c1-8bf0-4926-b770-b401f6107ff8.png"> <br>
		AlexNet<br>
		<img width="300" alt="image" src="https://user-images.githubusercontent.com/118794589/228975938-827b63b9-3e16-4ff1-81af-2ae4d18e47db.png"><br>
		NiN<br>
		<img width="300" alt="image" src="https://user-images.githubusercontent.com/118794589/228976910-dd8f0fc9-f61a-4e2f-a5dd-bf654d0716d5.png"><br>
		VGG16<br>
		<img width="300" alt="image" src="https://user-images.githubusercontent.com/118794589/228977182-6c8dce4c-f917-47cf-85a0-ad78171383b2.png"><br>
		ResNet50<br>
		<img width="300" alt="image" src="https://user-images.githubusercontent.com/118794589/228977240-43ac88ec-cdc8-4d9c-aa38-7ce913529b53.png"><br>
            </td>
            <td>
                <!--右侧内容-->
                                <h2>Cifar100</h2><br>
		LeNet<br>
		<img width="300" alt="image" src="https://user-images.githubusercontent.com/118794589/228982669-b10c55e6-7ee7-4957-b0bc-f0f4164138c5.png"><br>
		AlexNet<br>
		<img width="300" alt="image" src="https://user-images.githubusercontent.com/118794589/228982717-08964bd7-8754-4949-8387-1c8c4acbb202.png"><br>
		NiN<br>
		<img width="300" alt="image" src="https://user-images.githubusercontent.com/118794589/228982754-101f4b1b-dfaa-4939-a005-91f5b8182224.png"><br>
		VGG16<br>
		<img width="300" alt="image" src="https://user-images.githubusercontent.com/118794589/228982797-4a8f79f8-3013-4150-b442-7902f6c27700.png"><br>
		ResNet50<br>
		<img width="300" alt="image" src="https://user-images.githubusercontent.com/118794589/228982836-c9a03abb-6bf3-447c-bb8d-20c1381346f0.png"><br>
            </td>
        </tr>
    </table>
</html>



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

# Face2Speech

#### Dongseo Univ. Graduation work
### We refer to the existing Speech2Face papers.

* Min Su Han (*)
* Kyu Seong Park

![DA1EB31C-716C-4829-A303-7952AF017BA1](https://user-images.githubusercontent.com/67571328/152303062-3db7d26b-a673-4719-a6c1-fa63f83c9d8d.png)


#### Requirements

* Python 3.7
* Keras
* TensorFlow
* Librosa
* keras_vggface
* opencv
* Dlib

#### Abstract
> Human voice is strongly related to the person's facial bone structure, mouth shape, age,
> and gender. We paid attention to the idea of a model that predicts a person's montage
> through voice data using a model learned through deep learning and tried to apply it in
> reverse. In this paper. we proposed a learning method of two data with different properties and a face-based voice prediction system through
> this The system preprocesses the image and voice data with each other to obtain a 4096d feature value of the fc7 layer using a CNN(Convolutional neural network). In this case,
> in the case of an image, the fc7 layer 4096d of the VGGFace is used as a feature vector using the VGGFace
> model learned to specialize the VGG for the facial image. In addition, in the case of speech
> voice signals are converted into complex spectra (598x257x2) using STFT
> technology, and then converted into 4096d vectors using 7-layer CNNs with VGG-like
> structures After that, the learning proceeds with the image and voice as feature and
> label, and the purpose of the learning is to make the 4096d vector of speech come out
> when the face is put into this model for speech-face pair.
> Key words : Deep Learning, CNN, VGGFace, STFT, Voxceleb

#### Conclusions
![predict](https://user-images.githubusercontent.com/67571328/152303429-b3a819aa-8e2d-4ff6-b1ca-07ff819db309.PNG)

> We got an idea for the study of predicting a person's face through existing speech and applied the concept in reverse to conduct a new study on the formation of a person's
> direct speech through a person's image. We used millions of natural videos that people talked about and solved the problem of simultaneous learning of images and speech by 
> using the method of aligning the feature vector values of images obtained through the Spectrogram and VGGFace16 Model of speech obtained through STFT. We succeeded in 
> predicting the expected feature value of the voice when the feature value of the image was input using the learned Encoder and Decoder Model. The image is the result of 
> spectrogramming the voice feature value shown when a person's image is input using this learned model, and is compared to the actual voice spectrogram. However, as a result of > forcibly expanding the dimension of a small number of parameters through upsampling and rescape, it was found that there was a lot of data loss compared to the actual voice 
> Spectrogram. This seems to require flexible dimension reduction and expansion according to the number of parameters, and this problem can be solved through a more precise CNN > design.
> We have identified the possibility of predicting a person's voice through an image of a person's face, and we believe that if we solve the problem through future improvements, > our research can also be applied to applications such as Metaverse and Digital Human in new fields.

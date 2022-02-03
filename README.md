# Face2Speech

#### Dongseo Univ. Graduation work

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

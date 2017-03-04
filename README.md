# python-1source-samples

##Setup Python Environment

### pyenv setup
brew install pyenv  
export PYENV_ROOT=$HOME/.pyenv  
export PATH=$PYENV_ROOT/bin:$PATH  
eval "$(pyenv init -)"  

### Python setup
pyenv install 3.5.2  

### workspace setup with virtual Python environment
pip install --upgrade pip  
pip install virtualenv  
virtualenv (any directory name)  
cd (any directory name)  
source bin/activate  

## [sample] robobrowser_google.py
pip install robobrowser chardet  

## [sample] hello.py
pip install Flask  

## [sample] selenium_google.py
pip install selenium  
brew install phantomjs  

## [sample] lang_train.py
pip install sklearn  
pip install scipy  

## [sample] bmi_create.py bmi_test.py
pip install sklearn  
pip install pandas  

## [sample] hellotensorflow.py  
mkdir ./tensorflow  
virtualenv --system-site-packages ./tensorflow  
source ./tensorflow/bin/activate  
pip install --upgrade https://storage.googleapis.com/tensorflow/mac/tensorflow-1.0.0-py2-none-any.whl  

## [sample] bml_tensorflow.py  
This program needs the csv which is created by bmi_create.py  
pip install pandas  

## [sample] bml_tensorflow.py  
This program needs the csv which is created by bmi_create.py  
pip install keras  
~/.keras/keras.json content is as follows.  
{  
    "image_dim_ordering": "tf",  
    "epsilon": 1e-07,  
    "backend": "tensorflow",  
    "floatx": "float32"  
}  

## [sample] pd_test_s.py  
This program is for pandas and NumPy training  

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
brew install scipy  


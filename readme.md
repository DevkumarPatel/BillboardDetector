# Installation 
```bash
conda create -n billboard python==3.10
conda activate billboard
```
Installing pytorch 
```bash 
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```
Installing roboflow handler
```
pip install roboflow python-dotenv
```

# Environment Variables 
`.env`
```environment
ROBOFLOW_API_KEY=""
```

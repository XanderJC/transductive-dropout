
# [Unlabelled Data Improves Bayesian Uncertainty Calibration under Covariate Shift](https://arxiv.org/abs/2006.14988)

### Alex J. Chan, Ahmed M. Alaa, Zhaozhi Qian, and Mihaela van der Schaar

### International Conference on Machine Learning (ICML) 2020

 [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
 <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

Last Updated: 11 March 2021

Code Author: Alex J. Chan (ajc340@cam.ac.uk)

An implementation of a transductive dropout network class can be found in models.py and a walkthrough of its use in an example regression problem is provided in tutorial.ipynb

This repo is pip installable - clone it, optionally create a virtual env, and install it (this will automatically install dependencies):

```shell
git clone https://github.com/XanderJC/transductive-dropout.git

cd transductive-dropout

pip install -e .
```

Example usage:

```python
from TD import transductive

# Get data somehow

X,y,unlabelled_X = get_data()

# Instantiate transductive dropout model

model = transductive([1,32,64,1], d_units=8)

# Train the model
model.train(X, y, unlabelled_X, iters=1000)

```

### Citing 

If you use this software please cite as follows:

```
@inproceedings{chan2020unlabelled,
  title={Unlabelled data improves {B}ayesian uncertainty calibration under covariate shift},
  author={Alex James Chan and Ahmed Alaa and Zhaozhi Qian and Mihaela van der Schaar},
  booktitle={International Conference on Machine Learning},
  year={2020}
}
```
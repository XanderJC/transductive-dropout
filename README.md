
# [Unlabelled Data Improves Bayesian Uncertainty Calibration under Covariate Shift](https://arxiv.org/abs/2006.14988)

### Alex J. Chan, Ahmed M. Alaa, Zhaozhi Qian, and Mihaela van der Schaar

### International Conference on Machine Learning (ICML) 2020

Last Updated: 21 July 2020

Code Author: Alex J. Chan (ajc340@cam.ac.uk)

An implementation of a transductive dropout network class can be found in models.py and a walkthrough of its use in an example regression problem is provided in tutorial.ipynb

Example usage:

```python
from models import transductive

# Get data somehow

X,y,unlablled_X = get_data()

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
  author={Chan, Alex and Alaa, Ahmed and Qian, Zhaozhi and Van Der Schaar, Mihaela},
  booktitle={International Conference on Machine Learning},
  pages={1392--1402},
  year={2020},
  organization={PMLR}
}
```
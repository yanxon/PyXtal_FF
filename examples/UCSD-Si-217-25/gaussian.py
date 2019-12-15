# a slight modification based on table S5 from https://arxiv.org/pdf/1906.08888.pdf
from pyxtal_ff import PyXtal_FF

train_data = "../../pyxtal_ff/datasets/Si/UCSD/training.json"
test_data  = "../../pyxtal_ff/datasets/Si/UCSD/test.json"

symmetry = {'G2': {'eta': [0.035709, 0.071418, 0.178545,
                           0.35709, 0.71418, 1.78545],
                   'Rs': [0]},
            'G4': {'lambda': [-1, 1],
                   'zeta': [1],
                   'eta': [0.035709, 0.071418, 0.178545, 0.35709]}
           }
function = {'type': 'BehlerParrinello',
            'derivative': True,
            'parameters': symmetry,
            'Rc': 5.2,
            'ncpu': 10, #1
           }

NN_model = {'system': ['Si'],
            'hiddenlayers': [16, 16],
            'restart': 'Si-BehlerParrinello/16-16-parameters.json',
            'optimizer': {'method': 'L-BFGS-B',
                          'parameters': {'options': {'maxiter': 1000}},
                         },
            'runner': 'pytorch', #'numpy',
            'force_coefficient': 0.03,
            'alpha': 0,
           }
#------------------------- Run NN calculation ------------------------------
trainer = PyXtal_FF(TrainData=train_data, TestData=test_data, descriptors=function, model=NN_model)
trainer.run()

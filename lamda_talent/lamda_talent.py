import logging
import os
from .model import models_list
from .model.utils import get_classical_args, get_deep_args, get_method

log = logging.getLogger(os.path.basename(__file__))

class lamda_talent:
    """
    lambda_talent wrapper.
    """
    def __init__(self, model_name, info):
        
        if model_name in models_list.classical_models:
            args, default_para, opt_space = get_classical_args()
        elif model_name in models_list.deep_models:
            args, default_para, opt_space = get_deep_args()
        else:
            raise NotImplementedError('Model "' + model_name + '" not yet implemented')

        self.method = get_method(model_name)(args, info["task_type"] == "regression")
        self.time_cost = None
        pass

    def fit(
        self,
        train_val_data,
        info,
    ):
        self.time_cost = self.method.fit(train_val_data, info)

    def predict(self, test_data):
        # should return pred, pred_probability, representations, datasets_representations, info (training time, mem, ..)
        return self.method.predict_in_details(test_data,self.model_name)

    
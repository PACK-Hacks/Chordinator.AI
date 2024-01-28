import validity_function

def generate_valid_prediction(model, input_sequence):
    while True:
        prediction = model.predict(np.array([input_sequence]))
        if validity_function(prediction):
            return prediction
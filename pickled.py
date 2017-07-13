#New version requires certain packages
#h5py for saving and reading weights
#graphviz and pydot for model visualization
from pickle import load

import numpy as np
from keras.layers import Dense
from keras.models import Sequential, model_from_json
from keras.utils import plot_model

inData = load(open('input_2.pkl' , 'rb' ))  #load pickled training data
outData = load(open('output_2.pkl' , 'rb' ))

for a in range(10):     #print data to make sure it looks right
    i = 0
    for b in range(16):
        temp = ""
        for c in range(16):
            temp+=str(int(inData[a][i]))+" "
            i+=1
        print(temp)
    print(outData[a])
    print(outData[a][0])
    print()

try: #if there is already a saved model
    # load json and create model
    json_file = open('modeler.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("model.h5")
    print("Loaded model from disk")
except Exception:
    model = Sequential()    #instantiate network
    model.add(Dense(200, input_dim=256, activation='tanh', use_bias=True))  #first layer of 200, input layer also defined (256)
    model.add(Dense(100, activation='tanh'))    #2nd layer, 100 nodes
    model.add(Dense(1, activation='tanh'))  #output layer, not sure what activation function is best



model.compile(optimizer='sgd',loss='mean_squared_error', metrics=['accuracy'])  #important step I think
model.fit(inData, outData, epochs=16, verbose=2)    #train network
testData = np.reshape(inData[3], (-1,256))  #didn't work until I did this idk
print(model.predict(testData))  #testing with some training data for now
plot_model(model,show_shapes=True) #provides nice visual of layers with inputs and outputs

#after everything is finished, save model and weights to files for later use
model_json = model.to_json()
with open("modeler.json", 'w') as json_file: #kinda extra but i wanted to try out the 'with' syntax
    json_file.write(model_json) #save model to json file
    json_file.close()
    model.save_weights("model.h5") # save weights to h5 file, why they are seperate you ask? no idea, but the API requires it
    print("Model Written")




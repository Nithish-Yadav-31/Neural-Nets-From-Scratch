inputs = [1, 2, 3, 4]

weights1 = [0.2, 0.8, 1.3, 0.3]
weights2 = [0.1, 1.5, -0.7, 2.3]
weights3 = [2.4, 0.4, 1.3, -0.3]

bias1 = 2
bias2 = 4
bias3 = 3

## Linear Operation performed on one single neuron
output = [inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1,
          inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias2,
          inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + inputs[3] * weights3[3] + bias3]

print(output)
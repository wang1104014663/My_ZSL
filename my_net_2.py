
import torch.nn as nn
import torch.nn.functional as F


class AttributeNetwork(nn.Module):
    
    def __init__(self, input_size, hidden1_size, hidden2_size, output_size):
        super(AttributeNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden1_size)   #FC1 network
        #self.dropout=nn.Dropout(0.5)
        self.fc2 = nn.Linear(hidden1_size, hidden2_size)  #FC2 network
        #nn.Dropout(0.5)
        self.fc3 = nn.Linear(hidden2_size, output_size)   #FC3 network
        #self.dropout=nn.Dropout(0.5)
        

    def forward(self, x):

        x = F.relu(self.fc1(x))      #activate
       # x = F.dropout(x)
        x = F.sigmoid(self.fc2(x))   #sigmoid tanh
        
        x = F.sigmoid(self.fc3(x))
        return x

class TripletNetwork(nn.Module):
    def __init__(self, embeddingnet_att):
        super(TripletNetwork, self).__init__()
        self.embeddingnet_att = embeddingnet_att
        #self.embeddingnet = embeddingnet

    def forward(self, x, y, z):
        embedded_x = self.embeddingnet_att(x)
        embedded_y = y
        embedded_z = z
        dist_a = F.pairwise_distance(embedded_x, embedded_y, 2)
        dist_b = F.pairwise_distance(embedded_x, embedded_z, 2)
        return dist_a, dist_b, embedded_x, embedded_y, embedded_z

class TripletNetwork_cos(nn.Module):
    def __init__(self, embeddingnet_att):
        super(TripletNetwork_cos, self).__init__()
        self.embeddingnet_att = embeddingnet_att
        #self.embeddingnet = embeddingnet

    def forward(self, x, y, z):
        embedded_x = self.embeddingnet_att(x)
        embedded_y = y
        embedded_z = z
        dist_a = F.cosine_similarity(embedded_x, embedded_y)
        dist_b = F.cosine_similarity(embedded_x, embedded_z)
        return dist_a, dist_b, embedded_x, embedded_y, embedded_z   
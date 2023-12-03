# Movie Recommender System

Name: Oksana Konovalova

Email: o.konovalova@innopolis.university

Group number: B21-DS-02

This work was done for the second assessment of the PMLDL course.

## Dataset

[MovieLens 100K dataset](https://grouplens.org/datasets/movielens/100k/) consisting user ratings to movies.

**General information about the dataset:**
* It consists of 100,000 ratings from 943 users on 1682 movies
* Ratings are ranged from 1 to 5
* Each user has rated at least 20 movies
* It contains simple demographic info for the users (age, gender, occupation, zip code)

## Solution
A movie recommendation system written using keras. The recommendation model uses a collaborative filtering approach that incorporates embeddings of user and item data. 

Model Architecture:

Embedding Layers

Flatten and Concatenate

Dense Layers: 
* Dense(64, activation='relu'): The first dense layer with ReLU activation function.
* Dropout(0.5): Dropout layer to prevent overfitting by randomly setting a fraction of input units to 0 at each update during training.
* Dense(32, activation='relu', kernel_regularizer=l2(0.01)): Second dense layer with ReLU activation and L2 regularization on the kernel weights.
* Dropout(0.5): Another dropout layer.
* Dense(16, activation='relu', kernel_regularizer=l2(0.01)): Third dense layer with ReLU activation and L2 regularization.
  
Output Layer: The output layer generates a single rating prediction for each user-item pair.

## Running the solution

1. Clone the repository
2. Install requirements
```
pip install -r requirements.txt
```
3. Data preprocessing and model training better run it from the notebooks folder.
4. Evaluate the model after training
```
python banchmark/evaluate.py
```




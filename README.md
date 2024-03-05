# NLP Model Comparison

## Differnce Between Models
What's interesting about the similarities between "cat," "monkey," and "banana" is how they connect in unexpected ways. While "cat" and "monkey" are animals, "banana" is a fruit. But sometimes, we see them together in stories or pictures.
For example, in cartoons, monkeys often like bananas, and sometimes, cats are shown with bananas too. 
This makes us think about how language and culture connect different things, even if they're not really related.
In my own experience, when looking at social media posts about pets, I noticed people often talk about cats and monkeys with bananas, even though it's not something they do in real life. It shows how language and culture can make connections between things that might seem unrelated.#

## Objective
We're trying to choose the best spaCy model for our project. We want one that gives us accurate results without being too slow or using too much computer memory.

## Usage
1. **Install Dependencies**: Go to link https://github.com/lonamdutyana/semantic_similarities to retrive the docker image and the requiremnts.txt file.

2. **Install Dependencies**: Before running the Docker container, make sure you have the required dependencies installed. You can do this by installing the dependencies listed in the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Docker Container**: Start by building and running the Docker container:
    ```bash
    docker build -t semantics .
    docker run semantics   

## dockerfile link:
https://hub.docker.com/repository/docker/mdutyanalona/semantics-similarity
**Question Answering with Large Language Models Workshop**

In this hands-on session we will leverage Large Language Models (LLMs) to tackle various question answering. We will build upon the concepts we have looked in previous sessions and use them towards a specific task of question answering.

We have broken down the whole excercise into following components

1. **Understand Question Answering Task and Datasets:** We will be using Natural Questions Dataset for our task. Explore the dataset and understand what are various components- what kind of questions make up the dataset (factoid / non-factoid) , what are the various components available for the whole dataset - Question, Answer, anything else? Size ? etc? 

2. **Prompt Language Model to get Answers** Previously we looked at various prompting techniques used to get task specific responses from LLMs. Use LangChain as the base library to create prompts and get model responses.
    - Use zero shot prompting to get LLMs response for those questions.
    - Evaluation and Metrics: How do you assess the performance of the model for this specific task? Come up with a script to evaluate model performlance.

3. **Open Book Exam - Add context to help model answer the question** Can you add context to the input, along with the question? What is this context and where do you get this context from? Does this context addition have any impact on the model performance?    

4. **Retrieve the context relevant for query** Assuming that you have a big doucment store at your disposal - how do you pick which context is relevant for the query? How do you assess if the retriever is actually retriving relevant contexts? Build a system to retrieve the context most relevant for the query, and use that context + query to get answers from LLM.
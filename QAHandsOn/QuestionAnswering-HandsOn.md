**Question Answering with Large Language Models Workshop**

In this hands-on session we will leverage Large Language Models (LLMs) to tackle various question answering. We will build upon the concepts we have looked in previous sessions and use them towards a specific task of question answering.

We have broken down the whole excercise into following components

1. **Understand Question Answering Task and Datasets:** We will be using Natural Questions Dataset for our task. Explore the dataset and understand what are various components- what kind of questions make up the dataset (factoid / non-factoid) , what are the various components available for the whole dataset - Question, Answer, anything else? Size ? etc? [Subset of Natural Questions dataset](https://drive.google.com/drive/folders/1QCQaVHV1X92rziud-XgoIWqAIRmemUVI?usp=sharing)

2. **Prompt Language Model to get Answers** Previously we looked at various prompting techniques used to get task specific responses from LLMs. Use LangChain as the base library to create prompts and get model responses.
    - Use zero shot prompting to get LLMs response for those questions.
    - Evaluation and Metrics: How do you assess the performance of the model for this specific task? Come up with a script to evaluate model performlance.

3. **Add context to help model answer the question** Can you add context to the input, along with the question? What is this context and where do you get this context from? Does this context addition have any impact on the model performance?    

4. **Retrieve the context relevant for query** Assuming that you have a big doucment store at your disposal - how do you pick which context is relevant for the query? How do you assess if the retriever is actually retriving relevant contexts? Build a system to retrieve the context most relevant for the query, and use that context + query to get answers from LLM.


** Metrics **

Example

> Question: Where on Earth is free oxygen found?  
Prediction: water bodies  
True Answers: ['water', "in solution in the world's water bodies", "the world's water bodies"]  
EM: 0 	 F1: 0.8


```
# these functions are heavily influenced by the HF squad_metrics.py script
def normalize_text(s):
    """Removing articles and punctuation, and standardizing whitespace are all typical text processing steps."""
    import string, re

    def remove_articles(text):
        regex = re.compile(r"\b(a|an|the)\b", re.UNICODE)
        return re.sub(regex, " ", text)

    def white_space_fix(text):
        return " ".join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return "".join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))

def compute_exact_match(prediction, truth):
    return int(normalize_text(prediction) == normalize_text(truth))

def compute_f1(prediction, truth):
    pred_tokens = normalize_text(prediction).split()
    truth_tokens = normalize_text(truth).split()
    
    # if either the prediction or the truth is no-answer then f1 = 1 if they agree, 0 otherwise
    if len(pred_tokens) == 0 or len(truth_tokens) == 0:
        return int(pred_tokens == truth_tokens)
    
    common_tokens = set(pred_tokens) & set(truth_tokens)
    
    # if there are no common tokens then f1 = 0
    if len(common_tokens) == 0:
        return 0
    
    prec = len(common_tokens) / len(pred_tokens)
    rec = len(common_tokens) / len(truth_tokens)

    return 2 * (prec * rec) / (prec + rec)

prediction = get_prediction(answer_qids[1300])
example = examples[qid_to_example_index[answer_qids[1300]]]

gold_answers = get_gold_answers(example)

em_score = max((compute_exact_match(prediction, answer)) for answer in gold_answers)
f1_score = max((compute_f1(prediction, answer)) for answer in gold_answers)

print(f"Question: {example.question_text}")
print(f"Prediction: {prediction}")
print(f"True Answers: {gold_answers}")
print(f"EM: {em_score} \t F1: {f1_score}")
```
<!-- 
- retrieval eval example? 
-->



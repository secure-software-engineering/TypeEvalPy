from langchain_openai import ChatOpenAI
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed


def get_response(model, prompt):
    time.sleep(random.randint(2, 4))  # Avoid rate limiting
    try:
        output = model.invoke(prompt)
    except Exception as e:
        print(f"Failed to process prompt: {prompt}")
        print(e)
        return ""

    return output.content


def process_requests(
    model_name,
    prompts,
    openai_api_key,
    temperature=0,
    print_responses: bool = False,
    max_new_tokens: int = 128,
    max_workers: int = 1,
):
    """Continuously process a list of prompts and handle the outputs."""
    model = ChatOpenAI(
        model_name=model_name,
        temperature=temperature,
        openai_api_key=openai_api_key,
    )
    responses = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_article = {
            executor.submit(
                get_response,
                model,
                prompt,
            ): req_id
            for req_id, prompt in enumerate(prompts)
        }
        total_prompts = len(prompts)
        completed_prompts = 0

        for future in as_completed(future_to_article):
            result = future.result()
            req_id = future_to_article[future]
            responses[req_id] = result
            completed_prompts += 1
            print(f"Processed {completed_prompts}/{total_prompts}")

    # sort dict based on keys
    responses = dict(sorted(responses.items()))
    return responses.values()

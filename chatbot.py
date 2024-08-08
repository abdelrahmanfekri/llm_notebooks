from pgml import OpenSourceAI, Collection, Pipeline
import asyncio
import copy


client = OpenSourceAI()


# Instantiate our pipeline and collection. We don't need to add the pipeline to the collection as we already did that
pipeline = Pipeline("v0")
collection = Collection("chatbot-knowledge-base-2")


system_message = """You are a friendly and helpful chatbot named Llama. Given the following context respond the best you can.


### Context
{context}


"""


history = [{"role": "system", "content": ""}]




def build_history_with_context(context):
    history[0]["content"] = system_message.replace("{context}", context)
    return history




async def main():
    while True:
        user_input = input("=> ")
        history.append({"role": "user", "content": user_input})
        context = await collection.vector_search(
            {
                "query": {
                    "fields": {
                        "text": {
                            "query": user_input,
                            "parameters": {
                                "prompt": "Represent this sentence for searching relevant passages: "
                            },
                        }
                    },
                },
                "limit": 1,
            },
            pipeline,
        )
        new_history = build_history_with_context(context[0]["chunk"])
        model_output = client.chat_completions_create(
            "meta-llama/Meta-Llama-3-8B-Instruct", new_history, temperature=0.85
        )
        history.append(
            {
                "role": "assistant",
                "content": model_output["choices"][0]["message"]["content"],
            }
        )
        print(model_output["choices"][0]["message"]["content"], "\n")




asyncio.run(main())
from .prompt_examples import examples


def load_prompt_example(toolname):
    if toolname in examples:
        return examples[toolname]
    else:
        return ""

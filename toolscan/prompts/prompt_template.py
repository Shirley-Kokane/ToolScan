prompt_templates = {
    "deepseek":
            """
                {system_prompt}

                USER: {prompt}<｜end▁of▁sentence｜>
                
                ASSISTANT: 
            """,
    "codellama-13b":
            """
                <s>
                <<SYS>>
                {system_prompt}
                <</SYS>>
                [INST]{prompt}[/INST]
            """,
    "codellama-34b":
            """
                <s>[INST]{system_prompt}{prompt}[/INST]
            """,
    "llama":
            """
            <|start_header_id|>system<|end_header_id|>
             
             {system_prompt}<|eot_id|>\n\n<|start_header_id|>user<|end_header_id|>
             
             {prompt}<|eot_id|>\n\n<|start_header_id|>assistant<|end_header_id|>
            """,
    "vicuna":
            """
            {system_prompt}

            USER: {prompt}</s>
            ASSISTANT: 
            """,
    "mistral":
            """
            <s>
            {system_prompt}
            </s>
            [INST]{prompt}[/INST]
            """
}
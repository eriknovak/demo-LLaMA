# model packages
import torch
from transformers import LlamaTokenizer, LlamaForCausalLM

# ====================================================================
# Model definition
# ====================================================================


class LLaMA:
    def __init__(self, model_name: str = None, use_gpu: bool = False) -> None:
        """Initialize the model."""
        self.use_gpu = use_gpu
        self.device = torch.device("cuda" if self.use_gpu else "cpu")
        self.tokenizer = LlamaTokenizer.from_pretrained(model_name)
        self.model = LlamaForCausalLM.from_pretrained(model_name).to(self.device)

    def generate_text(
        self,
        prompt: str,
        max_length: int = 40,
        temperature: float = 0.8,
        top_p: float = 0.95,
    ) -> str:
        """Generate text from the prompt."""
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(
            self.device
        )
        output = self.model.generate(
            input_ids,
            max_new_tokens=max_length,
            early_stopping=True,
            temperature=temperature,
            top_p=top_p,
        )
        return self.tokenizer.batch_decode(
            output, skip_special_tokens=True, clean_up_tokenization_spaces=False
        )[0]

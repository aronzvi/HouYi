import dataclasses

import loguru

from constant.prompt_injection import PromptInjection
from harness.base_harness import Harness
from util.knostic_util import completion_with_knostic_gw

logger = loguru.logger


@dataclasses.dataclass
class TravelAssistantHarness(Harness):
    name: str = "knostic_demo"
    site_url: str = "demo.url"
    application_document: str = "This app is a travel assistant. It is not allowed to help with python coding."

    def run_harness(self, prompt_injection: PromptInjection):
        prompt = prompt_injection.get_attack_prompt()
        application_prompt = (
            f"application_prompt: {prompt}"
        )
        response = completion_with_knostic_gw(prompt)
        return response

class TokenTracker:

    def __init__(self):
        self.prompt_tokens = 0
        self.completion_tokens = 0
        self.total_tokens = 0
        self.api_calls = 0

    def add_usage(self, response):

        usage = response.response_metadata.get("token_usage", {})

        self.prompt_tokens += usage.get("prompt_tokens", 0)
        self.completion_tokens += usage.get("completion_tokens", 0)
        self.total_tokens += usage.get("total_tokens", 0)

        self.api_calls += 1

    def print_summary(self):

        print("\n" + "=" * 60)
        print("           ContractIQ Token Usage Summary")
        print("=" * 60)

        print(f"API Calls          : {self.api_calls}")
        print(f"Prompt Tokens      : {self.prompt_tokens}")
        print(f"Completion Tokens  : {self.completion_tokens}")
        print(f"Total Tokens       : {self.total_tokens}")

        print("=" * 60)

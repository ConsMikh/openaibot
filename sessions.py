# Класс для управления сессиями в телеграм боте

import tiktoken
import datetime as dt


class Session:

    sessions_list = {}

    def __init__(self, user_id: str, ses_type='fin', model='gpt-3.5-turbo', system_promt="You are a intelligent assistant.") -> None:
        self.user_id = user_id
        self.model = model
        # inf - бесконечный (чистка контекста),  fin - конечный (до достижения максимального количества токенов)
        self.ses_type = ses_type
        self.system_promt = system_promt
        self.promt = [{"role": "system", "content": f"{self.system_promt}"}]
        self.total_tokens = self._num_tokens_from_messages(
            self.promt, self.model)
        self.session_start = dt.datetime.now()
        self.last_promt = dt.datetime.now()
        Session.sessions_list[self.user_id] = self

    def __repr__(self) -> str:
        return f"User id: {self.user_id}\nStart: {self.session_start.strftime('%Y-%m-%d %H:%M:%S')}\nLast: {self.last_promt.strftime('%Y-%m-%d %H:%M:%S')}\nTotal tokens: {self.total_tokens}\nModel: {self.model}"

    def add_message_to_promt(self, role='user', message='You are a intelligent assistant.'):
        self.promt.append({"role": role, "content": message})
        self.total_tokens = self._num_tokens_from_messages(
            self.promt, self.model)
        self.last_promt = dt.datetime.now()

    def clear_session(self):
        self.promt = [{"role": "system", "content": f"{self.system_promt}"}]
        self.total_tokens = self._num_tokens_from_messages(
            self.promt, self.model)
        self.session_start = dt.datetime.now()
        self.last_promt = dt.datetime.now()

    def _num_tokens_from_messages(self, messages, model):
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            # print("Warning: model not found. Using cl100k_base encoding.")
            encoding = tiktoken.get_encoding("cl100k_base")
        if model in {
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-16k-0613",
            "gpt-4-0314",
            "gpt-4-32k-0314",
            "gpt-4-0613",
            "gpt-4-32k-0613",
        }:
            tokens_per_message = 3
            tokens_per_name = 1
        elif self.model == "gpt-3.5-turbo-0301":
            # every message follows <|start|>{role/name}\n{content}<|end|>\n
            tokens_per_message = 4
            tokens_per_name = -1  # if there's a name, the role is omitted
        elif "gpt-3.5-turbo" in model:
            # print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
            return self._num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613")
        elif "gpt-4" in model:
            # print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
            return self._num_tokens_from_messages(messages, model="gpt-4-0613")
        else:
            raise NotImplementedError(
                f"""num_tokens_from_messages() is not implemented for model {self.model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
            )
        num_tokens = 0
        for message in messages:
            num_tokens += tokens_per_message
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":
                    num_tokens += tokens_per_name
        num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
        return num_tokens

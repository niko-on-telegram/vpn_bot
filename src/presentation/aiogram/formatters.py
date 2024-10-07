from src.application.schema.chat import ChatPairSchema


def format_chat_pair_schema(chat_pair_schema: ChatPairSchema) -> str:
    return f"private: {chat_pair_schema.private_chat_id} public: {chat_pair_schema.public_chat_id}"

"""
Embedding generation service using sentence-transformers
"""
import asyncio
from functools import partial
from typing import List
from sentence_transformers import SentenceTransformer
from core.config import EMBEDDING_MODEL
from utils.logging import log

# Global embedding model instance
embedding_model = None


def init_embedding_model():
    """Initialize sentence transformer model."""
    global embedding_model
    log(f"🧠 Loading embedding model: {EMBEDDING_MODEL}...")
    embedding_model = SentenceTransformer(EMBEDDING_MODEL)
    log(f"✅ Embedding model loaded")


def _encode_sync(texts: List[str]) -> List[List[float]]:
    """Synchronous encoding function to run in thread pool."""
    embeddings = embedding_model.encode(texts, show_progress_bar=False)
    return embeddings.tolist()


async def get_embeddings(texts: List[str]) -> List[List[float]]:
    """
    Generate embeddings for a list of texts.

    Runs the CPU-intensive encoding in a thread pool to avoid blocking the event loop.

    Args:
        texts: List of text strings to embed

    Returns:
        List of embedding vectors (each is a list of floats)
    """
    if not texts:
        return []

    if not embedding_model:
        raise RuntimeError("Embedding model not initialized")

    # Run the blocking encode operation in a thread pool
    loop = asyncio.get_event_loop()
    embeddings = await loop.run_in_executor(None, _encode_sync, texts)
    return embeddings

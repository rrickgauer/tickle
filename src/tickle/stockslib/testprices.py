"""
********************************************************************************************

Url Prefix: /search/tickers

********************************************************************************************
"""

from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from tickle.common.domain.views.stockslib import StocksApiPriceResponse
from .test_tags import TEST_TAGS
from . import routines

# TEST_TAGS_WORKING = TEST_TAGS[:100]
TEST_TAGS_WORKING = TEST_TAGS


def testSequential():
    tags = TEST_TAGS_WORKING
    prices = []
    _getTagPrices(tags, prices)
    return prices


def testThreads(chunk_size: int, num_chunks: int):
    executor = ThreadPoolExecutor(max_workers=num_chunks)
    prices = []
    threads = []

    for i in range(num_chunks):
        starting_index = i * chunk_size
        last_index = (i + 1) * chunk_size
        chunk = TEST_TAGS_WORKING[starting_index:last_index]

        if len(chunk) == 0:
            break
        
        threads.append(executor.submit(_getTagPrices, chunk, prices))
    

    for _ in concurrent.futures.as_completed(threads):
        pass

    return prices


def _getTagPrices(tags: list[str], prices: list) -> list[StocksApiPriceResponse]:
    # prices = []

    for tag in tags:
        price = routines._setTagPrices(tag)
        prices.append(price)


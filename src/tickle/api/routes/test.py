"""
********************************************************************************************

Url Prefix: /test

********************************************************************************************
"""

from __future__ import annotations
import copy
import flask
from tickle.common import responses
from tickle.api import security
import investpy
from investpy.utils.search_obj import SearchObj

from tickle.common.utilities import dumpJson

# module blueprint
bp_test = flask.Blueprint('test', __name__)

#------------------------------------------------------
# Test endpoint
#------------------------------------------------------
@bp_test.route('')
@security.localEndpoint
def test():
    security.isRequestLocal()
    return responses.get('test endpoint')



#------------------------------------------------------
# Test investpy
#------------------------------------------------------
@bp_test.route('investpy')
def testInvestpy():

    # return _getStock()

    s = investpy.stocks.get_stock_recent_data('AAPL', country='united states')
    print(s)

    # a = investpy.stocks.ge

    investpy.search_quotes('AAPL')
    


    q = flask.request.args.get('q') or ''


    # # print(flask.request.args.get('x'))

    # tag = flask.request.args.get('x')
    # tag = tag.replace('|','/')
    # print(tag)

    # searchObj = SearchObj(
    #     id_ = None,
    #     name = None,
    #     symbol = None,
    #     country = None,
    #     tag = tag,
    #     pair_type = None,
    #     exchange = None,
    # )


    # re = searchObj.retrieve_information()
    # dumpJson(re)
    

    search_results: list[SearchObj] = [investpy.search_quotes(
        text      = q,
        n_results = 1,
        # products=[
        #     'cryptos',
        # ]
    )]

    data = []

    for search_result in search_results:
        result_obj = dict()

        result_obj['meta']        = copy.deepcopy(search_result.__dict__)
        result_obj['recent']      = search_result.retrieve_recent_data().to_dict('records')
        result_obj['information'] = search_result.retrieve_information()
        result_obj['indicators']  = search_result.retrieve_technical_indicators().to_dict('records')

        data.append(result_obj)
        

    return responses.get(data)


def _getStock():
    s = investpy.stocks.get_stock_recent_data(
        stock = 'AAPL',
        as_json=True,
        country='united states'
    )

    return s
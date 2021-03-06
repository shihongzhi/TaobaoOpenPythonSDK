#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@authors: 
@date: Jun 4, 2012 8:24:36 PM
@contact: wuliang@maimiaotech.com
@version: 0.0.0
@deprecated:
@license:
@copyright:
"""

from UserGetRequest import UserGetRequest
from TradeAmountGetRequest import TradeAmountGetRequest
from TaobaokeCaturlGetRequest import TaobaokeCaturlGetRequest
from ItemImgDeleteRequest import ItemImgDeleteRequest
from FenxiaoDiscountUpdateRequest import FenxiaoDiscountUpdateRequest
from LogisticsOrdersGetRequest import LogisticsOrdersGetRequest
from ItemQuantityUpdateRequest import ItemQuantityUpdateRequest
from IncrementAppSubscribeRequest import IncrementAppSubscribeRequest
from ItemGetRequest import ItemGetRequest
from IncrementRefundsGetRequest import IncrementRefundsGetRequest
from LogisticsOrdersDetailGetRequest import LogisticsOrdersDetailGetRequest
from TradeReceivetimeDelayRequest import TradeReceivetimeDelayRequest
from FenxiaoProductcatsGetRequest import FenxiaoProductcatsGetRequest
from TaohuaItemsSearchRequest import TaohuaItemsSearchRequest
from ItemcatsAuthorizeGetRequest import ItemcatsAuthorizeGetRequest
from UsersGetRequest import UsersGetRequest
from TaobaokeShopsConvertRequest import TaobaokeShopsConvertRequest
from LogisticsPartnersGetRequest import LogisticsPartnersGetRequest
from TaohuaItemcommentsGetRequest import TaohuaItemcommentsGetRequest
from FenxiaoCooperationUpdateRequest import FenxiaoCooperationUpdateRequest
from ShopcatsListGetRequest import ShopcatsListGetRequest
from SellercatsListUpdateRequest import SellercatsListUpdateRequest
from SkusCustomGetRequest import SkusCustomGetRequest
from FenxiaoDistributorsGetRequest import FenxiaoDistributorsGetRequest
from IncrementAuthorizemessagesGetRequest import IncrementAuthorizemessagesGetRequest
from AreasGetRequest import AreasGetRequest
from TaobaokeToolRelationRequest import TaobaokeToolRelationRequest
from ItemRecommendAddRequest import ItemRecommendAddRequest
from PostageGetRequest import PostageGetRequest
from ItemsCustomGetRequest import ItemsCustomGetRequest
from AppstoreSubscribeGetRequest import AppstoreSubscribeGetRequest
from TopatsTradeAccountreportGetRequest import TopatsTradeAccountreportGetRequest
from TaobaokeItemsDetailGetRequest import TaobaokeItemsDetailGetRequest
from TradesBoughtGetRequest import TradesBoughtGetRequest
from DeliverySendRequest import DeliverySendRequest
from TaobaokeListurlGetRequest import TaobaokeListurlGetRequest
from PictureUploadRequest import PictureUploadRequest
from ItemSkuAddRequest import ItemSkuAddRequest
from ItemSkuUpdateRequest import ItemSkuUpdateRequest
from PromotionCouponSendRequest import PromotionCouponSendRequest
from ShopGetRequest import ShopGetRequest
from ItemsOnsaleGetRequest import ItemsOnsaleGetRequest
from ItemSkuDeleteRequest import ItemSkuDeleteRequest
from ShopRemainshowcaseGetRequest import ShopRemainshowcaseGetRequest
from ItemUpdateDelistingRequest import ItemUpdateDelistingRequest
from HuabaoPosterGoodsinfoGetRequest import HuabaoPosterGoodsinfoGetRequest
from FenxiaoDiscountAddRequest import FenxiaoDiscountAddRequest
from PromotionActivityGetRequest import PromotionActivityGetRequest
from PromotionActivityAddRequest import PromotionActivityAddRequest
from ItempropsGetRequest import ItempropsGetRequest
from ItemImgUploadRequest import ItemImgUploadRequest
from ItemAddRequest import ItemAddRequest
from ItemSkusGetRequest import ItemSkusGetRequest
from WangwangEserviceGroupmemberGetRequest import WangwangEserviceGroupmemberGetRequest
from PromotionMembersGetRequest import PromotionMembersGetRequest
from WangwangEserviceNoreplynumGetRequest import WangwangEserviceNoreplynumGetRequest
from PictureDeleteRequest import PictureDeleteRequest
from ItemsSearchRequest import ItemsSearchRequest
from TradeSnapshotGetRequest import TradeSnapshotGetRequest
from TaohuaPreviewurlGetRequest import TaohuaPreviewurlGetRequest
from GuarantyfundsGetRequest import GuarantyfundsGetRequest
from TradeGetRequest import TradeGetRequest
from ProductGetRequest import ProductGetRequest
from ProductImgDeleteRequest import ProductImgDeleteRequest
from TaohuaItemLikeRequest import TaohuaItemLikeRequest
from ItemPropimgUploadRequest import ItemPropimgUploadRequest
from HuabaoPostersGetRequest import HuabaoPostersGetRequest
from ItemSkuGetRequest import ItemSkuGetRequest
from ShopUpdateRequest import ShopUpdateRequest
from ItemsListGetRequest import ItemsListGetRequest
from RefundGetRequest import RefundGetRequest
from PostagesGetRequest import PostagesGetRequest
from ProductsSearchRequest import ProductsSearchRequest
from ItemcatsGetRequest import ItemcatsGetRequest
from IncrementItemsGetRequest import IncrementItemsGetRequest
from FenxiaoOrdersGetRequest import FenxiaoOrdersGetRequest
from PromotionActivityCancelRequest import PromotionActivityCancelRequest
from TaohuaItempayurlGetRequest import TaohuaItempayurlGetRequest
from HuabaoChannelGetRequest import HuabaoChannelGetRequest
from ItempropvaluesGetRequest import ItempropvaluesGetRequest
from HuabaoPosterGetRequest import HuabaoPosterGetRequest
from PostageUpdateRequest import PostageUpdateRequest
from ItemsGetRequest import ItemsGetRequest
from TraderateAddRequest import TraderateAddRequest
from LogisticsTraceSearchRequest import LogisticsTraceSearchRequest
from TaohuaLatestupdateinfoGetRequest import TaohuaLatestupdateinfoGetRequest
from TimeGetRequest import TimeGetRequest
from TradeConfirmfeeGetRequest import TradeConfirmfeeGetRequest
from PictureGetRequest import PictureGetRequest
from TaobaokeShopsGetRequest import TaobaokeShopsGetRequest
from PromotionCoupondetailGetRequest import PromotionCoupondetailGetRequest
from TaobaokeReportGetRequest import TaobaokeReportGetRequest
from FenxiaoDiscountsGetRequest import FenxiaoDiscountsGetRequest
from TaohuaOrdersGetRequest import TaohuaOrdersGetRequest
from RefundsApplyGetRequest import RefundsApplyGetRequest
from WangwangEserviceChatrecordGetRequest import WangwangEserviceChatrecordGetRequest
from TaobaokeItemsGetRequest import TaobaokeItemsGetRequest
from TaohuaItemresurlGetRequest import TaohuaItemresurlGetRequest
from FavoriteAddRequest import FavoriteAddRequest
from RefundsReceiveGetRequest import RefundsReceiveGetRequest
from HuabaoSpecialpostersGetRequest import HuabaoSpecialpostersGetRequest
from PromotionCouponsGetRequest import PromotionCouponsGetRequest
from TaobaokeVirtualcardGetRequest import TaobaokeVirtualcardGetRequest
from WangwangEserviceChatlogGetRequest import WangwangEserviceChatlogGetRequest
from PromotionActivityDeleteRequest import PromotionActivityDeleteRequest
from ItemsInventoryGetRequest import ItemsInventoryGetRequest
from WangwangEserviceOnlinetimeGetRequest import WangwangEserviceOnlinetimeGetRequest
from TradeMemoUpdateRequest import TradeMemoUpdateRequest
from TradeMemoAddRequest import TradeMemoAddRequest
from TradeCloseRequest import TradeCloseRequest
from TaohuaChildcatesGetRequest import TaohuaChildcatesGetRequest
from SellercatsListGetRequest import SellercatsListGetRequest
from ItemUpdateListingRequest import ItemUpdateListingRequest
from TraderatesGetRequest import TraderatesGetRequest
from IncrementTradesGetRequest import IncrementTradesGetRequest
from ItemPropimgDeleteRequest import ItemPropimgDeleteRequest
from TaohuaBoughtitemIsRequest import TaohuaBoughtitemIsRequest
from ItemUpdateRequest import ItemUpdateRequest
from HuabaoChannelsGetRequest import HuabaoChannelsGetRequest
from ProductUpdateRequest import ProductUpdateRequest
from TradeOrderskuUpdateRequest import TradeOrderskuUpdateRequest
from FenxiaoProductsGetRequest import FenxiaoProductsGetRequest
from ProductPropimgDeleteRequest import ProductPropimgDeleteRequest
from PostageAddRequest import PostageAddRequest
from TradesSoldGetRequest import TradesSoldGetRequest
from TaobaokeItemsConvertRequest import TaobaokeItemsConvertRequest
from WangwangEserviceChatpeersGetRequest import WangwangEserviceChatpeersGetRequest
from TaohuaStaffrecitemsGetRequest import TaohuaStaffrecitemsGetRequest
from ProductsGetRequest import ProductsGetRequest
from TopatsDeliverySendRequest import TopatsDeliverySendRequest
from VasOrderSearchRequest import VasOrderSearchRequest
from FenxiaoGradesGetRequest import FenxiaoGradesGetRequest
from PromotionCouponAddRequest import PromotionCouponAddRequest
from ProductAddRequest import ProductAddRequest
from TraderateListAddRequest import TraderateListAddRequest
from ItemRecommendDeleteRequest import ItemRecommendDeleteRequest
from ProductPropimgUploadRequest import ProductPropimgUploadRequest
from WangwangEserviceAvgwaittimeGetRequest import WangwangEserviceAvgwaittimeGetRequest
from IncrementSubscribemessageGetRequest import IncrementSubscribemessageGetRequest
from DeliveryCodSendRequest import DeliveryCodSendRequest
from FenxiaoProductUpdateRequest import FenxiaoProductUpdateRequest
from KfcKeywordSearchRequest import KfcKeywordSearchRequest
from TaohuaItemdetailGetRequest import TaohuaItemdetailGetRequest
from VasSubscSearchRequest import VasSubscSearchRequest
from FenxiaoProductAddRequest import FenxiaoProductAddRequest
from TopatsTradesFullinfoGetRequest import TopatsTradesFullinfoGetRequest
from AftersaleGetRequest import AftersaleGetRequest
from RefundRefuseRequest import RefundRefuseRequest
from TradeShippingaddressUpdateRequest import TradeShippingaddressUpdateRequest
from WangwangEserviceReceivenumGetRequest import WangwangEserviceReceivenumGetRequest
from ProductImgUploadRequest import ProductImgUploadRequest
from TaohuaItemcommentAddRequest import TaohuaItemcommentAddRequest
from TradeFullinfoGetRequest import TradeFullinfoGetRequest
from VasSubscribeGetRequest import VasSubscribeGetRequest
from PictureCategoryGetRequest import PictureCategoryGetRequest
from ItemDeleteRequest import ItemDeleteRequest
from WangwangEserviceEvaluationGetRequest import WangwangEserviceEvaluationGetRequest
from PostageDeleteRequest import PostageDeleteRequest
from SellercatsListAddRequest import SellercatsListAddRequest
from TopatsResultGetRequest import TopatsResultGetRequest
from TradesSoldIncrementGetRequest import TradesSoldIncrementGetRequest
from LogisticsCompaniesGetRequest import LogisticsCompaniesGetRequest
from FavoriteSearchRequest import FavoriteSearchRequest

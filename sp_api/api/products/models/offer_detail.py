# coding: utf-8

"""
    Selling Partner API for Pricing

    The Selling Partner API for Pricing helps you programmatically retrieve product pricing and offer information for Amazon Marketplace products.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class OfferDetail(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'my_offer': 'bool',
        'sub_condition': 'str',
        'seller_feedback_rating': 'SellerFeedbackType',
        'shipping_time': 'DetailedShippingTimeType',
        'listing_price': 'MoneyType',
        'points': 'Points',
        'shipping': 'MoneyType',
        'ships_from': 'ShipsFromType',
        'is_fulfilled_by_amazon': 'bool',
        'is_buy_box_winner': 'bool',
        'is_featured_merchant': 'bool'
    }

    attribute_map = {
        'my_offer': 'MyOffer',
        'sub_condition': 'SubCondition',
        'seller_feedback_rating': 'SellerFeedbackRating',
        'shipping_time': 'ShippingTime',
        'listing_price': 'ListingPrice',
        'points': 'Points',
        'shipping': 'Shipping',
        'ships_from': 'ShipsFrom',
        'is_fulfilled_by_amazon': 'IsFulfilledByAmazon',
        'is_buy_box_winner': 'IsBuyBoxWinner',
        'is_featured_merchant': 'IsFeaturedMerchant'
    }

    def __init__(self, my_offer=None, sub_condition=None, seller_feedback_rating=None, shipping_time=None, listing_price=None, points=None, shipping=None, ships_from=None, is_fulfilled_by_amazon=None, is_buy_box_winner=None, is_featured_merchant=None):  # noqa: E501
        """OfferDetail - a model defined in Swagger"""  # noqa: E501
        self._my_offer = None
        self._sub_condition = None
        self._seller_feedback_rating = None
        self._shipping_time = None
        self._listing_price = None
        self._points = None
        self._shipping = None
        self._ships_from = None
        self._is_fulfilled_by_amazon = None
        self._is_buy_box_winner = None
        self._is_featured_merchant = None
        self.discriminator = None
        if my_offer is not None:
            self.my_offer = my_offer
        self.sub_condition = sub_condition
        if seller_feedback_rating is not None:
            self.seller_feedback_rating = seller_feedback_rating
        self.shipping_time = shipping_time
        self.listing_price = listing_price
        if points is not None:
            self.points = points
        self.shipping = shipping
        if ships_from is not None:
            self.ships_from = ships_from
        self.is_fulfilled_by_amazon = is_fulfilled_by_amazon
        if is_buy_box_winner is not None:
            self.is_buy_box_winner = is_buy_box_winner
        if is_featured_merchant is not None:
            self.is_featured_merchant = is_featured_merchant

    @property
    def my_offer(self):
        """Gets the my_offer of this OfferDetail.  # noqa: E501

        When true, this is the seller's offer.  # noqa: E501

        :return: The my_offer of this OfferDetail.  # noqa: E501
        :rtype: bool
        """
        return self._my_offer

    @my_offer.setter
    def my_offer(self, my_offer):
        """Sets the my_offer of this OfferDetail.

        When true, this is the seller's offer.  # noqa: E501

        :param my_offer: The my_offer of this OfferDetail.  # noqa: E501
        :type: bool
        """

        self._my_offer = my_offer

    @property
    def sub_condition(self):
        """Gets the sub_condition of this OfferDetail.  # noqa: E501

        The subcondition of the item. Subcondition values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.  # noqa: E501

        :return: The sub_condition of this OfferDetail.  # noqa: E501
        :rtype: str
        """
        return self._sub_condition

    @sub_condition.setter
    def sub_condition(self, sub_condition):
        """Sets the sub_condition of this OfferDetail.

        The subcondition of the item. Subcondition values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.  # noqa: E501

        :param sub_condition: The sub_condition of this OfferDetail.  # noqa: E501
        :type: str
        """
        if sub_condition is None:
            raise ValueError("Invalid value for `sub_condition`, must not be `None`")  # noqa: E501

        self._sub_condition = sub_condition

    @property
    def seller_feedback_rating(self):
        """Gets the seller_feedback_rating of this OfferDetail.  # noqa: E501


        :return: The seller_feedback_rating of this OfferDetail.  # noqa: E501
        :rtype: SellerFeedbackType
        """
        return self._seller_feedback_rating

    @seller_feedback_rating.setter
    def seller_feedback_rating(self, seller_feedback_rating):
        """Sets the seller_feedback_rating of this OfferDetail.


        :param seller_feedback_rating: The seller_feedback_rating of this OfferDetail.  # noqa: E501
        :type: SellerFeedbackType
        """

        self._seller_feedback_rating = seller_feedback_rating

    @property
    def shipping_time(self):
        """Gets the shipping_time of this OfferDetail.  # noqa: E501


        :return: The shipping_time of this OfferDetail.  # noqa: E501
        :rtype: DetailedShippingTimeType
        """
        return self._shipping_time

    @shipping_time.setter
    def shipping_time(self, shipping_time):
        """Sets the shipping_time of this OfferDetail.


        :param shipping_time: The shipping_time of this OfferDetail.  # noqa: E501
        :type: DetailedShippingTimeType
        """
        if shipping_time is None:
            raise ValueError("Invalid value for `shipping_time`, must not be `None`")  # noqa: E501

        self._shipping_time = shipping_time

    @property
    def listing_price(self):
        """Gets the listing_price of this OfferDetail.  # noqa: E501


        :return: The listing_price of this OfferDetail.  # noqa: E501
        :rtype: MoneyType
        """
        return self._listing_price

    @listing_price.setter
    def listing_price(self, listing_price):
        """Sets the listing_price of this OfferDetail.


        :param listing_price: The listing_price of this OfferDetail.  # noqa: E501
        :type: MoneyType
        """
        if listing_price is None:
            raise ValueError("Invalid value for `listing_price`, must not be `None`")  # noqa: E501

        self._listing_price = listing_price

    @property
    def points(self):
        """Gets the points of this OfferDetail.  # noqa: E501


        :return: The points of this OfferDetail.  # noqa: E501
        :rtype: Points
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this OfferDetail.


        :param points: The points of this OfferDetail.  # noqa: E501
        :type: Points
        """

        self._points = points

    @property
    def shipping(self):
        """Gets the shipping of this OfferDetail.  # noqa: E501


        :return: The shipping of this OfferDetail.  # noqa: E501
        :rtype: MoneyType
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """Sets the shipping of this OfferDetail.


        :param shipping: The shipping of this OfferDetail.  # noqa: E501
        :type: MoneyType
        """
        if shipping is None:
            raise ValueError("Invalid value for `shipping`, must not be `None`")  # noqa: E501

        self._shipping = shipping

    @property
    def ships_from(self):
        """Gets the ships_from of this OfferDetail.  # noqa: E501


        :return: The ships_from of this OfferDetail.  # noqa: E501
        :rtype: ShipsFromType
        """
        return self._ships_from

    @ships_from.setter
    def ships_from(self, ships_from):
        """Sets the ships_from of this OfferDetail.


        :param ships_from: The ships_from of this OfferDetail.  # noqa: E501
        :type: ShipsFromType
        """

        self._ships_from = ships_from

    @property
    def is_fulfilled_by_amazon(self):
        """Gets the is_fulfilled_by_amazon of this OfferDetail.  # noqa: E501

        When true, the offer is fulfilled by Amazon.  # noqa: E501

        :return: The is_fulfilled_by_amazon of this OfferDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_fulfilled_by_amazon

    @is_fulfilled_by_amazon.setter
    def is_fulfilled_by_amazon(self, is_fulfilled_by_amazon):
        """Sets the is_fulfilled_by_amazon of this OfferDetail.

        When true, the offer is fulfilled by Amazon.  # noqa: E501

        :param is_fulfilled_by_amazon: The is_fulfilled_by_amazon of this OfferDetail.  # noqa: E501
        :type: bool
        """
        if is_fulfilled_by_amazon is None:
            raise ValueError("Invalid value for `is_fulfilled_by_amazon`, must not be `None`")  # noqa: E501

        self._is_fulfilled_by_amazon = is_fulfilled_by_amazon

    @property
    def is_buy_box_winner(self):
        """Gets the is_buy_box_winner of this OfferDetail.  # noqa: E501

        When true, the offer is currently in the Buy Box. There can be up to two Buy Box winners at any time per ASIN, one that is eligible for Prime and one that is not eligible for Prime.  # noqa: E501

        :return: The is_buy_box_winner of this OfferDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_buy_box_winner

    @is_buy_box_winner.setter
    def is_buy_box_winner(self, is_buy_box_winner):
        """Sets the is_buy_box_winner of this OfferDetail.

        When true, the offer is currently in the Buy Box. There can be up to two Buy Box winners at any time per ASIN, one that is eligible for Prime and one that is not eligible for Prime.  # noqa: E501

        :param is_buy_box_winner: The is_buy_box_winner of this OfferDetail.  # noqa: E501
        :type: bool
        """

        self._is_buy_box_winner = is_buy_box_winner

    @property
    def is_featured_merchant(self):
        """Gets the is_featured_merchant of this OfferDetail.  # noqa: E501

        When true, the seller of the item is eligible to win the Buy Box.  # noqa: E501

        :return: The is_featured_merchant of this OfferDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_featured_merchant

    @is_featured_merchant.setter
    def is_featured_merchant(self, is_featured_merchant):
        """Sets the is_featured_merchant of this OfferDetail.

        When true, the seller of the item is eligible to win the Buy Box.  # noqa: E501

        :param is_featured_merchant: The is_featured_merchant of this OfferDetail.  # noqa: E501
        :type: bool
        """

        self._is_featured_merchant = is_featured_merchant

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OfferDetail, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OfferDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
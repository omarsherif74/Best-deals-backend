from helpers import percentToFraction

class Heuristic:

  def __init__(self, products):
    self.products = products

  def normalize(self):
    totalPrices = [product.totalPrice() for product in self.products]
    ratesScore = [product.rate * product.reviewsCount for product in self.products]

    minRateScore, maxRateScore = min(ratesScore), max(ratesScore)
    minTotalPrice, maxTotalPrice = min(totalPrices), max(totalPrices)

    if len(self.products) == 0: #TODO: Normalize on all sites
      product.setScore(ratesScore[0] - totalPrices[0])
      return

    for product in self.products:
      max_min_price_diff = maxTotalPrice-minTotalPrice
      max_min_rate_diff = maxRateScore-minRateScore

      weights = [-9, -3, 0, 3, 9]    

      normalizedTotalPrice = 1
      normalizedRate = 1

      if max_min_price_diff != 0:
        normalizedTotalPrice = (product.totalPrice() - minTotalPrice)/(max_min_price_diff)
      if max_min_price_diff != 0:
        normalizedRate = (weights[round(product.rate-1)] * product.reviewsCount - minRateScore)/(max_min_rate_diff)

      product.setScore(normalizedRate - normalizedTotalPrice)

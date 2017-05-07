#set working dir
setwd("C:/Users/Finbar/PycharmProjects/fyp")
#read in data

install.packages("zoo")
install.packages("forecast")

library(readr)
library(forecast)
library(lmtest)




###
###  priceVcounts (daily btc price Vs daily neg sentiment )
###
## try to get granger
## ref - https://www.r-bloggers.com/chicken-or-the-egg-granger-causality-for-the-masses/
# plot the time series
priceVneg <- read.csv("~/PycharmProjects/fyp/data_preprocessers/tweet_vol_senti.csv",header = T)
#View(priceVneg)
head(priceVneg)
par(mfrow=c(2,1))
plot.ts(priceVneg$usd)
plot.ts(priceVneg$neg)

##ccf - cross correlation with lags
ts.usd <- ts(priceVneg$usd)
ts.neg <- ts(priceVneg$neg)
ccf(ts.neg, ts.usd)
ccfvals <- ccf(ts.neg, ts.usd)
ccfvals

# test for unit root and number of differences required, 
# you can also test for seasonality with nsdiffs
ndiffs(priceVneg$usd, alpha=0.05, test=c("kpss"))
ndiffs(priceVneg$neg, alpha=0.05, test=c("kpss"))
# differenced time series
d.usd <- diff(priceVneg$usd)
d.neg <- diff(priceVneg$neg)
plot.ts(d.usd)
plot.ts(d.neg)
##lag 5
# do tweet counts granger casue usd price?
grangertest(d.usd ~ d.neg, order=5)
# do usd price granger casue tweet count?
grangertest(d.neg ~ d.usd, order=5)
##lag 4
# do tweet counts granger casue usd price?
grangertest(d.usd ~ d.neg, order=4)
# do usd price granger casue tweet count?
grangertest(d.neg ~ d.usd, order=4)
##lag 3
# do tweet counts granger casue usd price?
grangertest(d.usd ~ d.neg, order=3)
# do usd price granger casue tweet count?
grangertest(d.neg ~ d.usd, order=3)
##lag 2
# do tweet counts granger casue usd price?
grangertest(d.usd ~ d.neg, order=2)
# do usd price granger casue tweet count?
grangertest(d.neg ~ d.usd, order=2)
##lag 1
# do tweet counts granger casue usd price?
grangertest(d.usd ~ d.neg, order=1)
# do usd price granger casue tweet count?
grangertest(d.neg ~ d.usd, order=1)

# cor
cor(d.neg, d.usd)
cor(priceVneg$usd, priceVneg$neg)
cor.test(priceVneg$usd, priceVneg$neg)

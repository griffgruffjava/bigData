#set working dir
setwd("C:/Users/Finbar/PycharmProjects/fyp")
#read in data

install.packages("zoo")
install.packages("forecast")

library(readr)
library(forecast)
library(lmtest)




###
###  priceVcounts (daily btc price Vs daily pos sentiment)
###                       82 
## try to get granger
## ref - https://www.r-bloggers.com/chicken-or-the-egg-granger-causality-for-the-masses/
# plot the time series
priceVpos <- read.csv("~/PycharmProjects/fyp/data_preprocessers/tweet_vol_senti.csv",header = T)
View(priceVpos)
head(priceVpos)
par(mfrow=c(2,1))
plot.ts(priceVpos$usd)
plot.ts(priceVpos$pos)

##ccf - cross correlation with lags
ts.usd <- ts(priceVpos$usd)
ts.pos <- ts(priceVpos$pos)
ccf(ts.pos, ts.usd)
ccfvals <- ccf(ts.pos, ts.usd)
ccfvals

# test for unit root and number of differences required, 
# you can also test for seasonality with nsdiffs
ndiffs(priceVpos$usd, alpha=0.05, test=c("kpss"))
ndiffs(priceVpos$pos, alpha=0.05, test=c("kpss"))
# differenced time series
d.usd <- diff(priceVpos$usd)
d.pos <- diff(priceVpos$pos)
plot.ts(d.usd)
plot.ts(d.pos)

##lag 5
# do tweet counts granger casue usd price?
grangertest(d.usd ~ d.pos, order=5)
# do usd price granger casue tweet count?
grangertest(d.pos ~ d.usd, order=5)
##lag 4
# do tweet counts granger casue usd price?
grangertest(d.usd ~ d.pos, order=4)
# do usd price granger casue tweet count?
grangertest(d.pos ~ d.usd, order=4)
##lag 3
# do tweet counts granger casue usd price?
grangertest(d.usd ~ d.pos, order=3)
# do usd price granger casue tweet count?
grangertest(d.pos ~ d.usd, order=3)
##lag 2
# do tweet counts granger casue usd price?
grangertest(d.usd ~ d.pos, order=2)
# do usd price granger casue tweet count?
grangertest(d.pos ~ d.usd, order=2)
##lag 1
# do tweet counts granger casue usd price?
grangertest(d.usd ~ d.pos, order=1)
# do usd price granger casue tweet count?
grangertest(d.pos ~ d.usd, order=1)

# cor
cor(d.pos, d.usd)
cor(priceVpos$usd, priceVpos$pos)
cor.test(priceVpos$usd, priceVpos$pos)



#set working dir
setwd("C:/Users/Finbar/PycharmProjects/fyp")
#read in data

install.packages("zoo")
install.packages("forecast")

library(readr)
library(forecast)
library(lmtest)





###
###  priceVcounts (daily btc price Vs daily sentiment difference)
###
## try to get granger
## ref - https://www.r-bloggers.com/chicken-or-the-egg-granger-causality-for-the-masses/
# plot the time series
priceVdiff <- read.csv("~/PycharmProjects/fyp/data_preprocessers/tweet_vol_senti.csv",header = T)
View(priceVdiff)
head(priceVdiff)
par(mfrow=c(2,1))
plot.ts(priceVdiff$usd)
plot.ts(priceVdiff$diff)

##ccf - cross correlation with lags
ts.usd <- ts(priceVdiff$usd)
ts.diff <- ts(priceVdiff$diff)
ccf(ts.diff, ts.usd)
ccfvals <- ccf(ts.diff, ts.usd)
ccfvals


# test for unit root and number of differences required, 
# you can also test for seasonality with nsdiffs
ndiffs(priceVdiff$usd, alpha=0.05, test=c("kpss"))
ndiffs(priceVdiff$diff, alpha=0.05, test=c("kpss"))
# differenced time series
d.usd <- diff(priceVdiff$usd)
d.diff <- diff(priceVdiff$diff)
plot.ts(d.usd)
plot.ts(d.diff)
##lag 5
# do tweet counts granger casue usd price?
grangertest(d.usd ~ d.diff, order=5)
# do usd price granger casue tweet count?
grangertest(d.diff ~ d.usd, order=5)
##lag 4
# do tweet counts granger casue usd price?
grangertest(d.usd ~ d.diff, order=4)
# do usd price granger casue tweet count?
grangertest(d.diff ~ d.usd, order=4)
##lag 3
# do tweet counts granger casue usd price?
grangertest(d.usd ~ d.diff, order=3)
# do usd price granger casue tweet count?
grangertest(d.diff ~ d.usd, order=3)
##lag 2
# do tweet counts granger casue usd price?
grangertest(d.usd ~ d.diff, order=2)
# do usd price granger casue tweet count?
grangertest(d.diff ~ d.usd, order=2)
##lag 1
# do tweet counts granger casue usd price?
grangertest(d.usd ~ d.diff, order=1)
# do usd price granger casue tweet count?
grangertest(d.diff ~ d.usd, order=1)

# cor
cor(d.diff, d.usd)
cor(priceVdiff$usd, priceVdiff$diff)
cor.test(priceVdiff$usd, priceVdiff$diff)


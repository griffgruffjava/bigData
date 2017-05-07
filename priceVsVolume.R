#set working dir
setwd("C:/Users/Finbar/PycharmProjects/fyp")
#read in data

install.packages("zoo")
install.packages("forecast")

library(readr)
library(forecast)
library(lmtest)



###
###  priceVcounts (daily btc price Vs daily tweet count)
###               (82 obs from 2/2/2017 - 24/4/2017)
## try to get granger
## ref - https://www.r-bloggers.com/chicken-or-the-egg-granger-causality-for-the-masses/
# plot the time series
priceVvolume <- read.csv("~/PycharmProjects/fyp/data_preprocessers/tweet_vol_senti.csv",header = T)
View(priceVvolume)
head(priceVvolume)
par(mfrow=c(2,1))
plot.ts(priceVvolume$usd)
plot.ts(priceVvolume$count)

##ccf - cross correlation with lags
ts.usd <- ts(priceVvolume$usd)
ts.count <- ts(priceVvolume$count)
ccf(ts.count, ts.usd)
ccfvals <- ccf(ts.count, ts.usd)
ccfvals

# test for unit root and number of differences required, 
# you can also test for seasonality with nsdiffs
ndiffs(priceVvolume$usd, alpha=0.05, test=c("kpss"))
ndiffs(priceVvolume$count, alpha=0.05, test=c("kpss"))
# differenced time series
d.usd <- diff(priceVvolume$usd)
d.count <- diff(priceVvolume$count)
plot.ts(d.usd)
plot.ts(d.count)
##lag 5
# do tweet volume granger casue usd price?
grangertest(d.usd ~ d.count, order=5)
# do usd price granger casue tweet volume?
grangertest(d.count ~ d.usd, order=5)
##lag 4
# do tweet volume granger casue usd price?
grangertest(d.usd ~ d.count, order=4)
# do usd price granger casue tweet volume?
grangertest(d.count ~ d.usd, order=4)
##lag 3
# do tweet volume granger casue usd price?
grangertest(d.usd ~ d.count, order=3)
# do usd price granger casue tweet volume?
grangertest(d.count ~ d.usd, order=3)
##lag 2
# do tweet volume granger casue usd price?
grangertest(d.usd ~ d.count, order=2)
# do usd price granger casue tweet volume?
grangertest(d.count ~ d.usd, order=2)
##lag 1
# do tweet volume granger casue usd price?
grangertest(d.usd ~ d.count, order=1)
# do usd price granger casue tweet volume?
grangertest(d.count ~ d.usd, order=1)

# find Pearson cor
cor(d.count, d.usd)
cor(priceVvolume$usd, priceVvolume$count)
cor.test(priceVvolume$usd, priceVvolume$count)



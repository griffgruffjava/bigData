

#set working dir
setwd("C:/Users/Finbar/PycharmProjects/fyp")
#read in data

install.packages("zoo")
install.packages("forecast")

library(readr)
library(forecast)
library(lmtest)


###
###  google_trends (daily btc price AND daily google trend score 
###                       268 obs          from 02/08/2016 - 26/04/2017 )
###
## try to get granger
## ref - https://www.r-bloggers.com/chicken-or-the-egg-granger-causality-for-the-masses/
# plot the time series
dailys <- read.csv("~/PycharmProjects/fyp/data_preprocessers/daily_trends_trimmed_VER2.csv",header = T)
#View(dailys)
head(dailys)
par(mfrow=c(2,1))
plot.ts(dailys$usd)
plot.ts(dailys$trend)

##ccf
ts.usd <- ts(dailys$usd)
ts.trend <- ts(dailys$trend)
ccf(ts.trend, ts.usd)
ccf(ts.usd, ts.trend)
ccfvals <- ccf(ts.trend, ts.usd)
ccfvals

# test for unit root and number of differences required, 
# you can also test for seasonality with nsdiffs
ndiffs(dailys$usd, alpha=0.05, test=c("kpss"))
ndiffs(dailys$trend, alpha=0.05, test=c("kpss"))
# differenced time series
d.dailys.usd <- diff(dailys$usd)
d.dailys.trend <- diff(dailys$trend)
plot.ts(d.dailys.usd)
plot.ts(d.dailys.trend)
##lag 5
# do google trends granger casue usd price?
grangertest(d.dailys.usd ~ d.dailys.trend, order=5)
# do usd price granger casue google trends?
grangertest(d.dailys.trend ~ d.dailys.usd, order=5)
##lag 4
# do google trends granger casue usd price?
grangertest(d.dailys.usd ~ d.dailys.trend, order=4)
# do usd price granger casue google trends?
grangertest(d.dailys.trend ~ d.dailys.usd, order=4)
##lag 3
# do google trends granger casue usd price?
grangertest(d.dailys.usd ~ d.dailys.trend, order=3)
# do usd price granger casue google trends?
grangertest(d.dailys.trend ~ d.dailys.usd, order=3)
##lag 2
# do google trends granger casue usd price?
grangertest(d.dailys.usd ~ d.dailys.trend, order=2)
# do usd price granger casue google trends?
grangertest(d.dailys.trend ~ d.dailys.usd, order=2)
##lag 1
# do google trends granger casue usd price?
grangertest(d.dailys.usd ~ d.dailys.trend, order=1)
# do usd price granger casue google trends?
grangertest(d.dailys.trend ~ d.dailys.usd, order=1)

# looking at correlation
cor(d.dailys.trend,d.dailys.usd)
cor(dailys$usd,dailys$trend)

cor.test(dailys$usd,dailys$trend)


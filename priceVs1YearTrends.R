#set working dir
setwd("C:/Users/Finbar/PycharmProjects/fyp")
#read in data

install.packages("zoo")
install.packages("forecast")

library(readr)
library(forecast)
library(lmtest)


###
###  google_trends (weekly btc price AND weekly google trend score)
###                   260 obs     4/8/2012 - 26/3/2017
## try to get granger
## ref - https://www.r-bloggers.com/chicken-or-the-egg-granger-causality-for-the-masses/
# plot the time series
google_trends <- read.csv("~/PycharmProjects/fyp/data_preprocessers/2016_weekly_trends.csv",header = T)
#View(google_trends)
head(google_trends)
par(mfrow=c(2,1))
plot.ts(google_trends$usd, ylab="USD Price", xlab = "Week")
plot.ts(google_trends$trend, ylab="Trend Value", xlab = "Week")

##ccf
ts.usd <- ts(google_trends$usd)
ts.trend <- ts(google_trends$trend)
ccf(ts.trend, ts.usd)
ccf(ts.usd, ts.trend, main = "USD & Google Trends")
ccfvals <- ccf(ts.trend, ts.usd, 5)
ccfvals



# test for unit root and number of differences required, 
# you can also test for seasonality with nsdiffs
ndiffs(google_trends$usd, alpha=0.05, test=c("kpss"))
ndiffs(google_trends$trend, alpha=0.05, test=c("kpss"))
# differenced time series
d.weeklyusd <- diff(google_trends$usd)
d.trend <- diff(google_trends$trend)
plot.ts(d.weeklyusd)
plot.ts(d.trend)
##lag 5
# do google trends granger casue usd price?
grangertest(d.weeklyusd ~ d.trend, order=5)
# do usd price granger casue google trends?
grangertest(d.trend ~ d.weeklyusd, order=5)
##lag 4
# do google trends granger casue usd price?
grangertest(d.weeklyusd ~ d.trend, order=4)
# do usd price granger casue google trends?
grangertest(d.trend ~ d.weeklyusd, order=4)
##lag 3
# do google trends granger casue usd price?
grangertest(d.weeklyusd ~ d.trend, order=3)
# do usd price granger casue google trends?
grangertest(d.trend ~ d.weeklyusd, order=3)
##lag 2
# do google trends granger casue usd price?
grangertest(d.weeklyusd ~ d.trend, order=2)
# do usd price granger casue google trends?
grangertest(d.trend ~ d.weeklyusd, order=2)
##lag 1
# do google trends granger casue usd price?
grangertest(d.weeklyusd ~ d.trend, order=1)
# do usd price granger casue google trends?
grangertest(d.trend ~ d.weeklyusd, order=1)

# correlation
cor(d.trend, d.weeklyusd)
cor(google_trends$usd, google_trends$trend)
cor.test(google_trends$usd, google_trends$trend)
cor.test(google_trends$trend, google_trends$usd)


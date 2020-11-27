#Esantionare dintr-o populatie normala de medie m si dispersie sigma^2
m <- 7
sigma <- 4
xbar <- c()
for (i in 1:1000)
{
x <- rnorm(10^4,m,sigma)
xbar <-c(xbar,mean(x))
#dispersie <- var(x)
}
medie_xbar <- mean(xbar)
dispersie_xbar <- var(xbar)
hist(xbar)
hist(x)
#Simularea unei valori dintr-o exponentiala de parametru lambda
lambda <- 3
set.seed(15)
u <- runif(1)
x <- -1/lambda*log(u)

t <- seq(-1,5,0.001)
plot(t,dexp(t,lambda),col="green")

#Simularea a 10^6 valori dintr-o exponentiala de parametru lambda
u <- runif(10^6)
x <- -1/lambda*log(u)
hist(x,freq=F)
lines(t,dexp(t,lambda),col="green")

#TEMA: Construiti un algoritm care simuleaza 10^6 valori din repartitia
#lucrata in exemplul cu metoda inversa

# Algoritmul pentru simularea unei valori dintr-o variabila aleatoare
#discreta X:(1 2 3 4 5;10/30 1/30 4/30 7/30 8/30)
val <- 1:5
prob <- c(1/3,1/30,2/15,7/30,4/15)
u <- runif(1)
if (u<prob[1]) { x=val[1]
} else if (u<prob[1]+prob[2]) {x=val[2]
}else {if (u<prob[1]+prob[2]+prob[3]) x=val[3]
else  if (u<prob[1]+prob[2]+prob[3]+prob[4]) x=val[4]
else x=val[5]
}         

#TEMA: Eficientizati cat de mult posibil algoritmul de mai sus
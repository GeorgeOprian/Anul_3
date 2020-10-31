#simularea unei valori dintr-o exponetiala de param lambda
lambda <- 3
set.seed(15)
u <- runif(1)
x <- -1 / lambda * log(u)

t <- seq (-1, 5, 0.001)
plot (t, dexp(t, lambda), col = "green")

#simulare a 10^6 valori dintr-o exponentiala de param lambda

u <- runif(10^6)
x <- -1/lambda*log(u)
hist (x, freq = F)
lines (t, dexp(t, lambda), col = "green")

#TEMA
#Construiti un alg care simuleaza 10^6 valori din repartitia lucrata in lab cu metoda inversa   
 

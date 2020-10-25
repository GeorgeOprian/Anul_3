#Reperzentari grafice de functii
#Functia densitatea de prob a repartitieri normale

t <- seq(-6, 6, 0.001)
plot (t, dnorm(t, 0, 1))
plot(t, dexp(t, 2), ylim=c(0, 0.))
#ATENTIE: int R parametrii normalei sunt media si abaterea medie standard

#densitatea e o functie care caracterizeaza o var aleatoare continua
#daca integram denstatea obtinem probabilitatea
y <- rnorm(100000, 0, 1)
poz <- y[y>0]
nr_poz <- length(poz)
neg <- y[y<0]
nr_neg <- length(neg)

y <- rnorm (100, 0, 1)
length(y[(y>-3) & (y<3)])


lines(t, dnorm(t, 0, 1))

plot (t, dnorm(t, 0, 1), col = "magenta", xlim = c(-3, 3), ylim = c(0, 1)) # xlim si ylim pentru zoom
#plot face graficul principal si iti zice ce dimensiuni au axele
#functia din plot e principala si e linia ingrosata

lines(t, dnorm(t, 0, 4), col = 2) #graficul se aplatizeaza
lines(t, dnorm(t, 0, 0.5), col = 2) #graficul se ascute
#lines adauga linii subtiri in graficul facut cu plot 

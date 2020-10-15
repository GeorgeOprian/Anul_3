# Repartitii de v.a.
1.d+nume_repartitie=functie de masa(caz discret)/functia de densitate(caz continuu)
functia de masa:
  f(x)=P(X=x)
dbinom(x,n,p)
dbinom(2,6,0.8)
dbinom(1:3,6,0.8)
densitatea de probabilitate:
  f(x)<>probabilitate
dexp(x,lambda)
dexp(2,1) <- NU e o probabilitate
2. p+nume_repartitie=functia de repartitie
F(x)=P(X<=x)
pbinom(x,n,p)
pbinom(2,6,0.8)
pbinom(1:3,6,0.8)

3. r+nume_repartitie=genereaza valori din acel tip de repartitie
rbinom(nr,n,p)
rbinom(5,6,0.8)
rexp(3,1)


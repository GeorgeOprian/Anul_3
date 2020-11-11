#Eficientizarea algoritmului metodei inverse pe cazul discret
#Varianta lui Claudiu Mocanu

# problema initiala, cu valori de la 1 la 5

val <- 1:5
prob <- c(1/3,1/30,2/15,7/30,4/15)
u <- runif(1)
x <- length(prob[cumsum(prob)<u])+1
print(x)

# problema cu valori random a,b,c,d,e, cu cond. ca a<b<c<d<e
val <- c(2, 17, 35, 36, 51)
prob <- c(1/3,1/30,2/15,7/30,4/15)
u <- runif(1)
x <- val[length(prob[cumsum(prob)<u])+1]
print(x)

#Alta varianta
#val <- 1:5
prob <- c(1/3, 1/30, 2/15, 7/30, 4/15)
#Pt sortarea vectorului putem folosi sort()
u <- runif(1)
#x <- min(which(cumsum(prob)-u>0))
x <- which(cumsum(prob)-u>0)[1]

#Mai general
val <- c(2, 17, 35, 36, 51)
prob <- c(1/3,1/30,2/15,7/30,4/15)
u <- runif(1)
x <- val[which(cumsum(prob)-u>0)[1]]

#Folosirea functiilor in R

f <- function()
{
  # optional return()
}
#O functie returneaza prin numele sau ultima prelucrare din corpul functiei
#chiar daca nu folosim return, lucru foarte util pentru stocarea unei expresii matematice

f1 <- function(x)
{
   -2*x^2+x
  #x^5
  g <- 5
}
# FENOMEN CIUDAT
# Daca ultima instructiune din corpul functiei este o atribuire nu se afiseaza nimic
#dar daca cerem (f11(-1)), adica afisarea ultimei instructiuni executate, atunci 
#se afiseaza rezultatul intors de aceasta
f11 <- function(x)
{
  x <- -2*x^2+x
  
#  return(x)
}

(f1(-1))
f11(-1)
(y <- f11(-1))

f3 <- function(x)
{
  x^3
}

#Calculam integrala din f3
a <- integrate(f3,0,1)
a$value
b <- integrate(f3,0,1)$value
#Functia Gama cu George Oprian
fg <- function (x, a){
  x ^ (a - 1) * exp(-x)
}
fGama <-  function (f) {
  return (integrate(f, 0, Inf, a = 5)$value)
  
}

fGama(fg)



#Tema creati o functie in R numita gama_nume care sa implementeze proprietatile
#pe care le are functia gama(vezi documentul Integrale euleriene) si sa 
#foloseasca apelul functiei integrate doar atunci cand parametrul nu satisface 
#nicio conditie "buna"

# gama_nume <- function(....)
#{
#daca n e natural atunci foloseste propr. 3) #Puteti folosi functia din R factorial()
#daca n e de forma b/2(cu b natural) foloseste formula 2) si 4)
#altfel foloseste formula 2) pana cand argumentul devine subunitar
#si doar pentru acea valoare calculeaza cu integrate
#}

#Tema : de implementat o functie care genereaza n valori dintr-o v.a. repartizata
#Poisson de parametru lambda
#+de demonstrat relatia de recurenta de la Poisson din pdf-ul Lab4 Simulare




